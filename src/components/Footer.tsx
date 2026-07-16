"use client";

import Link from "next/link";
import { useToast } from "@/context/ToastContext";

const InstagramIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/>
  </svg>
);

const TwitterIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"/>
  </svg>
);

const FacebookIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
  </svg>
);

export default function Footer() {
  const { addToast } = useToast();

  return (
    <footer style={{ 
      backgroundColor: '#111827', 
      color: '#f9fafb', 
      padding: '2rem 1.5rem 1.5rem 1.5rem',
      marginTop: 'auto'
    }}>
      <div className="container" style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
        gap: '1.5rem',
        marginBottom: '1.5rem'
      }}>
        <div>
          <h3 style={{ fontSize: '1.5rem', marginBottom: '1rem', fontWeight: 800 }}>STARR.</h3>
          <p style={{ color: '#9ca3af', lineHeight: 1.6, marginBottom: '1.5rem' }}>
            Premium streetwear designed to elevate your everyday essentials. Crafted with precision.
          </p>
          <div style={{ display: 'flex', gap: '1rem' }}>
            <Link href="#" style={{ color: '#f9fafb' }}><InstagramIcon /></Link>
            <Link href="#" style={{ color: '#f9fafb' }}><TwitterIcon /></Link>
            <Link href="#" style={{ color: '#f9fafb' }}><FacebookIcon /></Link>
          </div>
        </div>

        <div>
          <h4 style={{ marginBottom: '1.5rem', fontWeight: 600 }}>Shop</h4>
          <ul style={{ listStyle: 'none', padding: 0, display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            <li><Link href="/" style={{ color: '#9ca3af', textDecoration: 'none' }}>All Products</Link></li>
            <li><Link href="/" style={{ color: '#9ca3af', textDecoration: 'none' }}>New Arrivals</Link></li>
            <li><Link href="/" style={{ color: '#9ca3af', textDecoration: 'none' }}>Best Sellers</Link></li>
          </ul>
        </div>

        <div>
          <h4 style={{ marginBottom: '1.5rem', fontWeight: 600 }}>Newsletter</h4>
          <p style={{ color: '#9ca3af', marginBottom: '1rem', fontSize: '0.875rem' }}>
            Subscribe to get early access to new drops.
          </p>
          <form 
            onSubmit={async (e) => {
              e.preventDefault();
              const form = e.target as HTMLFormElement;
              const email = (form.elements.namedItem('email') as HTMLInputElement).value;
              try {
                await fetch('/api/subscribers', {
                  method: 'POST',
                  body: JSON.stringify({ email })
                });
                addToast("Successfully subscribed to STARR drops!");
                form.reset();
              } catch(e) {}
            }}
            style={{ display: 'flex', gap: '0.5rem' }}
          >
            <input 
              type="email" 
              name="email"
              placeholder="Enter your email" 
              required
              style={{ 
                flex: 1, 
                padding: '0.75rem', 
                backgroundColor: 'transparent', 
                border: '1px solid #374151', 
                color: 'white', 
                outline: 'none',
                fontFamily: 'inherit'
              }} 
            />
            <button 
              type="submit" 
              style={{ 
                padding: '0.75rem 1.25rem', 
                backgroundColor: 'white', 
                color: 'black', 
                border: 'none', 
                fontWeight: 600,
                cursor: 'pointer',
                fontFamily: 'inherit'
              }}
            >
              Join
            </button>
          </form>
        </div>
      </div>

      <div className="container" style={{ 
        borderTop: '1px solid #374151', 
        paddingTop: '2rem',
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'space-between',
        alignItems: 'center',
        gap: '1rem',
        color: '#9ca3af',
        fontSize: '0.875rem'
      }}>
        <p>&copy; {new Date().getFullYear()} Starr Premium. All rights reserved.</p>
        <p style={{ fontWeight: 500, color: '#f9fafb' }}>Contact: textstar01@gmail.com</p>
        <div style={{ display: 'flex', gap: '1.5rem' }}>
          <Link href="#" style={{ color: '#9ca3af', textDecoration: 'none' }}>Privacy Policy</Link>
          <Link href="#" style={{ color: '#9ca3af', textDecoration: 'none' }}>Terms of Service</Link>
        </div>
      </div>
    </footer>
  );
}
