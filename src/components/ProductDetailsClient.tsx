"use client";

import { useState } from "react";
import { useCart } from "@/context/CartContext";
import ImageSlider from "@/components/ImageSlider";

interface ProductDetailsProps {
  product: {
    id: string;
    name: string;
    description: string;
    price: number;
    images: { url: string }[];
    sizes: { name: string }[];
  };
}

export default function ProductDetailsClient({ product }: ProductDetailsProps) {
  const { addToCart } = useCart();
  const [selectedSize, setSelectedSize] = useState<string>(product.sizes[0]?.name || "");

  const handleAddToCart = () => {
    if (!selectedSize) {
      alert("Please select a size");
      return;
    }
    
    addToCart({
      productId: product.id,
      name: product.name,
      price: product.price,
      quantity: 1,
      size: selectedSize,
      imageUrl: product.images[0]?.url || 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=80'
    });
  };

  const images = product.images.map(img => img.url).length > 0 
    ? product.images.map(img => img.url) 
    : ['https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=80', 'https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=800&q=80'];

  return (
    <div className="container" style={{ padding: '4rem 1.5rem', display: 'flex', gap: '4rem', flexWrap: 'wrap' }}>
      <div style={{ flex: '1 1 400px', maxWidth: '600px' }}>
        <ImageSlider images={images} />
      </div>
      
      <div style={{ flex: '1 1 300px', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
        <div>
          <h1 style={{ marginBottom: '0.5rem' }}>{product.name}</h1>
          <p className="product-price" style={{ fontSize: '1.5rem' }}>₦{product.price.toFixed(2)}</p>
        </div>
        
        <div>
          <p style={{ color: 'var(--text-muted)', lineHeight: '1.6' }}>{product.description}</p>
        </div>
        
        <div>
          <h4 style={{ marginBottom: '0.5rem' }}>Select Size</h4>
          <div className="size-selector">
            {product.sizes.length > 0 ? product.sizes.map((size) => (
              <button
                key={size.name}
                className={`size-btn ${selectedSize === size.name ? 'active' : ''}`}
                onClick={() => setSelectedSize(size.name)}
              >
                {size.name}
              </button>
            )) : (
              <div style={{ color: 'var(--text-muted)' }}>No sizes available</div>
            )}
          </div>
        </div>
        
        <button 
          className="btn btn-primary" 
          style={{ padding: '1rem', fontSize: '1.125rem', marginTop: '1rem' }}
          onClick={handleAddToCart}
          disabled={!selectedSize}
        >
          Add to Cart
        </button>
      </div>
    </div>
  );
}
