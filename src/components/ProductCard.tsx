import Link from "next/link";
import Image from "next/image";

interface ProductCardProps {
  id: string;
  name: string;
  price: number;
  imageUrl: string;
}

export default function ProductCard({ id, name, price, imageUrl }: ProductCardProps) {
  return (
    <div className="glass-card">
      <Link href={`/product/${id}`} style={{ textDecoration: 'none', color: 'inherit' }}>
        <div className="product-image-container">
          <Image 
            src={imageUrl} 
            alt={name} 
            fill
            className="product-image"
          />
        </div>
        <div className="product-info">
          <div>
            <h3 style={{ fontSize: '1.25rem', marginBottom: '0.25rem' }}>{name}</h3>
            <p className="product-price">${price.toFixed(2)}</p>
          </div>
        </div>
        <div className="btn btn-primary" style={{ width: '100%', marginTop: '1rem' }}>View Details</div>
      </Link>
    </div>
  );
}
