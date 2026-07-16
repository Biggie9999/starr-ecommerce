import { NextResponse } from "next/server";
import prisma from "@/lib/prisma";
import { Resend } from "resend";

export async function PATCH(req: Request, { params }: { params: Promise<{ id: string }> }) {
  try {
    const { id } = await params;
    const { status } = await req.json();

    const order = await prisma.order.update({
      where: { id },
      data: { status },
      include: {
        items: {
          include: {
            product: { select: { name: true } }
          }
        }
      }
    });

    // Send "Order Shipped" email to customer when admin marks as SHIPPED
    if (status === "SHIPPED" && process.env.RESEND_API_KEY && order.customerEmail) {
      try {
        const resend = new Resend(process.env.RESEND_API_KEY);
        const senderEmail = process.env.SENDER_EMAIL || "onboarding@resend.dev";

        const itemsListHtml = order.items.map((item: any) => `
          <tr>
            <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">
              <strong>${item.product?.name || 'Product'}</strong><br/>
              Size: ${item.size}
            </td>
            <td style="padding: 10px; border-bottom: 1px solid #eaeaea; text-align: center;">${item.quantity}</td>
          </tr>
        `).join('');

        const safeAddress = order.deliveryAddress ? String(order.deliveryAddress).replace(/\n/g, '<br/>') : 'N/A';

        const shippedEmailHtml = `
          <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; color: #000;">
            <h1 style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 20px;">STARR</h1>
            <h2>📦 Your Order Has Been Shipped!</h2>
            <p>Hi ${order.customerName || 'Valued Customer'},</p>
            <p>Great news! Your order has been shipped and is on its way to you.</p>
            
            <div style="background: #f0fdf4; padding: 20px; margin: 20px 0; border-left: 4px solid #22c55e; border-radius: 4px;">
              <h3 style="margin-top: 0; color: #166534;">Shipping Details</h3>
              <p style="margin: 5px 0;"><strong>Order ID:</strong> ${order.id.slice(-6).toUpperCase()}</p>
              <p style="margin: 5px 0;"><strong>Delivering to:</strong><br/>${safeAddress}</p>
            </div>

            <h3>Items in Your Order</h3>
            <table style="width: 100%; border-collapse: collapse;">
              <thead>
                <tr>
                  <th style="text-align: left; padding: 10px; background: #f9f9f9;">Item</th>
                  <th style="text-align: center; padding: 10px; background: #f9f9f9;">Qty</th>
                </tr>
              </thead>
              <tbody>${itemsListHtml}</tbody>
            </table>

            <p style="margin-top: 30px;">Please allow 3-5 business days for delivery. If you have any questions about your shipment, feel free to reach out to us.</p>
            
            <p style="margin-top: 40px; font-size: 12px; color: #666; text-align: center;">
              Thank you for shopping with STARR! ⭐
            </p>
          </div>
        `;

        // Send to customer
        await resend.emails.send({
          from: `Starr Shop <${senderEmail}>`,
          to: order.customerEmail,
          subject: `📦 Your Order Has Been Shipped - STARR #${order.id.slice(-6).toUpperCase()}`,
          html: shippedEmailHtml,
        });

      } catch (emailError) {
        console.error("Failed to send shipped email:", emailError);
        // Don't fail the status update if email fails
      }
    }

    return NextResponse.json({ success: true, order });
  } catch (error) {
    console.error("Order update error:", error);
    return NextResponse.json({ error: "Failed to update order" }, { status: 500 });
  }
}
