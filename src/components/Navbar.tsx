"use client";

import Link from "next/link";
import { useState } from "react";
import { useCart } from "@/context/CartContext";

export default function Navbar() {
  const { items } = useCart();
  const cartCount = items.reduce((total, item) => total + item.quantity, 0);

  return (
    <>
      <nav className="navbar">
        <div className="container">
          <Link href="/" className="nav-brand">STARR.</Link>
          <div className="nav-links">
            <Link href="/" className="nav-link">Shop</Link>

            <Link 
              href="/cart"
              className="btn btn-secondary" 
              style={{ position: 'relative', padding: '0.5rem', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="8" cy="21" r="1"/>
                <circle cx="19" cy="21" r="1"/>
                <path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/>
              </svg>
              {cartCount > 0 && (
                <span style={{
                  position: 'absolute',
                  top: '-8px',
                  right: '-8px',
                  background: 'var(--primary)',
                  color: 'white',
                  borderRadius: '50%',
                  width: '20px',
                  height: '20px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: '0.75rem',
                  fontWeight: 'bold'
                }}>
                  {cartCount}
                </span>
              )}
            </Link>
          </div>
        </div>
      </nav>
      {/* We will render CartDrawer here or at layout level later */}
    </>
  );
}
