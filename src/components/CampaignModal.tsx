"use client";

import { useState, useEffect } from "react";

export default function CampaignModal() {
  const [isOpen, setIsOpen] = useState(false);
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState<"idle" | "loading" | "success">("idle");

  useEffect(() => {
    // Show modal after 3 seconds on first visit
    const timer = setTimeout(() => {
      const hasSeenModal = localStorage.getItem("hasSeenCampaignModal");
      if (!hasSeenModal) {
        setIsOpen(true);
      }
    }, 3000);
    return () => clearTimeout(timer);
  }, []);

  const closeModal = () => {
    setIsOpen(false);
    localStorage.setItem("hasSeenCampaignModal", "true");
  };

  const subscribe = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email) return;
    
    setStatus("loading");
    try {
      const res = await fetch('/api/subscribers', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email })
      });
      
      if (!res.ok) throw new Error("Subscription failed");
      
      setStatus("success");
      setTimeout(() => {
        closeModal();
      }, 2000);
    } catch (error) {
      console.error(error);
      setStatus("idle");
    }
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={closeModal}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="modal-close" onClick={closeModal}>&times;</button>
        <h2 style={{ marginBottom: '1rem', textAlign: 'center' }}>Join the Club</h2>
        <p style={{ color: 'var(--text-muted)', marginBottom: '1.5rem', textAlign: 'center' }}>
          Subscribe to get exclusive access to new drops and 10% off your first order.
        </p>
        
        {status === "success" ? (
          <div style={{ textAlign: 'center', color: 'var(--success)', padding: '1rem 0' }}>
            Thanks for subscribing! Check your email.
          </div>
        ) : (
          <form onSubmit={subscribe} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <input 
              type="email" 
              className="input-field" 
              placeholder="Enter your email address" 
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <button type="submit" className="btn btn-primary" disabled={status === "loading"}>
              {status === "loading" ? "Subscribing..." : "Subscribe"}
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
