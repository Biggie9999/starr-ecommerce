"use client";

import { useState, useEffect } from "react";
import Confetti from "react-confetti";

export default function Home() {
  const [windowDimension, setWindowDimension] = useState({ width: 0, height: 0 });
  const [isClient, setIsClient] = useState(false);

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
      background: 'url(/night-sky.png) center/cover no-repeat',
      backgroundColor: '#000000',
      fontFamily: 'var(--font-outfit), sans-serif',
      textAlign: 'center',
      padding: '2rem',
      overflow: 'hidden'
    }}>
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
          zIndex: 10
        }}
      >
        Store is closed.
      </h1>
      
      <p 
        className="animate-fade-up delay-2"
        style={{
          fontSize: 'clamp(1rem, 2vw, 1.5rem)',
          letterSpacing: '0.3em',
          textTransform: 'uppercase',
          fontWeight: 700,
          color: '#dc2626',
          position: 'relative',
          zIndex: 10
        }}
      >
        Coming soon
      </p>
    </div>
  );
}
