---
layout: base
title: Background with Object 
description: Use Javascript to have an in motion
sprite: images/platformer/sprites/gravestone_1.png
background: images/platformer/backgrounds/spookyforestforgame.png
permalink: /spookyforest
---


<canvas id="world"></canvas> <!-- Canvas element for rendering the game world -->

<script>
  window.onload = function() {
}
  const canvas = document.getElementById("world"); // Get the canvas element
  const ctx = canvas.getContext('2d'); // Get the 2D drawing context
  const backgroundImg = new Image(); // Create a new Image for the background
  const spriteImg = new Image(); // Create a new Image for the sprite
  backgroundImg.src = 'images/platformer/backgrounds/spookyforestforgame.png'; // Set background image source from front matter
 spriteImg.src = 'images/platformer/sprites/gravestone_1.png'; // Set sprite image source from front matter

  let imagesLoaded = 0; // Track number of loaded images
  backgroundImg.onload = function() { // When background image loads
    imagesLoaded++; // Increment loaded count
    startGameWorld(); // Try to start the game
  };
  spriteImg.onload = function() { // When sprite image loads
    imagesLoaded++; // Increment loaded count
    startGameWorld(); // Try to start the game
  };

  // Load different sprite images
  const sprite2Img = new Image();
  sprite2Img.src = 'images/platformer/sprites/gravestone_2.png';
  const sprite3Img = new Image();
  sprite3Img.src = 'images/platformer/sprites/gravestone_3.png';
  const sprite4Img = new Image();
  sprite4Img.src = 'images/platformer/sprites/gravestone_4.png';
  const sprite5Img = new Image();
  sprite5Img.src = 'images/platformer/sprites/gravestone_5.png';
  const sprite6Img = new Image();
  sprite6Img.src = 'images/platformer/sprites/gravestone_6.png';



  function startGameWorld() {
    if (imagesLoaded < 2) return; // Wait until both images are loaded

    const NOTE_FREQ = {
  "e4": 329.63, "g4": 392.00, "d#4": 311.13,
  "f#4": 369.99, "c4": 261.63, "f4": 349.23, "c#4": 277.18
};
const GRAVE_TO_NOTE = { 1:"e4", 2:"g4", 3:"d#4", 4:"f#4", 5:"c4", 6:"f4" };
const SUCCESS_NOTE = "c#4";

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
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
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

    // Player class, animates sprite up and down
    class Player extends GameObject {
      constructor(image, gameWorld, customX, customY) {
        const width = image.naturalWidth / 2; // Set sprite width
        const height = image.naturalHeight / 2; // Set sprite height
        const x = customX !== undefined ? customX : (gameWorld.width - width) / 2; // Use custom X or center horizontally
        const y = customY !== undefined ? customY : (gameWorld.height - height) / 2; // Use custom Y or center vertically
        super(image, width, height, x, y); // Call base constructor
        this.baseY = y; // Store base Y position
        this.frame = 0; // Animation frame counter
      }
      update() {
        // this.y = this.baseY + Math.sin(this.frame * 0.05) * 20; // Animate up and down
        // this.frame++; // Increment frame
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
         new Player(spriteImg, this, 150, this.height / 2 - 60), // First gravestone 
         new Player(sprite2Img, this, 330, this.height / 2 - 60), // Second gravestone 
         new Player(sprite3Img, this, 496, this.height / 2 - 60), // Third gravestone 
         new Player(sprite4Img, this, 670, this.height / 2 - 60), // Fourth gravestone
         new Player(sprite5Img, this, 835, this.height / 2 - 60), // Fifth gravestone
         new Player(sprite6Img, this, 999, this.height / 2 - 60) // Sixth gravestone
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
