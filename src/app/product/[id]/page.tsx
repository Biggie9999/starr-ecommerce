import prisma from "@/lib/prisma";
import { notFound } from "next/navigation";
import ProductDetailsClient from "@/components/ProductDetailsClient";
import { Metadata } from "next";

export const dynamic = 'force-dynamic';

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const { id } = await params;
  
  const product = await prisma.product.findUnique({
    where: { id },
    include: { images: true }
  });

  if (!product) {
    return {
      title: "Product Not Found | STARR",
      description: "The requested product does not exist."
    };
  }

  const imageUrl = product.images[0]?.url || "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=80";

  return {
    title: `${product.name} | STARR`,
    description: product.description.substring(0, 160) + (product.description.length > 160 ? "..." : ""),
    openGraph: {
      title: `${product.name} | STARR Premium`,
      description: `₦${product.price.toFixed(2)} - ${product.description.substring(0, 100)}`,
      images: [{ url: imageUrl }],
    },
    twitter: {
      card: "summary_large_image",
      title: `${product.name} | STARR Premium`,
      description: `₦${product.price.toFixed(2)} - ${product.description.substring(0, 100)}`,
      images: [imageUrl],
    }
  };
}

export default async function ProductPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  
  const product = await prisma.product.findUnique({
    where: { id },
    include: {
      images: true,
      sizes: true
    }
  });

  if (!product) {
    notFound();
  }

  return <ProductDetailsClient product={product} />;
}
