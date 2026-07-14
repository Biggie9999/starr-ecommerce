import prisma from "@/lib/prisma";
import ProductCard from "@/components/ProductCard";
import CampaignModal from "@/components/CampaignModal";

export const dynamic = 'force-dynamic';

export default async function Home({ searchParams }: { searchParams: Promise<{ category?: string }> }) {
  const params = await searchParams;
  const category = params.category;

  // Fetch products from database
  const products = await prisma.product.findMany({
    where: category ? { category } : undefined,
    include: { images: true },
    orderBy: { createdAt: 'desc' }
  });

  const categories = ["All", "Tees", "Hoodies", "Accessories"];

  return (
    <div>
      <CampaignModal />
      
      {/* Brutalist Editorial Hero Section */}
      <section style={{ 
        height: '80vh', 
        display: 'flex',
        alignItems: 'flex-end',
        background: 'url(/hero.jpg)',
        backgroundSize: 'cover',
        backgroundPosition: 'center 20%',
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
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: '3rem', flexWrap: 'wrap', gap: '1rem' }}>
          <h2 style={{ fontSize: '2.5rem', borderBottom: '2px solid var(--foreground)', paddingBottom: '0.5rem', margin: 0 }}>
            {category ? category : "New Arrivals"}
          </h2>
          
          <div style={{ display: 'flex', gap: '1rem', overflowX: 'auto', paddingBottom: '0.5rem' }}>
            {categories.map((cat) => (
              <a 
                key={cat} 
                href={cat === "All" ? "/" : `/?category=${cat}`}
                style={{
                  fontWeight: 600,
                  textTransform: 'uppercase',
                  fontSize: '0.875rem',
                  color: (category === cat) || (!category && cat === "All") ? 'var(--foreground)' : 'var(--text-muted)',
                  borderBottom: (category === cat) || (!category && cat === "All") ? '2px solid var(--foreground)' : 'none',
                  paddingBottom: '0.25rem',
                  textDecoration: 'none'
                }}
              >
                {cat}
              </a>
            ))}
          </div>
        </div>
        
        {products.length === 0 ? (
          <div style={{ textAlign: 'center', color: 'var(--text-muted)', padding: '4rem 0' }}>
            <p>No products found.</p>
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
