const canvas = document.getElementById('wheel');
const ctx = canvas.getContext('2d');
const spinBtn = document.getElementById('spin-btn');
const modal = document.getElementById('result-modal');
const prizeText = document.getElementById('prize-text');
const closeModalBtn = document.getElementById('close-modal-btn');

const prizes = [
    "Shoes from outlash",
    "Bundles for sew in",
    "Bouquet",
    "Gown from oh Polly",
    "iPhone 17pro"
];

// Modern, vibrant color palette
const colors = [
    '#FF3366', // Vibrant Pink
    '#7C4DFF', // Deep Purple
    '#00E5FF', // Cyan
    '#FFC400', // Amber
    '#00E676'  // Green
];

let currentRotation = 0;
let isSpinning = false;

function drawWheel() {
    const numSegments = prizes.length;
    const anglePerSegment = (2 * Math.PI) / numSegments;
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = Math.min(centerX, centerY);

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < numSegments; i++) {
        const startAngle = i * anglePerSegment - Math.PI / 2; // Start from top
        const endAngle = startAngle + anglePerSegment;

        // Draw segment
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.arc(centerX, centerY, radius, startAngle, endAngle);
        ctx.closePath();
        
        ctx.fillStyle = colors[i % colors.length];
        ctx.fill();

        // Add subtle gradient/shadow for 3D effect
        const gradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, radius);
        gradient.addColorStop(0, 'rgba(255,255,255,0.2)');
        gradient.addColorStop(1, 'rgba(0,0,0,0.2)');
        ctx.fillStyle = gradient;
        ctx.fill();

        // Draw border
        ctx.lineWidth = 2;
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        ctx.stroke();

        // Draw text
        ctx.save();
        ctx.translate(centerX, centerY);
        
        let angle = startAngle + anglePerSegment / 2;
        
        // Normalize angle
        let normalizedAngle = angle % (2 * Math.PI);
        if (normalizedAngle < 0) normalizedAngle += 2 * Math.PI;

        ctx.rotate(angle);
        
        ctx.textBaseline = 'middle';
        ctx.fillStyle = '#ffffff';
        // Adjust font size slightly
        ctx.font = 'bold 18px Outfit, sans-serif';
        
        // Add text shadow for better readability
        ctx.shadowColor = 'rgba(0, 0, 0, 0.7)';
        ctx.shadowBlur = 5;
        ctx.shadowOffsetX = 1;
        ctx.shadowOffsetY = 1;

        // Prevent upside down text on the left side of the wheel
        if (normalizedAngle > Math.PI / 2 && normalizedAngle < 3 * Math.PI / 2) {
            ctx.rotate(Math.PI);
            ctx.textAlign = 'left';
            // Start near outer edge, grow towards center
            ctx.fillText(prizes[i], -radius + 40, 0, radius - 80);
        } else {
            ctx.textAlign = 'right';
            // Start near outer edge, grow towards center
            ctx.fillText(prizes[i], radius - 40, 0, radius - 80);
        }
        
        ctx.restore();
    }
    
    // Draw center dot
    ctx.beginPath();
    ctx.arc(centerX, centerY, 15, 0, 2 * Math.PI);
    ctx.fillStyle = '#ffffff';
    ctx.fill();
    ctx.shadowColor = 'transparent';
}

function spin() {
    if (isSpinning) return;
    
    isSpinning = true;
    spinBtn.disabled = true;

    // Calculate rotation
    // Minimum 5 full spins (5 * 360 = 1800 degrees) plus a random angle
    const minSpins = 5;
    const randomAngle = Math.random() * 360;
    const totalRotation = (minSpins * 360) + randomAngle;
    
    currentRotation += totalRotation;

    // Apply rotation via CSS
    canvas.style.transform = `rotate(${currentRotation}deg)`;

    // Wait for transition to finish
    setTimeout(() => {
        isSpinning = false;
        spinBtn.disabled = false;
        showResult(currentRotation);
    }, 5000); // 5s matches CSS transition duration
}

function showResult(rotation) {
    // Calculate which segment we landed on
    const numSegments = prizes.length;
    const degreesPerSegment = 360 / numSegments;
    
    // Normalize rotation to 0-360
    const normalizedRotation = rotation % 360;
    
    // The pointer is at the top (270 degrees in standard circle math, or 0 degrees relative to our starting position)
    // Since we rotate the canvas clockwise, the prize at the top moves backwards relative to the pointer
    // We need to calculate the offset
    let winningIndex = Math.floor((360 - normalizedRotation) / degreesPerSegment);
    
    // Ensure index is within bounds
    winningIndex = winningIndex % numSegments;
    
    prizeText.textContent = `You won: ${prizes[winningIndex]}! 🎉`;
    modal.classList.remove('hidden');
}

// Event Listeners
spinBtn.addEventListener('click', spin);
closeModalBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
});

// Initial draw
drawWheel();
