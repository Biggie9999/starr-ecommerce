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
    <div className="product-card">
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
          <h3 className="product-title">{name}</h3>
          <p className="product-price">₦{price.toFixed(2)}</p>
        </div>
      </Link>
    </div>
  );
}
