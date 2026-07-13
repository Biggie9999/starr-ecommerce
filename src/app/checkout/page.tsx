import CheckoutClient from "@/components/CheckoutClient";

export const metadata = {
  title: "Checkout - Starr",
};

export default function CheckoutPage() {
  return (
    <div>
      <div style={{ background: 'var(--surface)', padding: '2rem 0', borderBottom: '1px solid var(--border)', textAlign: 'center' }}>
        <h1>Checkout</h1>
      </div>
      <CheckoutClient />
    </div>
  );
}
