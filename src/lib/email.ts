import { Resend } from "resend";

export async function sendOrderEmails(order: any, calculatedTotal: number, calculatedDeliveryFee: number, state: string) {
  if (!process.env.RESEND_API_KEY) {
    console.log("No RESEND_API_KEY, skipping emails.");
    return;
  }
  
  try {
    const resend = new Resend(process.env.RESEND_API_KEY);
    const senderEmail = process.env.SENDER_EMAIL || "orders@star01.xyz";
    const adminEmail = "olusojiteniola26@gmail.com";
    
    const itemsSubtotal = calculatedTotal - calculatedDeliveryFee;

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

    const safeAddress = order.deliveryAddress ? String(order.deliveryAddress).replace(/\n/g, '<br/>') : 'N/A';

    // --- EMAIL 1: Admin Notification ---
    const adminEmailHtml = `
      <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; color: #000;">
        <h1 style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 20px;">STARR - New Order</h1>
        <h2>🛒 New Order Received!</h2>
        <p>A customer just placed an order on your store.</p>
        
        <div style="background: #f9f9f9; padding: 20px; margin: 20px 0; border-left: 4px solid #000;">
          <h3 style="margin-top: 0;">Customer Details</h3>
          <p style="margin: 5px 0;"><strong>Name:</strong> ${order.customerName}</p>
          <p style="margin: 5px 0;"><strong>Email:</strong> ${order.customerEmail}</p>
          <p style="margin: 5px 0;"><strong>Phone:</strong> ${order.phoneNumber || 'N/A'}</p>
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
              <td colspan="2" style="text-align: right; padding: 10px; font-weight: 500; color: #666;">Items Subtotal</td>
              <td style="text-align: right; padding: 10px; font-weight: 500; color: #666;">₦${itemsSubtotal.toFixed(2)}</td>
            </tr>
            <tr>
              <td colspan="2" style="text-align: right; padding: 10px; font-weight: 500; color: #666; border-bottom: 1px solid #eaeaea;">Delivery Fee (${state || 'N/A'})</td>
              <td style="text-align: right; padding: 10px; font-weight: 500; color: #666; border-bottom: 1px solid #eaeaea;">₦${calculatedDeliveryFee.toFixed(2)}</td>
            </tr>
            <tr>
              <td colspan="2" style="text-align: right; padding: 15px 10px; font-weight: bold;">Total Paid</td>
              <td style="text-align: right; padding: 15px 10px; font-weight: bold;">₦${calculatedTotal.toFixed(2)}</td>
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
        <p>Hi ${order.customerName},</p>
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
              <td colspan="2" style="text-align: right; padding: 10px; font-weight: 500; color: #666;">Items Subtotal</td>
              <td style="text-align: right; padding: 10px; font-weight: 500; color: #666;">₦${itemsSubtotal.toFixed(2)}</td>
            </tr>
            <tr>
              <td colspan="2" style="text-align: right; padding: 10px; font-weight: 500; color: #666; border-bottom: 1px solid #eaeaea;">Delivery Fee (${state || 'N/A'})</td>
              <td style="text-align: right; padding: 10px; font-weight: 500; color: #666; border-bottom: 1px solid #eaeaea;">₦${calculatedDeliveryFee.toFixed(2)}</td>
            </tr>
            <tr>
              <td colspan="2" style="text-align: right; padding: 15px 10px; font-weight: bold;">Total Paid</td>
              <td style="text-align: right; padding: 15px 10px; font-weight: bold;">₦${calculatedTotal.toFixed(2)}</td>
            </tr>
          </tfoot>
        </table>

        <div style="background: #f9f9f9; padding: 20px; margin-top: 30px; border-radius: 4px;">
          <h3 style="margin-top: 0;">Delivery Information</h3>
          <p style="margin: 5px 0;"><strong>Name:</strong> ${order.customerName}</p>
          <p style="margin: 5px 0;"><strong>Phone:</strong> ${order.phoneNumber || 'N/A'}</p>
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
      to: order.customerEmail,
      subject: `Order Confirmed - STARR #${order.id.slice(-6).toUpperCase()}`,
      html: customerEmailHtml,
    });

  } catch (emailError: any) {
    console.error("Email sending error:", emailError);
  }
}
