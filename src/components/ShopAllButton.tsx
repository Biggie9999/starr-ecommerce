"use client";
import { useState, useEffect } from 'react';

export default function ShopAllButton() {
  const [locked, setLocked] = useState(true);

  useEffect(() => {
    if (locked) {
      document.body.style.overflow = 'hidden';
      document.body.style.position = 'fixed';
      document.body.style.width = '100%';
      document.body.style.height = '100%';
      document.documentElement.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
      document.body.style.position = '';
      document.body.style.width = '';
      document.body.style.height = '';
      document.documentElement.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
      document.body.style.position = '';
      document.body.style.width = '';
      document.body.style.height = '';
      document.documentElement.style.overflow = '';
    };
  }, [locked]);

  const handleClick = (e: React.MouseEvent) => {
    e.preventDefault();
    setLocked(false);
    
    // Give it a tiny delay for the overflow:unset to apply, then scroll
    setTimeout(() => {
      const productsSection = document.getElementById('products');
      if (productsSection) {
        productsSection.scrollIntoView({ behavior: 'smooth' });
      }
    }, 50);
  };

  return (
    <a 
      href="#products" 
      onClick={handleClick}
      className="btn" 
      style={{ 
        backgroundColor: 'transparent', 
        color: 'white', 
        border: '1px solid white', 
        textDecoration: 'none', 
        fontSize: '0.875rem', 
        letterSpacing: '0.1em',
        padding: '1rem 3rem', 
        textTransform: 'uppercase',
        cursor: 'pointer'
      }}
    >
      SHOP ALL
    </a>
  );
}
