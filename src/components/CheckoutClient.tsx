"use client";

import { useState } from "react";
import { useCart } from "@/context/CartContext";
import { usePaystackPayment } from "react-paystack";
import { useRouter } from "next/navigation";
import { useToast } from "@/context/ToastContext";

const NIGERIAN_STATES = [
  "Abia", "Abuja (FCT)", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", 
  "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe", "Imo", "Jigawa", "Kaduna", 
  "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", 
  "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara", "Test"
];

const NORTHERN_STATES = [
  "Adamawa", "Bauchi", "Benue", "Borno", "Gombe", "Jigawa", 
  "Kaduna", "Katsina", "Kebbi", "Kogi", "Nasarawa", "Niger", 
  "Plateau", "Sokoto", "Taraba", "Yobe", "Zamfara"
];

function getDeliveryFee(state: string) {
  if (!state) return 0;
  if (state === "Test") return 50;
  if (state === "Kwara") return 3000;
  if (NORTHERN_STATES.includes(state)) return 8000;
  return 5000;
}

export default function CheckoutClient() {
  const { items, cartTotal, clearCart } = useCart();
  const { addToast } = useToast();
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [address, setAddress] = useState("");
  const [deliveryState, setDeliveryState] = useState("");
  const [paymentMethod, setPaymentMethod] = useState("paystack");
  const [isProcessing, setIsProcessing] = useState(false);
  const router = useRouter();

  const deliveryFee = getDeliveryFee(deliveryState);
  const finalTotal = cartTotal + deliveryFee;

  const config = {
    reference: (new Date()).getTime().toString(),
    email: email,
    amount: finalTotal * 100, // Paystack amount is in kobo (base currency * 100)
    publicKey: process.env.NEXT_PUBLIC_PAYSTACK_PUBLIC_KEY || "pk_live_487bcd15b31ec3a647f35535581b8f52e34c05b1",
  };

  const initializePayment = usePaystackPayment(config);

  const onSuccess = async (reference: any) => {
    try {
      setIsProcessing(true);
      const res = await fetch('/api/checkout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          reference: reference.reference,
          name,
          email,
          phone,
          address,
          state: deliveryState,
          items: items.map(item => ({
            id: item.productId,
            quantity: item.quantity,
            size: item.size,
          }))
        })
      });
      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        console.error("Failed to save order to DB", errData);
        addToast(`Database Error: ${errData.details || 'Unknown error'}`);
        return;
      }
      
      addToast("Order placed successfully!");
      clearCart();
      
      router.push("/success");
    } catch (e: any) {
      console.error(e);
      addToast(`Network error: ${e?.message || 'Unknown'}`);
    } finally {
      setIsProcessing(false);
    }
  };

  const onClose = () => {
    // implementation for whatever you want to do when the Paystack dialog closed.
    console.log("Payment modal closed");
  };

  const handleCheckout = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !name || !phone || !address || !deliveryState) {
      addToast("Please fill in all fields including State");
      return;
    }
    
    if (paymentMethod === "paystack") {
      initializePayment({ onSuccess, onClose });
    } else {
      // Crypto Checkout
      try {
        setIsProcessing(true);
        const res = await fetch('/api/checkout-crypto', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            name,
            email,
            phone,
            address,
            state: deliveryState,
            items: items.map(item => ({
              id: item.productId,
              quantity: item.quantity,
              size: item.size,
            }))
          })
        });
        
        const data = await res.json();
        
        if (!res.ok) {
          addToast(`Error: ${data.details || data.error || 'Unknown error'}`);
          setIsProcessing(false);
          return;
        }
        
        clearCart();
        window.location.href = data.invoice_url; // Redirect to NowPayments
      } catch (e: any) {
        console.error(e);
        addToast(`Network error: ${e?.message || 'Unknown'}`);
        setIsProcessing(false);
      }
    }
  };

  if (items.length === 0) {
    return (
      <div className="container" style={{ padding: '4rem 1.5rem', textAlign: 'center' }}>
        <h2>Your cart is empty</h2>
        <button className="btn btn-primary" style={{ marginTop: '2rem' }} onClick={() => router.push("/")}>Continue Shopping</button>
      </div>
    );
  }

  return (
    <div className="container" style={{ padding: '4rem 1.5rem', display: 'flex', gap: '4rem', flexWrap: 'wrap' }}>
      <div style={{ flex: '1 1 400px' }}>
        <h2 style={{ marginBottom: '2rem' }}>Checkout Details</h2>
        <form onSubmit={handleCheckout} style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <div>
            <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Full Name</label>
            <input 
              type="text" 
              className="input-field" 
              value={name} 
              onChange={e => setName(e.target.value)} 
              required 
            />
          </div>
          <div>
            <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Email Address</label>
            <input 
              type="email" 
              className="input-field" 
              value={email} 
              onChange={e => setEmail(e.target.value)} 
              required 
            />
          </div>
          <div>
            <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Phone Number</label>
            <input 
              type="tel" 
              className="input-field" 
              value={phone} 
              onChange={e => setPhone(e.target.value)} 
              required 
            />
          </div>
          <div>
            <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>State</label>
            <select 
              className="input-field" 
              value={deliveryState} 
              onChange={e => setDeliveryState(e.target.value)} 
              required
              style={{ backgroundColor: 'var(--background)' }}
            >
              <option value="" disabled>Select a state</option>
              {NIGERIAN_STATES.map(st => (
                <option key={st} value={st}>{st}</option>
              ))}
            </select>
          </div>
          <div>
            <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Delivery Address</label>
            <textarea 
              className="input-field" 
              value={address} 
              onChange={e => setAddress(e.target.value)} 
              required 
              style={{ minHeight: '100px', resize: 'vertical' }}
            />
          </div>
          <div>
            <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Payment Method</label>
            <div style={{ display: 'flex', gap: '1rem' }}>
              <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer', padding: '0.75rem 1rem', border: `1px solid ${paymentMethod === 'paystack' ? 'var(--primary)' : 'var(--border)'}`, borderRadius: '4px', flex: 1, backgroundColor: paymentMethod === 'paystack' ? 'rgba(220, 38, 38, 0.1)' : 'transparent' }}>
                <input 
                  type="radio" 
                  name="paymentMethod" 
                  value="paystack" 
                  checked={paymentMethod === 'paystack'} 
                  onChange={() => setPaymentMethod('paystack')}
                  style={{ accentColor: 'var(--primary)' }}
                />
                Card / Bank
              </label>
              <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer', padding: '0.75rem 1rem', border: `1px solid ${paymentMethod === 'crypto' ? 'var(--primary)' : 'var(--border)'}`, borderRadius: '4px', flex: 1, backgroundColor: paymentMethod === 'crypto' ? 'rgba(220, 38, 38, 0.1)' : 'transparent' }}>
                <input 
                  type="radio" 
                  name="paymentMethod" 
                  value="crypto" 
                  checked={paymentMethod === 'crypto'} 
                  onChange={() => setPaymentMethod('crypto')}
                  style={{ accentColor: 'var(--primary)' }}
                />
                Crypto (NowPayments)
              </label>
            </div>
          </div>
          <button type="submit" className="btn btn-primary" disabled={isProcessing} style={{ padding: '1rem', fontSize: '1.125rem', marginTop: '1rem' }}>
            {isProcessing ? 'Processing Order...' : `Pay ₦${finalTotal.toFixed(2)} with ${paymentMethod === 'paystack' ? 'Paystack' : 'Crypto'}`}
          </button>
        </form>
      </div>
      
      <div style={{ flex: '1 1 300px' }}>
        <div className="glass-card" style={{ padding: '2rem' }}>
          <h3 style={{ marginBottom: '1.5rem' }}>Order Summary</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', marginBottom: '2rem' }}>
            {items.map(item => (
              <div key={item.id} style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: '1rem', borderBottom: '1px solid var(--border)' }}>
                <div>
                  <div style={{ fontWeight: 500 }}>{item.name}</div>
                  <div style={{ fontSize: '0.875rem', color: 'var(--text-muted)' }}>Size: {item.size} &times; {item.quantity}</div>
                </div>
                <div style={{ fontWeight: 600 }}>₦{(item.price * item.quantity).toFixed(2)}</div>
              </div>
            ))}
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '1rem', marginBottom: '1rem', color: 'var(--text-muted)' }}>
            <span>Items Subtotal</span>
            <span>₦{cartTotal.toFixed(2)}</span>
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '1rem', marginBottom: '1.5rem', color: 'var(--text-muted)' }}>
            <span>Delivery Fee ({deliveryState || 'Select State'})</span>
            <span>₦{deliveryFee.toFixed(2)}</span>
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '1.25rem', fontWeight: 700, borderTop: '1px solid var(--border)', paddingTop: '1rem' }}>
            <span>Total</span>
            <span>₦{finalTotal.toFixed(2)}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
