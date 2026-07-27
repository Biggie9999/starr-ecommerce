export default function Home() {
  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      background: 'url(/store-closed-bg.jpg) center/contain no-repeat',
      backgroundColor: '#ffffff',
      color: '#000000',
      fontFamily: 'var(--font-outfit), sans-serif',
      textAlign: 'center',
      padding: '2rem'
    }}>
      <div style={{ 
        background: 'rgba(255, 255, 255, 0.85)', 
        padding: '3rem 4rem', 
        borderRadius: '1rem',
        backdropFilter: 'blur(8px)',
        boxShadow: '0 10px 30px rgba(0,0,0,0.1)'
      }}>
        <h1 style={{
          fontSize: 'clamp(3rem, 10vw, 7rem)',
          fontWeight: 900,
          letterSpacing: '-0.03em',
          lineHeight: 1,
          marginBottom: '1.5rem',
          textTransform: 'uppercase',
          color: '#000000'
        }}>
          Store is closed.
        </h1>
        <p style={{
          fontSize: 'clamp(1.25rem, 3vw, 2.25rem)',
          letterSpacing: '0.25em',
          textTransform: 'uppercase',
          fontWeight: 700,
          color: '#dc2626'
        }}>
          Coming soon
        </p>
      </div>
    </div>
  );
}
