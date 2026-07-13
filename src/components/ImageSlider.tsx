"use client";

import { useState } from "react";
import Image from "next/image";

export default function ImageSlider({ images }: { images: string[] }) {
  const [currentIndex, setCurrentIndex] = useState(0);

  const next = () => setCurrentIndex((prev) => (prev + 1) % images.length);
  const prev = () => setCurrentIndex((prev) => (prev - 1 + images.length) % images.length);

  if (!images || images.length === 0) return null;

  return (
    <div className="slider-container">
      <div 
        className="slider-track" 
        style={{ transform: `translateX(-${currentIndex * 100}%)` }}
      >
        {images.map((src, idx) => (
          <div key={idx} className="slider-slide" style={{ position: 'relative' }}>
            <Image 
              src={src} 
              alt={`Product image ${idx + 1}`} 
              fill
              style={{ objectFit: 'cover' }}
              priority={idx === 0}
            />
          </div>
        ))}
      </div>
      
      {images.length > 1 && (
        <>
          <button className="slider-btn prev" onClick={prev}>&#10094;</button>
          <button className="slider-btn next" onClick={next}>&#10095;</button>
        </>
      )}
      
      {images.length > 1 && (
        <div style={{ position: 'absolute', bottom: '1rem', left: '0', right: '0', display: 'flex', justifyContent: 'center', gap: '0.5rem' }}>
          {images.map((_, idx) => (
            <button
              key={idx}
              onClick={() => setCurrentIndex(idx)}
              style={{
                width: '8px',
                height: '8px',
                borderRadius: '50%',
                background: currentIndex === idx ? 'white' : 'rgba(255, 255, 255, 0.5)',
                border: 'none',
                cursor: 'pointer'
              }}
            />
          ))}
        </div>
      )}
    </div>
  );
}
