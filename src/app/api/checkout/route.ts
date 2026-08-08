import { NextResponse } from "next/server";
import prisma from "@/lib/prisma";
import { sendOrderEmails } from "@/lib/email";

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const { reference, name, email, phone, address, state, items } = body;

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
      const foundIds = existingProducts.map(p => p.id);
      const missingIds = uniqueProductIds.filter(id => !foundIds.includes(id));
      return NextResponse.json({ 
        error: "Checkout failed", 
        details: `The following product IDs are in your cart but missing from the database: ${missingIds.join(", ")}. Please completely empty your cart and try again.` 
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
    if (state === "Kwara") {
      calculatedDeliveryFee = 3000;
    } else if (NORTHERN_STATES.includes(state)) {
      calculatedDeliveryFee = 8000;
    } else if (!state) {
      calculatedDeliveryFee = 0; // Fallback just in case
    }
    
    const itemsSubtotal = calculatedTotal;
    calculatedTotal += calculatedDeliveryFee;

    // Verify payment with Paystack
    if (process.env.PAYSTACK_SECRET_KEY) {
      try {
        const paystackRes = await fetch(`https://api.paystack.co/transaction/verify/${reference}`, {
          headers: {
            Authorization: `Bearer ${process.env.PAYSTACK_SECRET_KEY}`
          }
        });
        const paystackData = await paystackRes.json();
        
        if (!paystackData.status || paystackData.data.status !== "success") {
          return NextResponse.json({ error: "Payment verification failed", details: "Transaction was not successful on Paystack." }, { status: 400 });
        }
        
        // Paystack amount is in kobo (base amount * 100)
        const expectedAmountKobo = Math.round(calculatedTotal * 100);
        if (paystackData.data.amount < expectedAmountKobo) {
          return NextResponse.json({ error: "Payment verification failed", details: "Amount paid is less than the calculated order total." }, { status: 400 });
        }
      } catch (paystackError) {
        console.error("Paystack verification error:", paystackError);
        return NextResponse.json({ error: "Payment verification failed", details: "Could not reach Paystack to verify transaction." }, { status: 500 });
      }
    } else {
      console.warn("WARNING: PAYSTACK_SECRET_KEY is not set. Skipping server-side payment verification. Do not do this in production!");
    }

    // Create the order in the database
    const fullDeliveryAddress = state ? `${address}\nState: ${state}` : address;
    
    const order = await prisma.order.create({
      data: {
        customerEmail: email,
        customerName: name,
        phoneNumber: phone,
        deliveryAddress: fullDeliveryAddress,
        totalAmount: calculatedTotal, // Use server-calculated total
        status: "PAID",
        paystackReference: reference,
        items: {
          create: verifiedItems.map((item: any) => ({
            productId: item.productId,
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
    await sendOrderEmails(order, calculatedTotal, calculatedDeliveryFee, state || 'N/A');

    return NextResponse.json({ success: true, orderId: order.id });
  } catch (error: any) {
    console.error("Checkout error:", error);
    return NextResponse.json({ error: "Checkout failed", details: error?.message || String(error) }, { status: 500 });
  }
}
