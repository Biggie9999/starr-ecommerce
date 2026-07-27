"use client";

import { useState, useEffect, useRef } from "react";

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
    if (diff <= 0) return { days: 0, hours: 0, minutes: 0, seconds: 0 };
    return {
      days: Math.floor(diff / (1000 * 60 * 60 * 24)),
      hours: Math.floor((diff / (1000 * 60 * 60)) % 24),
      minutes: Math.floor((diff / (1000 * 60)) % 60),
      seconds: Math.floor((diff / 1000) % 60),
    };
  };
  const [time, setTime] = useState(calc);
  useEffect(() => {
    const id = setInterval(() => setTime(calc()), 1000);
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

export default function Home() {
  const [isClient, setIsClient] = useState(false);
  const stars = useRef(generateStars(80));
  const particles = useRef(generateParticles(25));
  const { days, hours, minutes, seconds } = useCountdown(LAUNCH_DATE);
  const typedText = useTypingEffect(TYPING_TEXT, 80);

  useEffect(() => { setIsClient(true); }, []);

  const pad = (n: number) => String(n).padStart(2, "0");

  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#000000',
      fontFamily: 'var(--font-outfit), sans-serif',
      textAlign: 'center',
      padding: '2rem',
      overflow: 'hidden',
      position: 'relative'
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
      <div className="marquee-container">
        <div className="marquee-content">
          <span style={{ paddingRight: '2rem' }}>STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • </span>
          <span style={{ paddingRight: '2rem' }}>STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • </span>
        </div>
      </div>

      {/* Twinkling stars layer */}
      {isClient && stars.current.map(star => (
        <div key={star.id} className="twinkle-star" style={{
          top: star.top, left: star.left,
          width: `${star.size}px`, height: `${star.size}px`,
          animationDelay: star.delay, animationDuration: star.duration,
        }} />
      ))}

      {/* Floating ember particles */}
      {isClient && particles.current.map(p => (
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
      }}>
        Launching August 10
      </p>
    </div>
  );
}
