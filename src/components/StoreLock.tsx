"use client";

import { useState, useEffect, useRef } from "react";
import { usePathname } from "next/navigation";

// The launch date
const LAUNCH_DATE = new Date("2026-08-10T00:00:00");
const TYPING_TEXT = "Store is closed.";

function generateStars(count: number) {
  return Array.from({ length: count }, (_, i) => ({
    id: i,
    top: `${Math.random() * 100}%`,
    left: `${Math.random() * 100}%`,
    size: Math.random() * 2.5 + 0.5,
    delay: `${Math.random() * 5}s`,
    duration: `${Math.random() * 3 + 2}s`,
  }));
}

function generateParticles(count: number) {
  return Array.from({ length: count }, (_, i) => ({
    id: i,
    left: `${Math.random() * 100}%`,
    size: Math.random() * 4 + 2,
    delay: `${Math.random() * 8}s`,
    duration: `${Math.random() * 6 + 8}s`,
    opacity: Math.random() * 0.5 + 0.2,
  }));
}

function useCountdown(target: Date) {
  const calc = () => {
    const diff = target.getTime() - Date.now();
    if (diff <= 0) return { days: 0, hours: 0, minutes: 0, seconds: 0, isFinished: true };
    return {
      days: Math.floor(diff / (1000 * 60 * 60 * 24)),
      hours: Math.floor((diff / (1000 * 60 * 60)) % 24),
      minutes: Math.floor((diff / (1000 * 60)) % 60),
      seconds: Math.floor((diff / 1000) % 60),
      isFinished: false
    };
  };
  const [time, setTime] = useState(calc);
  
  useEffect(() => {
    const id = setInterval(() => {
      const newTime = calc();
      setTime(newTime);
      if (newTime.isFinished) {
        clearInterval(id);
      }
    }, 1000);
    return () => clearInterval(id);
  }, []);
  
  return time;
}

function useTypingEffect(text: string, speed = 80) {
  const [displayed, setDisplayed] = useState("");
  useEffect(() => {
    let i = 0;
    setDisplayed("");
    const id = setInterval(() => {
      setDisplayed(text.slice(0, i + 1));
      i++;
      if (i >= text.length) clearInterval(id);
    }, speed);
    return () => clearInterval(id);
  }, [text, speed]);
  return displayed;
}

export default function StoreLock() {
  const pathname = usePathname();
  const [isClient, setIsClient] = useState(false);
  const stars = useRef(generateStars(80));
  const particles = useRef(generateParticles(25));
  const { days, hours, minutes, seconds, isFinished } = useCountdown(LAUNCH_DATE);
  const typedText = useTypingEffect(TYPING_TEXT, 80);

  useEffect(() => { 
    setIsClient(true); 
  }, []);

  // Lock body scroll when overlay is active
  useEffect(() => {
    if (isClient && !isFinished) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [isClient, isFinished]);

  // To prevent hydration mismatch, ensure the first client render matches the server
  if (!isClient) {
    if (pathname && pathname.startsWith('/admin')) return null;
    return <div style={{ position: 'fixed', inset: 0, backgroundColor: '#000000', zIndex: 99999 }} />;
  }

  // If the countdown is finished or we are on the admin page, return null
  if (isFinished || (pathname && pathname.startsWith('/admin'))) {
    return null;
  }

  const pad = (n: number) => String(n).padStart(2, "0");

  return (
    <div style={{
      position: 'fixed',
      inset: 0,
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#000000',
      fontFamily: 'var(--font-outfit), sans-serif',
      textAlign: 'center',
      padding: '2rem',
      overflow: 'hidden',
      zIndex: 99999
    }}>
      {/* Animated galaxy background */}
      <div style={{
        position: 'absolute',
        inset: '-10%',
        backgroundImage: 'url(/dark-space.png)',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        animation: 'galaxy-zoom 20s ease-in-out infinite alternate',
        zIndex: 0
      }} />

      {/* Marquee at top */}
      <div className="marquee-container" style={{ position: 'absolute', top: 0, left: 0, right: 0, zIndex: 10 }}>
        <div className="marquee-content">
          <span style={{ paddingRight: '2rem' }}>STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • </span>
          <span style={{ paddingRight: '2rem' }}>STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • </span>
        </div>
      </div>

      {/* Twinkling stars layer */}
      {stars.current.map(star => (
        <div key={star.id} className="twinkle-star" style={{
          top: star.top, left: star.left,
          width: `${star.size}px`, height: `${star.size}px`,
          animationDelay: star.delay, animationDuration: star.duration,
        }} />
      ))}

      {/* Floating ember particles */}
      {particles.current.map(p => (
        <div key={p.id} className="float-particle" style={{
          left: p.left, width: `${p.size}px`, height: `${p.size}px`,
          opacity: p.opacity, animationDelay: p.delay, animationDuration: p.duration,
        }} />
      ))}

      {/* Logo */}
      <img
        src="/store-closed-bg-transparent.png"
        alt="Starr Premium"
        className="animate-glow"
        style={{ maxWidth: '420px', width: '100%', marginBottom: '2rem', position: 'relative', zIndex: 10 }}
      />

      {/* Typing heading */}
      <h1 style={{
        fontSize: 'clamp(2rem, 6vw, 5rem)',
        fontWeight: 900,
        letterSpacing: '-0.04em',
        lineHeight: 1,
        marginBottom: '2.5rem',
        textTransform: 'uppercase',
        color: '#dc2626',
        position: 'relative',
        zIndex: 10,
        textShadow: '0 0 40px rgba(220, 38, 38, 0.6)',
        minHeight: '1.2em',
      }}>
        {typedText}<span className="cursor-blink">|</span>
      </h1>

      {/* Countdown */}
      <div style={{
        display: 'flex',
        gap: 'clamp(1rem, 4vw, 3rem)',
        position: 'relative',
        zIndex: 10,
        marginBottom: '2rem',
      }}>
        {[
          { label: 'Days', value: days },
          { label: 'Hours', value: hours },
          { label: 'Mins', value: minutes },
          { label: 'Secs', value: seconds },
        ].map(({ label, value }) => (
          <div key={label} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '0.25rem' }}>
            <div style={{
              fontSize: 'clamp(2.5rem, 8vw, 5rem)',
              fontWeight: 900,
              color: '#ffffff',
              lineHeight: 1,
              background: 'rgba(255,255,255,0.05)',
              border: '1px solid rgba(220,38,38,0.4)',
              borderRadius: '0.75rem',
              padding: 'clamp(0.5rem, 2vw, 1rem) clamp(0.75rem, 3vw, 1.5rem)',
              minWidth: 'clamp(60px, 12vw, 110px)',
              textAlign: 'center',
              backdropFilter: 'blur(10px)',
              boxShadow: '0 0 20px rgba(220, 38, 38, 0.15)',
              fontVariantNumeric: 'tabular-nums',
            }}>
              {pad(value)}
            </div>
            <span style={{ fontSize: '0.7rem', letterSpacing: '0.2em', color: '#9ca3af', textTransform: 'uppercase', fontWeight: 600 }}>
              {label}
            </span>
          </div>
        ))}
      </div>

      {/* Coming soon */}
      <p className="animate-fade-up delay-2" style={{
        fontSize: 'clamp(0.875rem, 2vw, 1.25rem)',
        letterSpacing: '0.3em',
        textTransform: 'uppercase',
        fontWeight: 700,
        color: 'rgba(255,255,255,0.5)',
        position: 'relative',
        zIndex: 10,
        marginBottom: '2.5rem',
      }}>
        Launching August 10
      </p>

      {/* Social links */}
      <div style={{ display: 'flex', gap: '1.5rem', position: 'relative', zIndex: 10 }}>
        {[
          { href: "https://www.instagram.com/tenisastar?igsh=MXJsdGJ4aWp2cWF1aw%3D%3D&utm_source=qr", label: "Instagram", icon: <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg> },
          { href: "https://www.tiktok.com/@tenisastar?_r=1&_t=ZS-98NsLys0PVE", label: "TikTok", icon: <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.5 2.89 2.89 0 0 1-2.89-2.89 2.89 2.89 0 0 1 2.89-2.89c.28 0 .54.04.79.1V9.01a6.33 6.33 0 0 0-.79-.05 6.34 6.34 0 0 0-6.34 6.34 6.34 6.34 0 0 0 6.34 6.34 6.34 6.34 0 0 0 6.33-6.34V8.69a8.18 8.18 0 0 0 4.78 1.52V6.76a4.85 4.85 0 0 1-1.01-.07z"/></svg> },
          { href: "https://x.com/tenisastar?s=11", label: "X", icon: <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"/></svg> },
        ].map(({ href, label, icon }) => (
          <a
            key={label}
            href={href}
            target="_blank"
            rel="noopener noreferrer"
            aria-label={label}
            style={{
              color: 'rgba(255,255,255,0.6)',
              transition: 'color 0.2s, transform 0.2s',
              display: 'flex',
              alignItems: 'center',
            }}
            onMouseEnter={e => { (e.currentTarget as HTMLElement).style.color = '#dc2626'; (e.currentTarget as HTMLElement).style.transform = 'scale(1.2)'; }}
            onMouseLeave={e => { (e.currentTarget as HTMLElement).style.color = 'rgba(255,255,255,0.6)'; (e.currentTarget as HTMLElement).style.transform = 'scale(1)'; }}
          >
            {icon}
          </a>
        ))}
      </div>
    </div>
  );
}
