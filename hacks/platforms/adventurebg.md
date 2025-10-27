---
layout: base
title: Background with Object 
description: Use JavaScript to have an in motion background.
sprite: images/platformer/sprites/lonelypsychodude.png
background: images/platformer/backgrounds/Cemetery.png
permalink: /dead
---

<style>
#world {
    border: 1px solid black;
    width: 800px;
    height: 400px;
}
</style>

<canvas id="world" width="800" height="400"></canvas> <!-- Canvas element for rendering the game world -->

<script>
  window.onload = function() {
    // Initialize game when window loads
    const canvas = document.getElementById("world"); // Get the canvas element
  const ctx = canvas.getContext('2d'); // Get the 2D drawing context
  const backgroundImg = new Image(); // Create a new Image for the background
  const spriteImg = new Image(); // Create a new Image for the sprite
  backgroundImg.src = 'images/platformer/backgrounds/Cemetery.png'; // Set background image source from front matter
 spriteImg.src = 'images/platformer/sprites/lonelypsychodude.png'; // Set sprite image source from front matter

  let imagesLoaded = 0; // Track number of loaded images
  backgroundImg.onload = function() { // When background image loads
    imagesLoaded++; // Increment loaded count
    startGameWorld(); // Try to start the game
  };
  spriteImg.onload = function() { // When sprite image loads
    imagesLoaded++; // Increment loaded count
    startGameWorld(); // Try to start the game
  };

  function startGameWorld() {
    if (imagesLoaded < 2) return; // Wait until both images are loaded

    // Base class for all game objects
    class GameObject {
      constructor(image, width, height, x = 0, y = 0, speedRatio = 0) {
        this.image = image; // Image to draw
        this.width = width; // Width of object
        this.height = height; // Height of object
        this.x = x; // X position
        this.y = y; // Y position
        this.speedRatio = speedRatio; // Speed ratio for movement
        this.speed = GameWorld.gameSpeed * this.speedRatio; // Actual speed
      }
      update() {} // Update object state (empty for base)
      draw(ctx) { // Draw object on canvas
        // Use imageSmoothingEnabled = false to keep GIF pixels crisp
        ctx.imageSmoothingEnabled = false;
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
        ctx.imageSmoothingEnabled = true;
      }
    }

    // Background class, scrolls horizontally
    class Background extends GameObject {
      constructor(image, gameWorld) {
        // Fill entire canvas with background image
        super(image, gameWorld.width, gameWorld.height, 0, 0, 0);
      }
      update() {
        this.x = (this.x - this.speed) % this.width; // Move background left, wrap around
      }
      draw(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height); // Draw first background
        ctx.drawImage(this.image, this.x + this.width, this.y, this.width, this.height); // Draw second for seamless scroll
      }
    }

    // Player class with WASD controls
    class Player extends GameObject {
      constructor(image, gameWorld) {
        const width = image.naturalWidth / 8; // Set sprite width (even smaller)
        const height = image.naturalHeight / 8; // Set sprite height (even smaller)
        const x = (gameWorld.width - width) / 2; // Center horizontally
        const y = (gameWorld.height - height) / 2; // Center vertically
        super(image, width, height, x, y); // Call base constructor
        this.moveSpeed = 5; // Movement speed
        this.keys = { w: false, a: false, s: false, d: false }; // Track key states
        
        // Add key event listeners
        window.addEventListener('keydown', (e) => this.handleKeyDown(e));
        window.addEventListener('keyup', (e) => this.handleKeyUp(e));
      }

      handleKeyDown(e) {
        // Update key states on keydown
        // Prevent the browser from scrolling when pressing WASD
        const key = e.key.toLowerCase();
        if (key === 'w' || key === 'a' || key === 's' || key === 'd') {
          e.preventDefault();
        }
        switch(key) {
          case 'w': this.keys.w = true; break;
          case 'a': this.keys.a = true; break;
          case 's': this.keys.s = true; break;
          case 'd': this.keys.d = true; break;
        }
      }

      handleKeyUp(e) {
        // Update key states on keyup
        const key = e.key.toLowerCase();
        if (key === 'w' || key === 'a' || key === 's' || key === 'd') {
          e.preventDefault();
        }
        switch(key) {
          case 'w': this.keys.w = false; break;
          case 'a': this.keys.a = false; break;
          case 's': this.keys.s = false; break;
          case 'd': this.keys.d = false; break;
        }
      }

      update() {
        // Move horizontally based on key states (lock vertical position)
        if (this.keys.a) this.x -= this.moveSpeed;
        if (this.keys.d) this.x += this.moveSpeed;

        // Keep sprite within canvas horizontal bounds
        this.x = Math.max(0, Math.min(this.x, canvas.width - this.width));

        // Lock the vertical position to the vertical center of the canvas
        this.y = (canvas.height - this.height) / 2;
      }
    }

    // Game world class, manages canvas and objects
    class GameWorld {
      static gameSpeed = 5; // Base speed for game objects
      constructor(backgroundImg, spriteImg) {
        this.canvas = document.getElementById("world"); // Get canvas
        this.ctx = this.canvas.getContext('2d'); // Get context
        this.width = window.innerWidth; // Set canvas width to window width
        this.height = window.innerHeight; // Set canvas height to window height
        this.canvas.width = this.width; // Apply width
        this.canvas.height = this.height; // Apply height
        this.canvas.style.width = `${this.width}px`; // Style width
        this.canvas.style.height = `${this.height}px`; // Style height
        this.canvas.style.position = 'absolute'; // Position canvas
        this.canvas.style.left = `0px`; // Align left
        this.canvas.style.top = `${(window.innerHeight - this.height) / 2}px`; // Center vertically

        this.gameObjects = [
         new Background(backgroundImg, this), // Add background object
         new Player(spriteImg, this) // Add player object
        ];
      }
      gameLoop() {
        this.ctx.clearRect(0, 0, this.width, this.height); // Clear canvas
        for (const obj of this.gameObjects) { // Loop through game objects
          obj.update(); // Update object state
          obj.draw(this.ctx); // Draw object
        }
        requestAnimationFrame(this.gameLoop.bind(this)); // Loop again on next frame
      }
      start() {
        this.gameLoop(); // Start the game loop
      }
    }

    const world = new GameWorld(backgroundImg, spriteImg); // Create game world instance
    world.start(); // Start the game
  }
</script>
