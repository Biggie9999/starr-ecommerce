"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function AdminDashboard() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [password, setPassword] = useState("");

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [imageFile, setImageFile] = useState<File | null>(null);
  const [sizesInput, setSizesInput] = useState("S,M,L,XL");
  
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const router = useRouter();

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    if (password === "admin123") {
      setIsAuthenticated(true);
    } else {
      alert("Invalid password");
    }
  };

  const handleCreateProduct = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    if (!imageFile) {
      setMessage("Please select an image");
      setLoading(false);
      return;
    }

    const sizes = sizesInput.split(",").map(s => s.trim()).filter(s => s);

    try {
      // 1. Upload the file to Vercel Blob
      const formData = new FormData();
      formData.append("file", imageFile);
      
      const uploadRes = await fetch("/api/upload", {
        method: "POST",
        body: formData,
      });
      
      if (!uploadRes.ok) throw new Error("Failed to upload image");
      
      const uploadData = await uploadRes.json();
      const imageUrl = uploadData.url;

      // 2. Create the product with the returned URL
      const res = await fetch("/api/products", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name,
          description,
          price,
          images: [imageUrl],
          sizes
        })
      });

      if (!res.ok) throw new Error("Failed to create product");
      
      setMessage("Product created successfully!");
      setName("");
      setDescription("");
      setPrice("");
      setImageFile(null);
      
      // Navigate to home to see the product after a short delay
      setTimeout(() => {
        router.push("/");
        router.refresh();
      }, 1500);

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
      <h1 style={{ marginBottom: '2rem' }}>Admin Dashboard</h1>
      
      <div className="glass-card" style={{ maxWidth: '600px' }}>
        <h2 style={{ marginBottom: '1.5rem' }}>Upload New Product</h2>
        
        {message && (
          <div style={{ padding: '1rem', marginBottom: '1.5rem', background: 'rgba(16, 185, 129, 0.1)', color: 'var(--success)', borderRadius: '0.5rem' }}>
            {message}
          </div>
        )}

        <form onSubmit={handleCreateProduct} style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
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
            <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Price ($)</label>
            <input type="number" step="0.01" className="input-field" value={price} onChange={e => setPrice(e.target.value)} required />
          </div>
          
          <div>
            <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Product Image (Photo Library)</label>
            <input 
              type="file" 
              accept="image/*"
              className="input-field" 
              onChange={e => e.target.files && setImageFile(e.target.files[0])} 
              required 
            />
          </div>
          
          <div>
            <label style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--text-muted)' }}>Available Sizes (comma separated)</label>
            <input type="text" className="input-field" value={sizesInput} onChange={e => setSizesInput(e.target.value)} required />
          </div>
          
          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? "Uploading..." : "Upload Product"}
          </button>
        </form>
      </div>
    </div>
  );
}
