"use client";

import Link from "next/link";
import { useState } from "react";

export default function Navbar() {
  const [isCartOpen, setIsCartOpen] = useState(false);

  return (
    <>
      <nav className="navbar">
        <div className="container">
          <Link href="/" className="nav-brand">STARR.</Link>
          <div className="nav-links">
            <Link href="/" className="nav-link">Shop</Link>
            <Link href="/admin" className="nav-link">Admin</Link>
            <button 
              className="btn btn-secondary" 
              style={{ position: 'relative', padding: '0.5rem 1rem' }}
              onClick={() => setIsCartOpen(true)}
            >
              Cart
              <span className="cart-badge">2</span>
            </button>
          </div>
        </div>
      </nav>
      {/* We will render CartDrawer here or at layout level later */}
    </>
  );
}
