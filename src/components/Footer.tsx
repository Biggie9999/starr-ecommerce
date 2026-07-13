import Link from "next/link";
import { Facebook, Instagram, Twitter } from "lucide-react";

export default function Footer() {
  return (
    <footer style={{ 
      backgroundColor: '#111827', 
      color: '#f9fafb', 
      padding: '4rem 1.5rem 2rem 1.5rem',
      marginTop: 'auto'
    }}>
      <div className="container" style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
        gap: '3rem',
        marginBottom: '3rem'
      }}>
        <div>
          <h3 style={{ fontSize: '1.5rem', marginBottom: '1rem', fontWeight: 800 }}>STARR.</h3>
          <p style={{ color: '#9ca3af', lineHeight: 1.6, marginBottom: '1.5rem' }}>
            Premium streetwear designed to elevate your everyday essentials. Crafted with precision.
          </p>
          <div style={{ display: 'flex', gap: '1rem' }}>
            <Link href="#" style={{ color: '#f9fafb' }}><Instagram size={24} /></Link>
            <Link href="#" style={{ color: '#f9fafb' }}><Twitter size={24} /></Link>
            <Link href="#" style={{ color: '#f9fafb' }}><Facebook size={24} /></Link>
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
          <h4 style={{ marginBottom: '1.5rem', fontWeight: 600 }}>Support</h4>
          <ul style={{ listStyle: 'none', padding: 0, display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            <li><Link href="#" style={{ color: '#9ca3af', textDecoration: 'none' }}>FAQ</Link></li>
            <li><Link href="#" style={{ color: '#9ca3af', textDecoration: 'none' }}>Shipping & Returns</Link></li>
            <li><Link href="#" style={{ color: '#9ca3af', textDecoration: 'none' }}>Contact Us</Link></li>
          </ul>
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
        <div style={{ display: 'flex', gap: '1.5rem' }}>
          <Link href="#" style={{ color: '#9ca3af', textDecoration: 'none' }}>Privacy Policy</Link>
          <Link href="#" style={{ color: '#9ca3af', textDecoration: 'none' }}>Terms of Service</Link>
        </div>
      </div>
    </footer>
  );
}
