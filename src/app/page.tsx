import prisma from "@/lib/prisma";
import ProductCard from "@/components/ProductCard";
import CampaignModal from "@/components/CampaignModal";
import ShopAllButton from "@/components/ShopAllButton";

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

  const categories = ["All", "Jeans", "Jorts", "Hoodies", "Tees", "Jewelries"];

  return (
    <div style={{ 
      '--background': 'transparent', 
      '--foreground': '#ffffff',
      '--text': '#ffffff',
      '--text-muted': 'rgba(255,255,255,0.7)',
      '--surface': 'rgba(255,255,255,0.05)',
      '--border': 'rgba(255,255,255,0.1)'
    } as React.CSSProperties}>
      
      {/* Fixed Background for entire page */}
      <div style={{
        position: 'fixed',
        inset: 0,
        backgroundImage: 'linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("/hero.jpg")',
        backgroundSize: 'cover',
        backgroundPosition: 'center 20%',
        zIndex: 0,
        pointerEvents: 'none'
      }} />

      <CampaignModal />
      
      {/* Brutalist Editorial Hero Section */}
      <section style={{ 
        height: '100vh', 
        display: 'flex',
        alignItems: 'flex-end',
        position: 'relative'
      }}>
        
        <div className="container" style={{ position: 'relative', zIndex: 1, paddingBottom: '6rem', width: '100%', display: 'flex', justifyContent: 'center' }}>
          <ShopAllButton />
        </div>
      </section>

      {/* Product Grid */}
      <section id="products" className="container" style={{ padding: '3rem 1.5rem', position: 'relative', zIndex: 1 }}>
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
