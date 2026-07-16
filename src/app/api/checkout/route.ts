import { NextResponse } from "next/server";
import prisma from "@/lib/prisma";
import { Resend } from "resend";

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const { reference, name, email, phone, address, items, total } = body;

    if (!email || !items || items.length === 0) {
      return NextResponse.json({ error: "Invalid order data" }, { status: 400 });
    }

    // Verify all products still exist in the database
    const productIds = items.map((item: any) => item.id);
    const uniqueProductIds = Array.from(new Set(productIds)) as string[];
    
    const existingProducts = await prisma.product.findMany({
      where: { id: { in: uniqueProductIds } },
      select: { id: true }
    });

    if (existingProducts.length !== uniqueProductIds.length) {
      const foundIds = existingProducts.map(p => p.id);
      const missingIds = uniqueProductIds.filter(id => !foundIds.includes(id));
      return NextResponse.json({ 
        error: "Checkout failed", 
        details: `The following product IDs are in your cart but missing from the database: ${missingIds.join(", ")}. Please completely empty your cart and try again.` 
      }, { status: 400 });
    }

    // Create the order in the database
    const order = await prisma.order.create({
      data: {
        customerEmail: email,
        customerName: name,
        phoneNumber: phone,
        deliveryAddress: address,
        totalAmount: total,
        status: "PAID",
        paystackReference: reference,
        items: {
          create: items.map((item: any) => ({
            productId: item.id,
            quantity: item.quantity,
            size: item.size,
            price: item.price
          }))
        }
      },
      include: {
        items: {
          include: {
            product: { select: { name: true } }
          }
        }
      }
    });

    // Send emails
    if (process.env.RESEND_API_KEY) {
      try {
        const resend = new Resend(process.env.RESEND_API_KEY);
        const senderEmail = process.env.SENDER_EMAIL || "onboarding@resend.dev";
        const adminEmail = "olusojiteniola26@gmail.com";
        
        const itemsListHtml = order.items.map((item: any) => `
          <tr>
            <td style="padding: 10px; border-bottom: 1px solid #eaeaea;">
              <strong>${item.product?.name || 'Product'}</strong><br/>
              Size: ${item.size}
            </td>
            <td style="padding: 10px; border-bottom: 1px solid #eaeaea; text-align: center;">${item.quantity}</td>
            <td style="padding: 10px; border-bottom: 1px solid #eaeaea; text-align: right;">₦${(item.price * item.quantity).toFixed(2)}</td>
          </tr>
        `).join('');

        const safeAddress = address ? String(address).replace(/\n/g, '<br/>') : 'N/A';

        // --- EMAIL 1: Admin Notification ---
        const adminEmailHtml = `
          <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; color: #000;">
            <h1 style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 20px;">STARR - New Order</h1>
            <h2>🛒 New Order Received!</h2>
            <p>A customer just placed an order on your store.</p>
            
            <div style="background: #f9f9f9; padding: 20px; margin: 20px 0; border-left: 4px solid #000;">
              <h3 style="margin-top: 0;">Customer Details</h3>
              <p style="margin: 5px 0;"><strong>Name:</strong> ${name}</p>
              <p style="margin: 5px 0;"><strong>Email:</strong> ${email}</p>
              <p style="margin: 5px 0;"><strong>Phone:</strong> ${phone || 'N/A'}</p>
              <p style="margin: 5px 0;"><strong>Address:</strong><br/>${safeAddress}</p>
            </div>

            <h3>Order Items</h3>
            <table style="width: 100%; border-collapse: collapse;">
              <thead>
                <tr>
                  <th style="text-align: left; padding: 10px; background: #f9f9f9;">Item</th>
                  <th style="text-align: center; padding: 10px; background: #f9f9f9;">Qty</th>
                  <th style="text-align: right; padding: 10px; background: #f9f9f9;">Price</th>
                </tr>
              </thead>
              <tbody>${itemsListHtml}</tbody>
              <tfoot>
                <tr>
                  <td colspan="2" style="text-align: right; padding: 15px 10px; font-weight: bold;">Total Paid</td>
                  <td style="text-align: right; padding: 15px 10px; font-weight: bold;">₦${total.toFixed(2)}</td>
                </tr>
              </tfoot>
            </table>
            <p style="margin-top: 20px; font-size: 12px; color: #666;">Order ID: ${order.id}</p>
          </div>
        `;

        await resend.emails.send({
          from: `Starr Shop <${senderEmail}>`,
          to: adminEmail,
          subject: `🛒 New Order Received - STARR #${order.id.slice(-6).toUpperCase()}`,
          html: adminEmailHtml,
        });

        // --- EMAIL 2: Customer Confirmation ---
        const customerEmailHtml = `
          <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; color: #000;">
            <h1 style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 20px;">STARR</h1>
            <h2>Order Confirmed ✓</h2>
            <p>Hi ${name},</p>
            <p>Thank you for your order! We've received your payment and are getting your items ready for shipment.</p>
            
            <h3 style="margin-top: 30px;">Order Details</h3>
            <p><strong>Order ID:</strong> ${order.id.slice(-6).toUpperCase()}</p>
            
            <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
              <thead>
                <tr>
                  <th style="text-align: left; padding: 10px; background: #f9f9f9;">Item</th>
                  <th style="text-align: center; padding: 10px; background: #f9f9f9;">Qty</th>
                  <th style="text-align: right; padding: 10px; background: #f9f9f9;">Price</th>
                </tr>
              </thead>
              <tbody>${itemsListHtml}</tbody>
              <tfoot>
                <tr>
                  <td colspan="2" style="text-align: right; padding: 15px 10px; font-weight: bold;">Total Paid</td>
                  <td style="text-align: right; padding: 15px 10px; font-weight: bold;">₦${total.toFixed(2)}</td>
                </tr>
              </tfoot>
            </table>

            <div style="background: #f9f9f9; padding: 20px; margin-top: 30px; border-radius: 4px;">
              <h3 style="margin-top: 0;">Delivery Information</h3>
              <p style="margin: 5px 0;"><strong>Name:</strong> ${name}</p>
              <p style="margin: 5px 0;"><strong>Phone:</strong> ${phone || 'N/A'}</p>
              <p style="margin: 5px 0;"><strong>Address:</strong><br/>${safeAddress}</p>
            </div>
            
            <p style="margin-top: 30px;">We'll send you another email once your order has been shipped. 📦</p>
            <p style="margin-top: 40px; font-size: 12px; color: #666; text-align: center;">
              If you have any questions, reply to this email or contact our support.
            </p>
          </div>
        `;

        await resend.emails.send({
          from: `Starr Shop <${senderEmail}>`,
          to: email,
          subject: `Order Confirmed - STARR #${order.id.slice(-6).toUpperCase()}`,
          html: customerEmailHtml,
        });

      } catch (emailError: any) {
        console.error("Email sending error:", emailError);
        // Don't fail the checkout if email fails
      }
    }

    return NextResponse.json({ success: true, orderId: order.id });
  } catch (error: any) {
    console.error("Checkout error:", error);
    return NextResponse.json({ error: "Checkout failed", details: error?.message || String(error) }, { status: 500 });
  }
}
