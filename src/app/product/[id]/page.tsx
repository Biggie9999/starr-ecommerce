import prisma from "@/lib/prisma";
import { notFound } from "next/navigation";
import ProductDetailsClient from "@/components/ProductDetailsClient";

export default async function ProductPage({ params }: { params: { id: string } }) {
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
