import { NextResponse } from "next/server";
import prisma from "@/lib/prisma";

export async function DELETE(request: Request, { params }: { params: { id: string } }) {
  try {
    const { id } = await params;
    
    // Delete relations first
    await prisma.size.deleteMany({ where: { productId: id } });
    await prisma.productImage.deleteMany({ where: { productId: id } });
    
    // Delete product
    await prisma.product.delete({ where: { id } });
    
    return NextResponse.json({ success: true });
  } catch (error) {
    console.error("Delete error:", error);
    return NextResponse.json({ error: "Failed to delete" }, { status: 500 });
  }
}

export async function PUT(request: Request, { params }: { params: { id: string } }) {
  try {
    const { id } = await params;
    const body = await request.json();
    
    // Update basic product fields
    await prisma.product.update({
      where: { id },
      data: {
        name: body.name,
        description: body.description,
        price: parseFloat(body.price),
      }
    });

    // Update sizes
    if (body.sizes && Array.isArray(body.sizes)) {
      await prisma.size.deleteMany({ where: { productId: id } });
      await prisma.product.update({
        where: { id },
        data: {
          sizes: {
            create: body.sizes.map((size: string) => ({ name: size }))
          }
        }
      });
    }

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error("Update error:", error);
    return NextResponse.json({ error: "Failed to update" }, { status: 500 });
  }
}
