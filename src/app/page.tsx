"use client";

import { useState, useEffect, useRef } from "react";
import Confetti from "react-confetti";

// Generates a list of star objects once
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

// Generates floating particles
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

export default function Home() {
  const [windowDimension, setWindowDimension] = useState({ width: 0, height: 0 });
  const [isClient, setIsClient] = useState(false);
  const stars = useRef(generateStars(80));
  const particles = useRef(generateParticles(25));

  useEffect(() => {
    setIsClient(true);
    setWindowDimension({ width: window.innerWidth, height: window.innerHeight });

    const handleResize = () => {
      setWindowDimension({ width: window.innerWidth, height: window.innerHeight });
    };
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      background: 'url(/dark-space.png) center/cover no-repeat',
      backgroundColor: '#000000',
      fontFamily: 'var(--font-outfit), sans-serif',
      textAlign: 'center',
      padding: '2rem',
      overflow: 'hidden',
      position: 'relative',
      animation: 'bg-zoom 30s ease-in-out infinite alternate'
    }}>

      {/* Marquee at top */}
      <div className="marquee-container">
        <div className="marquee-content">
          <span style={{ paddingRight: '2rem' }}>STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • </span>
          <span style={{ paddingRight: '2rem' }}>STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • STARR IS COMING • </span>
        </div>
      </div>

      {/* Confetti */}
      {isClient && (
        <Confetti
          width={windowDimension.width}
          height={windowDimension.height}
          colors={['#ffffff', '#facc15', '#dc2626']}
          recycle={true}
          numberOfPieces={100}
          gravity={0.03}
        />
      )}

      {/* Twinkling stars layer */}
      {isClient && stars.current.map(star => (
        <div
          key={star.id}
          className="twinkle-star"
          style={{
            top: star.top,
            left: star.left,
            width: `${star.size}px`,
            height: `${star.size}px`,
            animationDelay: star.delay,
            animationDuration: star.duration,
          }}
        />
      ))}

      {/* Floating ember particles */}
      {isClient && particles.current.map(p => (
        <div
          key={p.id}
          className="float-particle"
          style={{
            left: p.left,
            width: `${p.size}px`,
            height: `${p.size}px`,
            opacity: p.opacity,
            animationDelay: p.delay,
            animationDuration: p.duration,
          }}
        />
      ))}

      {/* Logo */}
      <img
        src="/store-closed-bg-transparent.png"
        alt="Starr Premium"
        className="animate-glow"
        style={{
          maxWidth: '500px',
          width: '100%',
          marginBottom: '3rem',
          position: 'relative',
          zIndex: 10
        }}
      />

      {/* Store is closed */}
      <h1
        className="animate-fade-up delay-1"
        style={{
          fontSize: 'clamp(2.5rem, 8vw, 6rem)',
          fontWeight: 900,
          letterSpacing: '-0.04em',
          lineHeight: 1,
          marginBottom: '1rem',
          textTransform: 'uppercase',
          color: '#dc2626',
          position: 'relative',
          zIndex: 10,
          textShadow: '0 0 40px rgba(220, 38, 38, 0.6)',
        }}
      >
        Store is closed.
      </h1>

      {/* Coming soon */}
      <p
        className="animate-fade-up delay-2"
        style={{
          fontSize: 'clamp(1rem, 2vw, 1.5rem)',
          letterSpacing: '0.3em',
          textTransform: 'uppercase',
          fontWeight: 700,
          color: '#dc2626',
          position: 'relative',
          zIndex: 10,
        }}
      >
        Coming soon
      </p>
    </div>
  );
}
