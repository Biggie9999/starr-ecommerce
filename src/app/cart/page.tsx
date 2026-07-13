import CartClient from "@/components/CartClient";

export const metadata = {
  title: "Shopping Cart - Starr",
  description: "View your shopping cart",
};

export default function CartPage() {
  return (
    <main>
      <div style={{ background: 'var(--surface)', padding: '2rem 0', borderBottom: '1px solid var(--border)', textAlign: 'center' }}>
        <h1>Your Cart</h1>
      </div>
      <CartClient />
    </main>
  );
}
