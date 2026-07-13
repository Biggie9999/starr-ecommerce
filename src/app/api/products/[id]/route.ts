import { NextResponse } from "next/server";
import prisma from "@/lib/prisma";

export async function DELETE(request: Request, { params }: { params: Promise<{ id: string }> }) {
  try {
    const { id } = await params;
    
    // Delete product (relations like images and sizes will cascade automatically)
    await prisma.product.delete({ where: { id } });
    
    return NextResponse.json({ success: true });
  } catch (error) {
    console.error("Delete error:", error);
    return NextResponse.json({ error: "Failed to delete" }, { status: 500 });
  }
}

export async function PUT(request: Request, { params }: { params: Promise<{ id: string }> }) {
  try {
    const { id } = await params;
    const { name, description, price, category, sizes } = await request.json();

    // Update basic product fields
    await prisma.product.update({
      where: { id },
      data: {
        name,
        description,
        price: parseFloat(price),
        category,
      }
    });

    // Update sizes
    if (sizes && Array.isArray(sizes)) {
      await prisma.size.deleteMany({ where: { productId: id } });
      await prisma.product.update({
        where: { id },
        data: {
          sizes: {
            create: sizes.map((size: string) => ({ name: size }))
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
