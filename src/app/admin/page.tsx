"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";

export default function AdminDashboard() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [password, setPassword] = useState("");

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [category, setCategory] = useState("Tees");
  const [imageFile, setImageFile] = useState<File | null>(null);
  const [sizesInput, setSizesInput] = useState("S,M,L,XL");
  
  const [products, setProducts] = useState<any[]>([]);
  const [orders, setOrders] = useState<any[]>([]);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<"products" | "orders">("products");

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const router = useRouter();

  useEffect(() => {
    if (isAuthenticated) {
      fetch("/api/products")
        .then(res => res.json())
        .then(data => {
          if (Array.isArray(data)) setProducts(data);
        })
        .catch(console.error);
        
      fetch("/api/orders")
        .then(res => res.json())
        .then(data => {
          if (Array.isArray(data)) setOrders(data);
        })
        .catch(console.error);
    }
  }, [isAuthenticated]);

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    if (password === "admin123") {
      setIsAuthenticated(true);
    } else {
      alert("Invalid password");
    }
  };

  const handleEdit = (product: any) => {
    setEditingId(product.id);
    setName(product.name);
    setDescription(product.description);
    setPrice(product.price.toString());
    setCategory(product.category || "Tees");
    setSizesInput(product.sizes.map((s: any) => s.name).join(","));
    setMessage("");
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleDelete = async (id: string) => {
    if (!confirm("Are you sure you want to delete this product?")) return;
    try {
      const res = await fetch(`/api/products/${id}`, { method: "DELETE" });
      if (!res.ok) throw new Error();
      setProducts(products.filter(p => p.id !== id));
      if (editingId === id) resetForm();
    } catch (e) {
      alert("Failed to delete product");
    }
  };

  const resetForm = () => {
    setEditingId(null);
    setName("");
    setDescription("");
    setPrice("");
    setCategory("Tees");
    setImageFile(null);
    setSizesInput("S,M,L,XL");
  };

  const handleUpdateOrderStatus = async (orderId: string, status: string) => {
    try {
      const res = await fetch(`/api/orders/${orderId}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ status })
      });
      if (res.ok) {
        setOrders(orders.map(o => o.id === orderId ? { ...o, status } : o));
      }
    } catch (e) {
      console.error(e);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    const sizes = sizesInput.split(",").map(s => s.trim()).filter(s => s);

    if (editingId) {
      try {
        const res = await fetch(`/api/products/${editingId}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name, description, price, category, sizes })
        });
        if (!res.ok) throw new Error("Failed to update");
        
        setMessage("Product updated successfully!");
        resetForm();
        fetch("/api/products").then(r => r.json()).then(setProducts);
      } catch (error) {
        setMessage("Error updating product");
      } finally {
        setLoading(false);
      }
      return;
    }

    if (!imageFile) {
      setMessage("Please select an image");
      setLoading(false);
      return;
    }

    try {
      const formData = new FormData();
      formData.append("file", imageFile);
      
      const uploadRes = await fetch("/api/upload", {
        method: "POST",
        body: formData,
      });
      
      if (!uploadRes.ok) throw new Error("Failed to upload image");
      
      const uploadData = await uploadRes.json();
      const imageUrl = uploadData.url;

      const res = await fetch("/api/products", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name,
          description,
          price,
          category,
          images: [imageUrl],
          sizes
        })
      });

      if (!res.ok) throw new Error("Failed to create product");
      
      setMessage("Product created successfully!");
      resetForm();
      fetch("/api/products").then(r => r.json()).then(setProducts);
    } catch (error) {
      setMessage("Error creating product");
    } finally {
      setLoading(false);
    }
  };

  if (!isAuthenticated) {
    return (
      <div className="container" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '60vh' }}>
        <div className="glass-card" style={{ width: '100%', maxWidth: '400px' }}>
          <h2 style={{ marginBottom: '1.5rem', textAlign: 'center' }}>Admin Login</h2>
          <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <input 
              type="password" 
              className="input-field" 
              placeholder="Enter admin password (admin123)" 
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button type="submit" className="btn btn-primary">Login</button>
          </form>
        </div>
      </div>
    );
  }

  return (
    <div className="container" style={{ padding: '4rem 1.5rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1 style={{ margin: 0 }}>Admin Dashboard</h1>
        <div style={{ display: 'flex', gap: '1rem' }}>
          <button 
            className={`btn ${activeTab === 'products' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('products')}
          >
            Products
          </button>
          <button 
            className={`btn ${activeTab === 'orders' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('orders')}
          >
            Orders
          </button>
        </div>
      </div>
      
      {activeTab === 'products' ? (
      <div style={{ display: 'flex', gap: '2rem', flexWrap: 'wrap', alignItems: 'flex-start' }}>
        <div className="glass-card" style={{ flex: '1 1 400px', maxWidth: '600px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
            <h2>{editingId ? "Edit Product" : "Upload New Product"}</h2>
            {editingId && (
              <button onClick={resetForm} style={{ background: 'transparent', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', textDecoration: 'underline' }}>
                Cancel Edit
              </button>
            )}
          </div>
          
          {message && (
            <div style={{ padding: '1rem', marginBottom: '1.5rem', background: 'rgba(16, 185, 129, 0.1)', color: 'var(--success)', borderRadius: '0.5rem' }}>
              {message}
            </div>
          )}

          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <div>
              <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Product Name</label>
              <input type="text" className="input-field" value={name} onChange={e => setName(e.target.value)} required />
            </div>
            
            <div>
              <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Description</label>
              <textarea 
                className="input-field" 
                rows={4} 
                value={description} 
                onChange={e => setDescription(e.target.value)} 
                required 
              />
            </div>
            
            <div>
              <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Price (₦)</label>
              <input type="number" step="0.01" className="input-field" value={price} onChange={e => setPrice(e.target.value)} required />
            </div>

            <div>
              <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Category</label>
              <select className="input-field" value={category} onChange={e => setCategory(e.target.value)} required style={{ width: '100%' }}>
                <option value="Tees">Tees</option>
                <option value="Hoodies">Hoodies</option>
                <option value="Accessories">Accessories</option>
              </select>
            </div>
            
            {!editingId && (
              <div>
                <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Product Image (Photo Library)</label>
                <input 
                  type="file" 
                  accept="image/*"
                  className="input-field" 
                  onChange={e => e.target.files && setImageFile(e.target.files[0])} 
                  required={!editingId}
                />
              </div>
            )}
            
            <div>
              <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Available Sizes (comma separated)</label>
              <input type="text" className="input-field" value={sizesInput} onChange={e => setSizesInput(e.target.value)} required />
            </div>
            
            <button type="submit" className="btn btn-primary" disabled={loading}>
              {loading ? "Saving..." : (editingId ? "Update Product" : "Upload Product")}
            </button>
          </form>
        </div>

        <div className="glass-card" style={{ flex: '1 1 400px' }}>
          <h2 style={{ marginBottom: '1.5rem' }}>Manage Products</h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {products.length === 0 ? (
              <p style={{ color: 'var(--text-muted)' }}>No products found.</p>
            ) : (
              products.map(product => (
                <div key={product.id} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '1rem', border: '1px solid var(--border)', borderRadius: '0.5rem' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                    {product.images && product.images[0] && (
                      <img src={product.images[0].url} alt={product.name} style={{ width: '50px', height: '50px', objectFit: 'cover', borderRadius: '0.25rem' }} />
                    )}
                    <div>
                      <h4 style={{ margin: 0 }}>{product.name}</h4>
                      <p style={{ margin: 0, color: 'var(--text-muted)', fontSize: '0.875rem' }}>₦{product.price.toFixed(2)}</p>
                    </div>
                  </div>
                  <div style={{ display: 'flex', gap: '0.5rem' }}>
                    <button onClick={() => handleEdit(product)} className="btn btn-secondary" style={{ padding: '0.5rem 1rem', fontSize: '0.875rem' }}>Edit</button>
                    <button onClick={() => handleDelete(product.id)} className="btn" style={{ padding: '0.5rem 1rem', fontSize: '0.875rem', background: 'var(--danger)', color: 'white' }}>Delete</button>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
      ) : (
      <div style={{ width: '100%' }}>
        <div className="glass-card" style={{ width: '100%' }}>
          <h2 style={{ marginBottom: '1.5rem' }}>Customer Orders</h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {orders.length === 0 ? (
              <p style={{ color: 'var(--text-muted)' }}>No orders found.</p>
            ) : (
              orders.map(order => (
                <div key={order.id} style={{ padding: '1.5rem', border: '1px solid var(--border)', borderRadius: '0.5rem', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1rem' }}>
                    <div>
                      <h4 style={{ margin: 0, fontWeight: 700 }}>Order: {order.id}</h4>
                      <p style={{ margin: 0, color: 'var(--text-muted)', fontSize: '0.875rem' }}>Customer: {order.customerEmail}</p>
                      <p style={{ margin: 0, color: 'var(--text-muted)', fontSize: '0.875rem' }}>Total: ₦{order.totalAmount.toFixed(2)}</p>
                      <p style={{ margin: 0, color: 'var(--text-muted)', fontSize: '0.875rem' }}>Date: {new Date(order.createdAt).toLocaleString()}</p>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: '0.5rem' }}>
                      <span style={{ 
                        padding: '0.25rem 0.75rem', 
                        borderRadius: '9999px', 
                        fontSize: '0.75rem', 
                        fontWeight: 700,
                        backgroundColor: order.status === 'PAID' ? 'var(--foreground)' : (order.status === 'SHIPPED' ? 'var(--success)' : 'var(--border)'),
                        color: order.status === 'PENDING' ? 'black' : 'white'
                      }}>
                        {order.status}
                      </span>
                      {order.status === 'PAID' && (
                        <button onClick={() => handleUpdateOrderStatus(order.id, 'SHIPPED')} className="btn btn-secondary" style={{ padding: '0.5rem 1rem', fontSize: '0.75rem' }}>
                          Mark as Shipped
                        </button>
                      )}
                    </div>
                  </div>
                  
                  <div style={{ borderTop: '1px solid var(--border)', paddingTop: '1rem' }}>
                    <h5 style={{ margin: '0 0 0.5rem 0', fontWeight: 600 }}>Items:</h5>
                    <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '0.25rem' }}>
                      {order.items.map((item: any) => (
                        <li key={item.id} style={{ fontSize: '0.875rem', color: 'var(--text-muted)' }}>
                          {item.quantity}x {item.product?.name || 'Unknown Product'} (Size: {item.size}) - ₦{item.price.toFixed(2)}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
      )}
    </div>
  );
}
