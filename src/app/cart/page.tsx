import CartClient from "@/components/CartClient";

export const metadata = {
  title: "Shopping Cart - Starr",
  description: "View your shopping cart",
};

export default function CartPage() {
  return (
    <main>
      <CartClient />
    </main>
  );
}
