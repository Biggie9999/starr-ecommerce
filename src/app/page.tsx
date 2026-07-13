import prisma from "@/lib/prisma";
import ProductCard from "@/components/ProductCard";
import CampaignModal from "@/components/CampaignModal";

export const dynamic = 'force-dynamic';

export default async function Home() {
  // Fetch products from database
  const products = await prisma.product.findMany({
    include: { images: true }
  });

  return (
    <div>
      <CampaignModal />
      
      {/* Brutalist Editorial Hero Section */}
      <section style={{ 
        height: '80vh', 
        display: 'flex',
        alignItems: 'flex-end',
        background: 'url(https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=2000&q=80)',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        position: 'relative'
      }}>
        {/* Dark overlay for contrast */}
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%)' }} />
        
        <div className="container" style={{ position: 'relative', zIndex: 1, paddingBottom: '4rem', width: '100%' }}>
          <h1 style={{ 
            color: 'white', 
            fontSize: 'clamp(3rem, 8vw, 6rem)', 
            lineHeight: 1, 
            marginBottom: '1.5rem',
            maxWidth: '800px',
            letterSpacing: '-0.02em'
          }}>
            The New <br/><span style={{ color: 'var(--primary)' }}>Standard.</span>
          </h1>
          <button className="btn" style={{ backgroundColor: 'white', color: 'black', border: 'none' }}>
            Shop Collection
          </button>
        </div>
      </section>

      {/* Product Grid */}
      <section className="container" style={{ padding: '6rem 1.5rem' }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '3rem', borderBottom: '2px solid var(--foreground)', paddingBottom: '1rem', display: 'inline-block' }}>New Arrivals</h2>
        
        {products.length === 0 ? (
          <div style={{ textAlign: 'center', color: 'var(--text-muted)' }}>
            <p>No products available yet.</p>
            <p style={{ marginTop: '0.5rem', fontSize: '0.875rem' }}>Admin needs to upload some pieces.</p>
          </div>
        ) : (
          <div className="product-grid">
            {products.map((product) => (
              <ProductCard 
                key={product.id}
                id={product.id}
                name={product.name}
                price={product.price}
                imageUrl={product.images[0]?.url || 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=80'}
              />
            ))}
          </div>
        )}
      </section>
    </div>
  );
}
