"use client";

import Link from "next/link";
import { CheckCircle } from "lucide-react";

export default function SuccessPage() {
  return (
    <div className="container" style={{ minHeight: '70vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <div className="glass-card" style={{ maxWidth: '500px', width: '100%', textAlign: 'center', padding: '4rem 2rem' }}>
        <CheckCircle size={64} color="var(--success, #10B981)" style={{ margin: '0 auto 1.5rem auto' }} />
        <h1 style={{ marginBottom: '1rem', fontSize: '2rem' }}>Payment Successful!</h1>
        <p style={{ color: 'var(--text-muted)', marginBottom: '2rem', fontSize: '1.125rem' }}>
          Thank you for your order. Your premium pieces are being prepared for shipping.
        </p>
        <Link href="/">
          <button className="btn btn-primary" style={{ padding: '1rem 2rem', fontSize: '1.125rem' }}>
            Continue Shopping
          </button>
        </Link>
      </div>
    </div>
  );
}
