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
            <h2 style="border-bottom: 2px solid #000; padding-bottom: 10px;">New Subscriber Alert!</h2>
            <p>You have a new subscriber from the STARR website newsletter form.</p>
            <div style="background: #f9f9f9; padding: 20px; border-left: 4px solid #000; margin: 20px 0;">
              <strong>Email Address:</strong> ${email}
            </div>
            <p style="font-size: 12px; color: #666;">This notification was generated automatically.</p>
          </div>
        `;

        await resend.emails.send({
          from: "Starr Notifications <onboarding@resend.dev>",
          to: "olusojiteniola26@gmail.com",
          subject: "New Newsletter Subscriber - STARR",
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
