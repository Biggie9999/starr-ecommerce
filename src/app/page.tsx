export default function Home() {
  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#ffffff',
      fontFamily: 'var(--font-outfit), sans-serif',
      textAlign: 'center',
      padding: '2rem'
    }}>
      <img 
        src="/store-closed-bg.jpg" 
        alt="Starr Premium" 
        style={{ 
          maxWidth: '600px', 
          width: '100%', 
          marginBottom: '3rem' 
        }} 
      />
      
      <h1 style={{
        fontSize: 'clamp(2.5rem, 8vw, 6rem)',
        fontWeight: 900,
        letterSpacing: '-0.04em',
        lineHeight: 1,
        marginBottom: '1rem',
        textTransform: 'uppercase',
        color: '#000000'
      }}>
        Store is closed.
      </h1>
      <p style={{
        fontSize: 'clamp(1rem, 2vw, 1.5rem)',
        letterSpacing: '0.3em',
        textTransform: 'uppercase',
        fontWeight: 700,
        color: '#dc2626'
      }}>
        Coming soon
      </p>
    </div>
  );
}
