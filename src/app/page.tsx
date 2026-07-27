export default function Home() {
  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#000000',
      color: '#ffffff',
      fontFamily: 'var(--font-outfit), sans-serif',
      textAlign: 'center',
      padding: '2rem'
    }}>
      <h1 style={{
        fontSize: 'clamp(3rem, 10vw, 7rem)',
        fontWeight: 900,
        letterSpacing: '-0.03em',
        lineHeight: 1,
        marginBottom: '1.5rem',
        textTransform: 'uppercase'
      }}>
        Store is closed.
      </h1>
      <p style={{
        fontSize: 'clamp(1.25rem, 3vw, 2.25rem)',
        letterSpacing: '0.25em',
        textTransform: 'uppercase',
        opacity: 0.7,
        fontWeight: 500
      }}>
        Coming soon
      </p>
    </div>
  );
}
