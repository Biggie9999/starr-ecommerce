"use client";

import Link from "next/link";
import Image from "next/image";
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

const TikTokIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
    <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.5 2.89 2.89 0 0 1-2.89-2.89 2.89 2.89 0 0 1 2.89-2.89c.28 0 .54.04.79.1V9.01a6.33 6.33 0 0 0-.79-.05 6.34 6.34 0 0 0-6.34 6.34 6.34 6.34 0 0 0 6.34 6.34 6.34 6.34 0 0 0 6.33-6.34V8.69a8.18 8.18 0 0 0 4.78 1.52V6.76a4.85 4.85 0 0 1-1.01-.07z"/>
  </svg>
);

export default function Footer() {
  const { addToast } = useToast();

  return (
    <footer style={{ 
      backgroundColor: '#000000', 
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
          <div style={{ marginBottom: '1.5rem', display: 'flex', alignItems: 'center' }}>
            <Image src="/logo.png" alt="Starr Logo" width={60} height={60} style={{ objectFit: 'contain' }} />
          </div>
          <p style={{ color: '#9ca3af', lineHeight: 1.6, marginBottom: '1.5rem' }}>
            Premium streetwear designed to elevate your everyday essentials. Crafted with precision.
          </p>
          <div style={{ display: 'flex', gap: '1rem' }}>
            <Link href="https://www.instagram.com/tenisastar?igsh=MXJsdGJ4aWp2cWF1aw%3D%3D&utm_source=qr" target="_blank" rel="noopener noreferrer" style={{ color: '#f9fafb' }}><InstagramIcon /></Link>
            <Link href="https://x.com/tenisastar?s=11" target="_blank" rel="noopener noreferrer" style={{ color: '#f9fafb' }}><TwitterIcon /></Link>
            <Link href="https://www.tiktok.com/@tenisastar?_r=1&_t=ZS-98NsLys0PVE" target="_blank" rel="noopener noreferrer" style={{ color: '#f9fafb' }}><TikTokIcon /></Link>
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
