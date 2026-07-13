"use client";

import { useCart } from "@/context/CartContext";
import Image from "next/image";
import Link from "next/link";

export default function CartDrawer() {
  const { items, isCartOpen, setIsCartOpen, updateQuantity, removeFromCart, cartTotal } = useCart();

  return (
    <>
      {isCartOpen && (
        <div 
          className="modal-overlay" 
          onClick={() => setIsCartOpen(false)}
          style={{ zIndex: 90, animation: 'fadeIn 0.2s' }}
        />
      )}
      <div className={`cart-drawer ${isCartOpen ? 'open' : ''}`}>
        <div className="cart-header">
          <h2>Your Cart ({items.reduce((acc, item) => acc + item.quantity, 0)})</h2>
          <button className="modal-close" style={{ position: 'static' }} onClick={() => setIsCartOpen(false)}>&times;</button>
        </div>
        
        <div className="cart-body">
          {items.length === 0 ? (
            <div style={{ textAlign: 'center', marginTop: '2rem', color: 'var(--text-muted)' }}>
              Your cart is empty.
            </div>
          ) : (
            items.map((item) => (
              <div key={item.id} className="cart-item">
                <div style={{ position: 'relative', width: '80px', height: '80px', flexShrink: 0 }}>
                  <Image src={item.imageUrl} alt={item.name} fill className="cart-item-image" />
                </div>
                <div style={{ flex: 1 }}>
                  <h4 style={{ marginBottom: '0.25rem' }}>{item.name}</h4>
                  <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem', marginBottom: '0.5rem' }}>Size: {item.size}</p>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                      <button className="size-btn" style={{ width: '24px', height: '24px' }} onClick={() => updateQuantity(item.id, item.quantity - 1)}>-</button>
                      <span>{item.quantity}</span>
                      <button className="size-btn" style={{ width: '24px', height: '24px' }} onClick={() => updateQuantity(item.id, item.quantity + 1)}>+</button>
                    </div>
                    <span style={{ fontWeight: 600 }}>${(item.price * item.quantity).toFixed(2)}</span>
                  </div>
                </div>
                <button 
                  onClick={() => removeFromCart(item.id)}
                  style={{ background: 'none', border: 'none', color: 'var(--danger)', cursor: 'pointer', height: 'fit-content' }}
                >
                  &times;
                </button>
              </div>
            ))
          )}
        </div>

        {items.length > 0 && (
          <div className="cart-footer">
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem', fontSize: '1.25rem', fontWeight: 600 }}>
              <span>Total</span>
              <span>${cartTotal.toFixed(2)}</span>
            </div>
            <Link href="/checkout" style={{ textDecoration: 'none' }}>
              <button className="btn btn-primary" style={{ width: '100%' }} onClick={() => setIsCartOpen(false)}>
                Proceed to Checkout
              </button>
            </Link>
          </div>
        )}
      </div>
    </>
  );
}
