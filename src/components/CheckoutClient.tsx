"use client";

import { useState } from "react";
import { useCart } from "@/context/CartContext";
import { usePaystackPayment } from "react-paystack";
import { useRouter } from "next/navigation";

export default function CheckoutClient() {
  const { items, cartTotal, clearCart } = useCart();
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [address, setAddress] = useState("");
  const [isProcessing, setIsProcessing] = useState(false);
  const router = useRouter();

  const config = {
    reference: (new Date()).getTime().toString(),
    email: email,
    amount: cartTotal * 100, // Paystack amount is in kobo (base currency * 100)
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
          items: items.map(item => ({
            id: item.productId,
            name: item.name,
            price: item.price,
            quantity: item.quantity,
            size: item.size,
          })),
          total: cartTotal
        })
      });
      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        console.error("Failed to save order to DB", errData);
        alert(`Database Error: ${errData.details || 'Unknown error'}`);
        return;
      }
      
      const result = await res.json();
      // Temporary debug: show email status
      alert(`Order saved! Email status: ${result.emailStatus}${result.emailError ? ' - Error: ' + JSON.stringify(result.emailError) : ''}`);
      
      clearCart();
      router.push("/success");
    } catch (e: any) {
      console.error(e);
      alert(`Network error: ${e?.message || 'Unknown'}`);
    } finally {
      setIsProcessing(false);
    }
  };

  const onClose = () => {
    // implementation for whatever you want to do when the Paystack dialog closed.
    console.log("Payment modal closed");
  };

  const handleCheckout = (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !name || !phone || !address) return;
    initializePayment({ onSuccess, onClose });
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
            <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Delivery Address</label>
            <textarea 
              className="input-field" 
              value={address} 
              onChange={e => setAddress(e.target.value)} 
              required 
              style={{ minHeight: '100px', resize: 'vertical' }}
            />
          </div>
          <button type="submit" className="btn btn-primary" disabled={isProcessing} style={{ padding: '1rem', fontSize: '1.125rem', marginTop: '1rem' }}>
            {isProcessing ? 'Processing Order...' : `Pay ₦${cartTotal.toFixed(2)} with Paystack`}
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
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '1.25rem', fontWeight: 700 }}>
            <span>Total</span>
            <span>₦{cartTotal.toFixed(2)}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
