---
layout: base
title: Gravestone Memory Game
description: A spooky memory game where players must remember and replicate sequences of glowing gravestones with musical notes.
permalink: /gravestone-memory-game
---

<style>
  #gameCanvas {
    border: 2px solid #333;
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    cursor: pointer;
  }
  
  .game-ui {
    text-align: center;
    font-family: 'Creepster', cursive;
    color: #fff;
    margin: 20px 0;
  }
  
  .score-display {
    font-size: 24px;
    margin: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
  }
  
  .game-button {
    background: linear-gradient(135deg, #8B0000, #B22222);
    color: white;
    border: none;
    padding: 15px 30px;
    font-size: 18px;
    cursor: pointer;
    border-radius: 10px;
    margin: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    transition: all 0.3s ease;
  }
  
  .game-button:hover {
    background: linear-gradient(135deg, #A52A2A, #DC143C);
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.4);
  }
  
  .game-button:disabled {
    background: #666;
    cursor: not-allowed;
    transform: none;
  }
  
  @import url('https://fonts.googleapis.com/css2?family=Creepster&display=swap');
</style>

<div class="game-ui">
  <h1>🪦 Gravestone Memory Game 🪦</h1>
  <div class="score-display">
    Score: <span id="scoreDisplay">0</span> | Level: <span id="levelDisplay">1</span>
  </div>
  <div>
    <button id="startButton" class="game-button">Start Game</button>
    <button id="resetButton" class="game-button">Reset</button>
  </div>
  <div id="gameStatus" style="font-size: 18px; margin: 15px 0; min-height: 25px;"></div>
</div>

<canvas id="gameCanvas" width="800" height="600"></canvas>

<script>
class GravestoneMemoryGame {
  constructor() {
    this.canvas = document.getElementById('gameCanvas');
    this.ctx = this.canvas.getContext('2d');
    this.scoreElement = document.getElementById('scoreDisplay');
    this.levelElement = document.getElementById('levelDisplay');
    this.statusElement = document.getElementById('gameStatus');
    this.startButton = document.getElementById('startButton');
    this.resetButton = document.getElementById('resetButton');
    
    // Game state
    this.gameActive = false;
    this.playerTurn = false;
    this.score = 0;
    this.level = 1;
    this.sequence = [];
    this.playerSequence = [];
    this.sequenceIndex = 0;
    
    // Images
    this.gravestoneImages = [];
    this.imagesLoaded = 0;
    this.totalImages = 2;
    
    // Gravestone properties
    this.gravestones = [];
    this.loadImages();
    
    // Audio context for generating tones
    this.audioContext = null;
    this.initializeAudio();
    
    // Event listeners
    this.setupEventListeners();
  }
  
  loadImages() {
    // Load gravestone images
    const imagePaths = [
      '/images/platformer/sprites/gravestone_1.png',
      '/images/platformer/sprites/gravestone_2.png'
    ];
    
    imagePaths.forEach((path, index) => {
      const img = new Image();
      img.onload = () => {
        this.imagesLoaded++;
        if (this.imagesLoaded === this.totalImages) {
          this.initializeGravestones();
          this.render();
        }
      };
      img.onerror = () => {
        console.error(`Failed to load image: ${path}`);
        this.imagesLoaded++;
        if (this.imagesLoaded === this.totalImages) {
          this.initializeGravestones();
          this.render();
        }
      };
      img.src = path;
      this.gravestoneImages[index] = img;
    });
  }
  
  initializeAudio() {
    try {
      this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
    } catch (e) {
      console.warn('Web Audio API not supported');
    }
  }
  
  initializeGravestones() {
    const colors = [
      { normal: '#8B4513', glow: '#FFD700', note: 261.63 }, 
      { normal: '#A0522D', glow: '#FF6347', note: 391.995 }, 
      { normal: '#654321', glow: '#32CD32', note: 311.13 },
      { normal: '#8B7355', glow: '#00CED1', note: 369.994 },
      { normal: '#A0522D', glow: '#9370DB', note: 261.63 }, 
      { normal: '#696969', glow: '#FF1493', note: 277.18} 
    ];
    
    const positions = [
      { x: 80, y: 200 },   // Gravestone 1
      { x: 200, y: 200 },  // Gravestone 2
      { x: 320, y: 200 },  // Gravestone 3
      { x: 440, y: 200 },  // Gravestone 4
      { x: 560, y: 200 },  // Gravestone 5
      { x: 680, y: 200 }   // Gravestone 6
    ];
    
    for (let i = 0; i < 6; i++) {
      this.gravestones.push({
        id: i,
        x: positions[i].x,
        y: positions[i].y,
        width: 80,
        height: 120,
        color: colors[i].normal,
        glowColor: colors[i].glow,
        isGlowing: false,
        glowIntensity: 0,
        note: colors[i].note,
        image: this.gravestoneImages[i % this.gravestoneImages.length] // Cycle through available images
      });
    }
  }
  
  setupEventListeners() {
    this.startButton.addEventListener('click', () => this.startGame());
    this.resetButton.addEventListener('click', () => this.resetGame());
    
    this.canvas.addEventListener('click', (e) => {
      if (this.playerTurn) {
        this.handleCanvasClick(e);
      }
    });
    
    // Resume audio context on user interaction
    this.canvas.addEventListener('click', () => {
      if (this.audioContext && this.audioContext.state === 'suspended') {
        this.audioContext.resume();
      }
    });
  }
  
  handleCanvasClick(e) {
    const rect = this.canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    // Check which gravestone was clicked
    for (let gravestone of this.gravestones) {
      if (x >= gravestone.x && x <= gravestone.x + gravestone.width &&
          y >= gravestone.y && y <= gravestone.y + gravestone.height) {
        this.handleGravestoneClick(gravestone.id);
        break;
      }
    }
  }
  
  handleGravestoneClick(gravestoneId) {
    if (!this.playerTurn) return;
    
    // Light up the clicked gravestone and play its note
    this.lightUpGravestone(gravestoneId);
    this.playNote(this.gravestones[gravestoneId].note);
    
    // Check if it matches the sequence
    if (gravestoneId === this.sequence[this.sequenceIndex]) {
      this.sequenceIndex++;
      
      // Check if player completed the sequence
      if (this.sequenceIndex >= this.sequence.length) {
        this.playerTurn = false;
        this.score += this.level * 10;
        this.updateDisplay();
        this.statusElement.textContent = "Correct! Preparing next sequence...";
        
        setTimeout(() => {
          this.nextLevel();
        }, 1500);
      }
    } else {
      // Wrong sequence
      this.gameOver();
    }
  }
  
  startGame() {
    this.gameActive = true;
    this.playerTurn = false;
    this.score = 0;
    this.level = 1;
    this.sequence = [];
    this.sequenceIndex = 0;
    
    this.startButton.disabled = true;
    this.updateDisplay();
    this.statusElement.textContent = "Get ready! Watch the sequence...";
    
    setTimeout(() => {
      this.nextLevel();
    }, 1000);
  }
  
  nextLevel() {
    this.level++;
    this.sequence.push(Math.floor(Math.random() * this.gravestones.length));
    this.sequenceIndex = 0;
    this.updateDisplay();
    
    this.statusElement.textContent = `Level ${this.level - 1}: Watch carefully...`;
    this.playSequence();
  }
  
  playSequence() {
    this.playerTurn = false;
    let index = 0;
    
    const playNext = () => {
      if (index < this.sequence.length) {
        const gravestoneId = this.sequence[index];
        this.lightUpGravestone(gravestoneId);
        this.playNote(this.gravestones[gravestoneId].note);
        
        index++;
        setTimeout(playNext, 800);
      } else {
        // Sequence finished, player's turn
        setTimeout(() => {
          this.playerTurn = true;
          this.statusElement.textContent = "Your turn! Click the gravestones in order.";
        }, 500);
      }
    };
    
    setTimeout(playNext, 500);
  }
  
  lightUpGravestone(id) {
    const gravestone = this.gravestones[id];
    gravestone.isGlowing = true;
    gravestone.glowIntensity = 1.0;
    
    // Fade out the glow over time
    const fadeOut = () => {
      gravestone.glowIntensity -= 0.05;
      if (gravestone.glowIntensity <= 0) {
        gravestone.isGlowing = false;
        gravestone.glowIntensity = 0;
      } else {
        requestAnimationFrame(fadeOut);
      }
    };
    
    setTimeout(() => {
      requestAnimationFrame(fadeOut);
    }, 300);
  }
  
  playNote(frequency) {
    if (!this.audioContext) return;
    
    const oscillator = this.audioContext.createOscillator();
    const gainNode = this.audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(this.audioContext.destination);
    
    oscillator.frequency.setValueAtTime(frequency, this.audioContext.currentTime);
    oscillator.type = 'sine';
    
    gainNode.gain.setValueAtTime(0.3, this.audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.5);
    
    oscillator.start(this.audioContext.currentTime);
    oscillator.stop(this.audioContext.currentTime + 0.5);
  }
  
  gameOver() {
    this.gameActive = false;
    this.playerTurn = false;
    this.startButton.disabled = false;
    this.statusElement.textContent = `Game Over! Final Score: ${this.score}`;
    
    // Flash all gravestones red
    this.gravestones.forEach((gravestone, index) => {
      setTimeout(() => {
        gravestone.isGlowing = true;
        gravestone.glowIntensity = 1.0;
        gravestone.glowColor = '#FF0000';
        
        setTimeout(() => {
          gravestone.isGlowing = false;
          gravestone.glowColor = this.getOriginalGlowColor(index);
        }, 200);
      }, index * 100);
    });
  }
  
  getOriginalGlowColor(index) {
    const colors = ['#FFD700', '#FF6347', '#32CD32', '#00CED1', '#9370DB', '#FF1493'];
    return colors[index];
  }
  
  resetGame() {
    this.gameActive = false;
    this.playerTurn = false;
    this.score = 0;
    this.level = 1;
    this.sequence = [];
    this.sequenceIndex = 0;
    this.startButton.disabled = false;
    
    this.gravestones.forEach(gravestone => {
      gravestone.isGlowing = false;
      gravestone.glowIntensity = 0;
    });
    
    this.updateDisplay();
    this.statusElement.textContent = "Game reset. Click Start to play!";
  }
  
  updateDisplay() {
    this.scoreElement.textContent = this.score;
    this.levelElement.textContent = this.level;
  }
  
  drawGravestone(gravestone) {
    const { x, y, width, height, isGlowing, glowColor, glowIntensity, image } = gravestone;
    
    if (!image) return; // Skip if image not loaded
    
    this.ctx.save();
    
    // Draw glow effect
    if (isGlowing && glowIntensity > 0) {
      this.ctx.shadowColor = glowColor;
      this.ctx.shadowBlur = 30 * glowIntensity;
      this.ctx.globalAlpha = 0.6 * glowIntensity;
      
      // Draw glowing background
      this.ctx.fillStyle = glowColor;
      this.ctx.fillRect(x - 10, y - 10, width + 20, height + 20);
    }
    
    this.ctx.restore();
    this.ctx.save();
    
    // Apply color tint if glowing
    if (isGlowing && glowIntensity > 0) {
      this.ctx.globalCompositeOperation = 'multiply';
      this.ctx.fillStyle = glowColor;
      this.ctx.fillRect(x, y, width, height);
      this.ctx.globalCompositeOperation = 'screen';
      this.ctx.globalAlpha = 0.3 * glowIntensity;
    }
    
    this.ctx.restore();
    
    // Draw the gravestone image
    this.ctx.drawImage(image, x, y, width, height);
    
    this.ctx.restore();
  }
  
  render() {
    // Clear canvas
    this.ctx.fillStyle = '#0a0a0a';
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    
    // Draw spooky background elements
    this.drawBackground();
    
    // Draw gravestones
    this.gravestones.forEach(gravestone => {
      this.drawGravestone(gravestone);
    });
    
    requestAnimationFrame(() => this.render());
  }
  
  drawBackground() {
    // Draw mist effect
    this.ctx.save();
    this.ctx.globalAlpha = 0.1;
    this.ctx.fillStyle = '#ffffff';
    
    for (let i = 0; i < 20; i++) {
      const x = Math.sin(Date.now() * 0.001 + i) * 50 + i * 40;
      const y = this.canvas.height - 100 + Math.sin(Date.now() * 0.002 + i) * 20;
      const radius = 30 + Math.sin(Date.now() * 0.003 + i) * 10;
      
      this.ctx.beginPath();
      this.ctx.arc(x, y, radius, 0, Math.PI * 2);
      this.ctx.fill();
    }
    
    // Draw ground
    this.ctx.globalAlpha = 0.3;
    this.ctx.fillStyle = '#2F4F2F';
    this.ctx.fillRect(0, this.canvas.height - 50, this.canvas.width, 50);
    
    this.ctx.restore();
  }
}

// Start the game when the page loads
window.addEventListener('DOMContentLoaded', () => {
  const game = new GravestoneMemoryGame();
});
</script>
