"use client";

import { useState } from "react";
import Image from "next/image";
import { useCart } from "@/context/CartContext";
import { useToast } from "@/context/ToastContext";
import { ChevronDown, ShieldCheck, Truck } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export default function ProductDetailsClient({ product }: { product: any }) {
  const [selectedSize, setSelectedSize] = useState("");
  const [quantity, setQuantity] = useState(1);
  const { addToCart } = useCart();
  const { addToast } = useToast();
  const [activeAccordion, setActiveAccordion] = useState<string | null>(null);

  const handleAddToCart = () => {
    if (!selectedSize) {
      alert("Please select a size");
      return;
    }
    
    addToCart({
      productId: product.id,
      name: product.name,
      price: product.price,
      quantity,
      size: selectedSize,
      imageUrl: product.images[0]?.url || ""
    });

    addToast(`Added ${product.name} to cart.`);
  };

  const toggleAccordion = (id: string) => {
    setActiveAccordion(activeAccordion === id ? null : id);
  };

  return (
    <div className="container" style={{ padding: '4rem 1.5rem' }}>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '4rem' }}>
        
        {/* Left Side: Image Gallery */}
        <div style={{ flex: '1 1 500px', position: 'relative' }}>
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            style={{ 
              position: 'sticky', 
              top: '100px',
              backgroundColor: 'var(--surface)',
              borderRadius: '1rem',
              overflow: 'hidden',
              boxShadow: '0 4px 20px rgba(0,0,0,0.05)'
            }}
          >
            <Image 
              src={product.images[0]?.url || 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=80'}
              alt={product.name}
              width={800}
              height={1000}
              style={{ width: '100%', height: 'auto', objectFit: 'cover' }}
              priority
            />
          </motion.div>
        </div>

        {/* Right Side: Product Details */}
        <div style={{ flex: '1 1 400px', paddingTop: '2rem' }}>
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            <h1 style={{ fontSize: '2.5rem', fontWeight: 800, marginBottom: '0.5rem' }}>{product.name}</h1>
            <p style={{ fontSize: '1.5rem', color: 'var(--primary)', fontWeight: 600, marginBottom: '2rem' }}>
              ₦{product.price.toFixed(2)}
            </p>

            <p style={{ color: 'var(--text-muted)', lineHeight: 1.6, marginBottom: '3rem', fontSize: '1.125rem' }}>
              {product.description}
            </p>

            {/* Size Selector */}
            <div style={{ marginBottom: '3rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
                <span style={{ fontWeight: 600 }}>Select Size</span>
                <span style={{ color: 'var(--text-muted)', textDecoration: 'underline', cursor: 'pointer', fontSize: '0.875rem' }}>Size Guide</span>
              </div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.75rem' }}>
                {product.sizes.map((size: any) => (
                  <button
                    key={size.id}
                    onClick={() => setSelectedSize(size.name)}
                    style={{
                      width: '60px',
                      height: '60px',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      border: selectedSize === size.name ? '2px solid var(--primary)' : '1px solid var(--border)',
                      backgroundColor: selectedSize === size.name ? 'var(--primary)' : 'transparent',
                      color: selectedSize === size.name ? '#fff' : 'var(--text)',
                      borderRadius: '0.5rem',
                      fontWeight: 600,
                      cursor: 'pointer',
                      transition: 'all 0.2s ease'
                    }}
                  >
                    {size.name}
                  </button>
                ))}
              </div>
            </div>

            <button 
              className="btn btn-primary" 
              style={{ width: '100%', padding: '1.25rem', fontSize: '1.125rem', marginBottom: '2rem' }}
              onClick={handleAddToCart}
            >
              {selectedSize ? "Add to Cart" : "Select a Size"}
            </button>

            {/* Trust Badges */}
            <div style={{ display: 'flex', gap: '2rem', marginBottom: '3rem', padding: '1.5rem', backgroundColor: 'var(--surface)', borderRadius: '0.5rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', color: 'var(--text-muted)', fontSize: '0.875rem' }}>
                <Truck size={20} />
                <span>Fast & Reliable Shipping</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', color: 'var(--text-muted)', fontSize: '0.875rem' }}>
                <ShieldCheck size={20} />
                <span>Secure Checkout</span>
              </div>
            </div>

            {/* Accordions */}
            <div style={{ borderTop: '1px solid var(--border)' }}>
              <div 
                style={{ padding: '1.5rem 0', display: 'flex', justifyContent: 'space-between', cursor: 'pointer', borderBottom: '1px solid var(--border)' }}
                onClick={() => toggleAccordion('details')}
              >
                <span style={{ fontWeight: 600 }}>Product Details & Care</span>
                <ChevronDown style={{ transform: activeAccordion === 'details' ? 'rotate(180deg)' : 'rotate(0)', transition: 'transform 0.3s' }} />
              </div>
              <AnimatePresence>
                {activeAccordion === 'details' && (
                  <motion.div 
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    style={{ overflow: 'hidden' }}
                  >
                    <p style={{ padding: '0 0 1.5rem 0', color: 'var(--text-muted)', lineHeight: 1.6, fontSize: '0.875rem' }}>
                      Designed with a modern oversized fit. Made from heavyweight 100% premium cotton. Machine wash cold, hang dry to preserve the fit and print quality.
                    </p>
                  </motion.div>
                )}
              </AnimatePresence>

              <div 
                style={{ padding: '1.5rem 0', display: 'flex', justifyContent: 'space-between', cursor: 'pointer', borderBottom: '1px solid var(--border)' }}
                onClick={() => toggleAccordion('shipping')}
              >
                <span style={{ fontWeight: 600 }}>Shipping & Returns</span>
                <ChevronDown style={{ transform: activeAccordion === 'shipping' ? 'rotate(180deg)' : 'rotate(0)', transition: 'transform 0.3s' }} />
              </div>
              <AnimatePresence>
                {activeAccordion === 'shipping' && (
                  <motion.div 
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    style={{ overflow: 'hidden' }}
                  >
                    <p style={{ padding: '0 0 1.5rem 0', color: 'var(--text-muted)', lineHeight: 1.6, fontSize: '0.875rem' }}>
                      Orders are processed within 24-48 hours. Domestic delivery takes 3-5 business days. We offer a 14-day return policy for unwashed and unworn items with original tags.
                    </p>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>

          </motion.div>
        </div>
      </div>
    </div>
  );
}
