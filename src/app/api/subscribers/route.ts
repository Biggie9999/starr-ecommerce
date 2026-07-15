import { NextResponse } from "next/server";
import prisma from "@/lib/prisma";
import { Resend } from "resend";

export async function POST(req: Request) {
  try {
    const { email } = await req.json();

    if (!email || !email.includes("@")) {
      return NextResponse.json({ error: "Invalid email address" }, { status: 400 });
    }

    // Check if already subscribed
    const existing = await prisma.subscriber.findUnique({
      where: { email }
    });

    if (existing) {
      return NextResponse.json({ success: true, message: "Already subscribed!" });
    }

    // Save subscriber
    await prisma.subscriber.create({
      data: { email }
    });

    // Send Welcome Email
    if (process.env.RESEND_API_KEY) {
      try {
        const resend = new Resend(process.env.RESEND_API_KEY);
        
        const emailHtml = `
          <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto; color: #000;">
            <h1 style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 20px;">STARR</h1>
            <h2>Welcome to the Club!</h2>
            <p>You're officially on the list.</p>
            <p>As a subscriber, you'll be the first to know about new drops, exclusive collections, and secret sales.</p>
            
            <div style="background: #000; color: #fff; padding: 20px; text-align: center; margin: 30px 0; border-radius: 4px;">
              <h3 style="margin: 0; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Your Welcome Gift</h3>
              <p style="margin: 10px 0 0 0; font-size: 24px; font-weight: bold;">Use code: STARR10</p>
              <p style="margin: 5px 0 0 0; font-size: 14px;">For 10% off your first order</p>
            </div>
            
            <p style="margin-top: 40px; font-size: 12px; color: #666; text-align: center;">
              You received this email because you subscribed on our website.
            </p>
          </div>
        `;

        await resend.emails.send({
          from: "Starr Club <newsletter@resend.dev>",
          to: email,
          subject: "Welcome to STARR 🌟 - Here is 10% Off!",
          html: emailHtml,
        });
      } catch (emailError) {
        console.error("Failed to send welcome email:", emailError);
      }
    }

    return NextResponse.json({ success: true, message: "Successfully subscribed!" });
  } catch (error) {
    console.error("Subscription error:", error);
    return NextResponse.json({ error: "Failed to subscribe" }, { status: 500 });
  }
}
