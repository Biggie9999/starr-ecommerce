import { NextResponse } from "next/server";
import prisma from "@/lib/prisma";

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const { name, email, phone, address, state, items } = body;

    if (!email || !items || items.length === 0) {
      return NextResponse.json({ error: "Invalid order data" }, { status: 400 });
    }

    // Verify all products still exist in the database
    const productIds = items.map((item: any) => item.id);
    const uniqueProductIds = Array.from(new Set(productIds)) as string[];
    
    const existingProducts = await prisma.product.findMany({
      where: { id: { in: uniqueProductIds } },
      select: { id: true, price: true, name: true }
    });

    if (existingProducts.length !== uniqueProductIds.length) {
      return NextResponse.json({ 
        error: "Checkout failed", 
        details: "Some products in your cart are no longer available. Please empty your cart and try again." 
      }, { status: 400 });
    }

    // Calculate true total from database prices
    let calculatedTotal = 0;
    const verifiedItems = items.map((clientItem: any) => {
      const dbProduct = existingProducts.find(p => p.id === clientItem.id);
      if (!dbProduct) throw new Error("Product missing during calculation");
      
      const truePrice = dbProduct.price;
      calculatedTotal += truePrice * clientItem.quantity;
      
      return {
        productId: dbProduct.id,
        quantity: clientItem.quantity,
        size: clientItem.size,
        price: truePrice,
        name: dbProduct.name
      };
    });

    const NORTHERN_STATES = [
      "Adamawa", "Bauchi", "Benue", "Borno", "Gombe", "Jigawa", 
      "Kaduna", "Katsina", "Kebbi", "Kogi", "Nasarawa", "Niger", 
      "Plateau", "Sokoto", "Taraba", "Yobe", "Zamfara"
    ];

    let calculatedDeliveryFee = 5000;
    if (state === "Test") {
      calculatedDeliveryFee = 50;
    } else if (state === "Kwara") {
      calculatedDeliveryFee = 3000;
    } else if (NORTHERN_STATES.includes(state)) {
      calculatedDeliveryFee = 8000;
    } else if (!state) {
      calculatedDeliveryFee = 0; 
    }
    
    calculatedTotal += calculatedDeliveryFee;

    // Create the order in the database with status PENDING
    const fullDeliveryAddress = state ? `${address}\nState: ${state}` : address;
    
    const order = await prisma.order.create({
      data: {
        customerEmail: email,
        customerName: name,
        phoneNumber: phone,
        deliveryAddress: fullDeliveryAddress,
        totalAmount: calculatedTotal,
        status: "PENDING", 
        paystackReference: "CRYPTO_" + (new Date()).getTime().toString(),
        items: {
          create: verifiedItems.map((item: any) => ({
            productId: item.productId,
            quantity: item.quantity,
            size: item.size,
            price: item.price
          }))
        }
      }
    });

    // Call NowPayments to create invoice
    const nowPaymentsKey = process.env.NOWPAYMENTS_API_KEY || "G3KK8K7-9M4MXX7-GT0Y2QW-QBWDD9R";
    const appUrl = process.env.NEXT_PUBLIC_APP_URL || "https://star01.xyz"; 

    const invoicePayload = {
      price_amount: calculatedTotal,
      price_currency: "ngn", // Assuming Nigerian Naira
      order_id: order.id,
      order_description: "STARR E-Commerce Order",
      success_url: `${appUrl}/success`,
      cancel_url: `${appUrl}/`
    };

    const invoiceRes = await fetch("https://api.nowpayments.io/v1/invoice", {
      method: "POST",
      headers: {
        "x-api-key": nowPaymentsKey,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(invoicePayload)
    });

    const invoiceData = await invoiceRes.json();

    if (!invoiceRes.ok || !invoiceData.invoice_url) {
      console.error("NowPayments Error:", invoiceData);
      return NextResponse.json({ error: "Failed to generate Crypto Invoice", details: invoiceData.message || "Unknown error" }, { status: 500 });
    }

    return NextResponse.json({ success: true, invoice_url: invoiceData.invoice_url });
  } catch (error: any) {
    console.error("Crypto Checkout error:", error);
    return NextResponse.json({ error: "Checkout failed", details: error?.message || String(error) }, { status: 500 });
  }
}
