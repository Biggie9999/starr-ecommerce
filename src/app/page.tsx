import prisma from "@/lib/prisma";
import ProductCard from "@/components/ProductCard";
import CampaignModal from "@/components/CampaignModal";

export default async function Home() {
  // Fetch products from database
  const products = await prisma.product.findMany({
    include: { images: true }
  });

  return (
    <div>
      <CampaignModal />
      
      {/* Hero Section */}
      <section style={{ 
        height: '60vh', 
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: 'center',
        background: 'linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url(https://images.unsplash.com/photo-1441984904996-e0b6ba687e04?auto=format&fit=crop&w=2000&q=80)',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        textAlign: 'center'
      }}>
        <div style={{ padding: '0 1.5rem' }}>
          <h1 style={{ marginBottom: '1rem', color: 'white' }}>Exclusive Pieces.</h1>
          <p style={{ fontSize: '1.25rem', color: 'rgba(255,255,255,0.8)', marginBottom: '2rem', maxWidth: '600px', margin: '0 auto 2rem auto' }}>
            Discover our latest collection of premium clothing. Crafted with precision and style.
          </p>
          <button className="btn btn-primary" style={{ padding: '1rem 2rem', fontSize: '1.125rem' }}>
            Shop the Collection
          </button>
        </div>
      </section>

      {/* Product Grid */}
      <section className="container" style={{ padding: '4rem 1.5rem' }}>
        <h2 style={{ marginBottom: '2rem', textAlign: 'center' }}>New Arrivals</h2>
        
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
