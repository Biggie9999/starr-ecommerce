"use client";

import { useState } from "react";
import { useCart } from "@/context/CartContext";
import { usePaystackPayment } from "react-paystack";
import { useRouter } from "next/navigation";

export default function CheckoutClient() {
  const { items, cartTotal, clearCart } = useCart();
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const router = useRouter();

  const config = {
    reference: (new Date()).getTime().toString(),
    email: email,
    amount: cartTotal * 100, // Paystack amount is in kobo (base currency * 100)
    publicKey: process.env.NEXT_PUBLIC_PAYSTACK_PUBLIC_KEY || "pk_test_2c11dd140d238739f2fdff54c5d2b80aec8b9e51",
  };

  const initializePayment = usePaystackPayment(config);

  const onSuccess = (reference: any) => {
    // Implementation for whatever you want to do with reference and after success call.
    alert("Payment successful! Reference: " + reference.reference);
    clearCart();
    router.push("/");
  };

  const onClose = () => {
    // implementation for whatever you want to do when the Paystack dialog closed.
    console.log("Payment modal closed");
  };

  const handleCheckout = (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !name) return;
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
          <button type="submit" className="btn btn-primary" style={{ padding: '1rem', fontSize: '1.125rem', marginTop: '1rem' }}>
            Pay ₦{cartTotal.toFixed(2)} with Paystack
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
