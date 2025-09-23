---
layout: base
title: Background with Object
description: Use JavaScript to have an in motion background.
sprite: images/platformer/sprites/redcarthatREALLYworks.png
background: images/platformer/backgrounds/THEBETTERSTREETPLSWORK.png
permalink: /background
---

<canvas id="world"></canvas>

<!-- Controls: speed slider -->
<div id="controls" style="position:fixed; top:10px; left:10px; background: rgba(255,255,255,0.9); padding:6px 8px; border-radius:6px; z-index:1000; font-family: sans-serif; font-size:14px;">
  <label style="display:block; margin-bottom:4px;">Speed: <span id="speedValue">6</span></label>
  <input id="speedRange" type="range" min="1" max="30" value="6" />
  <div id="speedDesc" style="margin-top:6px; font-size:12px; color:#333; max-width:220px;">
    Play around with the speed of the car 😁

<a href="https://precia-verma.github.io/Group-projects/homebrew-installation-shop/" style="text-decoration: none; position: absolute; top: 200px; left: 240px;">
<button style="background-color: #f59f00ff; color: #f7f6f8ff; padding: 3.5px 20px; border-radius: 8px; font-weight: bold; border: none; cursor: pointer;">
    The Homebrew Shop
  </button>
</a>
<a href="https://precia-verma.github.io/Group-projects/ruby-gems-installation-shop/" style="text-decoration: none; position: absolute; top: 220px; left: 510px;">
  <button style="background-color: #a72a26ff; color: #faf2c4ff; padding: 2px 20px; border-radius: 8px; font-weight: bold; border: none; cursor: pointer;">
   The Ruby Gem Shop
  </button>
</a>
  <a href="https://precia-verma.github.io/Group-projects/python-installation-shop/" 
     style="text-decoration: none; position: absolute; top: 240px; left: 815px;">
    <button style="background-color: #344e74ff; color: #c7c7c7ff; 
                   padding: 3px 20px; border-radius: 8px; 
                   font-weight: bold; border: none; cursor: pointer;">
      The Pet Python Shop
    </button>
  </a>
</div>





<script>
  // Get the canvas and its drawing context
  const canvas = document.getElementById("world");
  const ctx = canvas.getContext('2d');
  // Create image objects for background and sprite
  const backgroundImg = new Image();
  const spriteImg = new Image();
  // Set image sources using Jekyll page variables
  backgroundImg.src = '{{page.background}}';
  spriteImg.src = '{{page.sprite}}';

  let imagesLoaded = 0;
  // Wait for background image to load
  backgroundImg.onload = function() {
    imagesLoaded++;
    startGameWorld();
  };
  // Wait for sprite image to load
  spriteImg.onload = function() {
    imagesLoaded++;
    startGameWorld();
  };

  // Start the game world only when both images are loaded
  function startGameWorld() {
    if (imagesLoaded < 2) return;

    // Base class for all game objects
    class GameObject {
      constructor(image, width, height, x = 0, y = 0, speedRatio = 0) {
        this.image = image;
        this.width = width;
        this.height = height;
        this.x = x;
        this.y = y;
        this.speedRatio = speedRatio;
        // Speed is based on game speed and object's speed ratio
        this.speed = GameWorld.gameSpeed * this.speedRatio;
      }
      update() {}
      // Draw the object on the canvas
      draw(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
      }
    }

    // Background class for scrolling effect
    class Background extends GameObject {
      constructor(image, gameWorld) {
        // Fill entire canvas
        super(image, gameWorld.width, gameWorld.height, 0, 0, 0.1);
      }
      // Stop background from moving
      update() {
        // Do nothing, background stays static
      }
      // Draw two backgrounds for seamless scrolling
      draw(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
        ctx.drawImage(this.image, this.x + this.width, this.y, this.width, this.height);
      }
    }

    // Player class for animated sprite
    class Player extends GameObject {
      constructor(image, gameWorld) {
        // Scale sprite to half its natural size and center it
    const scale = 0.8; // change this number to tweak size (e.g., 1 = natural, 0.5 = half)
    const width = image.naturalWidth * scale;
    const height = image.naturalHeight * scale;
  // Start the player a bit left of center. Change startOffset to move further left/right.
  const startOffset = 500; // pixels to shift left from center (increase to move further left)
  const x = Math.max(0, (gameWorld.width - width) / 2 - startOffset);
        const y = (gameWorld.height - height) / 2 + 200;
        super(image, width, height, x, y);
        this.baseY = y;
        this.frame = 0;
        // Movement properties
        this.gameWorld = gameWorld;
  this.speed = 6; // pixels per frame when moving
  this.movingForward = false; // holding forward key
  this.movingBackward = false; // holding backward key
  this.vx = 0;
      }
      // Update player position and simple animation
      update() {
  // Compute horizontal velocity from forward/back flags
  const dir = (this.movingForward ? 1 : 0) - (this.movingBackward ? 1 : 0);
  this.vx = dir * this.speed;
  this.x += this.vx;
        // Keep player inside the canvas horizontally
        const minX = 0;
        const maxX = this.gameWorld.width - this.width;
        if (this.x < minX) this.x = minX;
        if (this.x > maxX) this.x = maxX;

        // Simple frame animation (if sprite sheet, advance frame)
        this.frame = (this.frame + 1) % 60;
      }
    }

    // Main game world class
    class GameWorld {
      static gameSpeed = 5;
      constructor(backgroundImg, spriteImg) {
        this.canvas = document.getElementById("world");
        this.ctx = this.canvas.getContext('2d');
        // Set canvas size to window size
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.canvas.width = this.width;
        this.canvas.height = this.height;
        this.canvas.style.width = `${this.width}px`;
        this.canvas.style.height = `${this.height}px`;
        this.canvas.style.position = 'absolute';
        this.canvas.style.left = `0px`;
        this.canvas.style.top = `${(window.innerHeight - this.height) / 2}px`;

        // Add background and player to game objects
        const bg = new Background(backgroundImg, this);
        const player = new Player(spriteImg, this);
        this.player = player; // expose for input handling
        this.gameObjects = [
         bg,
         player
        ];
        // Keyboard handlers to control player movement (forward and backward)
        window.addEventListener('keydown', (e) => {
          if (e.key === 'ArrowRight' || e.key === 'ArrowUp') {
            player.movingForward = true;
            e.preventDefault();
          }
          if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') {
            player.movingBackward = true;
            e.preventDefault();
          }
        });
        window.addEventListener('keyup', (e) => {
          if (e.key === 'ArrowRight' || e.key === 'ArrowUp') {
            player.movingForward = false;
            e.preventDefault();
          }
          if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') {
            player.movingBackward = false;
            e.preventDefault();
          }
        });
      }
      // Main game loop: update and draw all objects
      gameLoop() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        for (const obj of this.gameObjects) {
          obj.update();
          obj.draw(this.ctx);
        }
        requestAnimationFrame(this.gameLoop.bind(this));
      }
      // Start the game loop
      start() {
        this.gameLoop();
      }
    }

    // Create and start the game world
    const world = new GameWorld(backgroundImg, spriteImg);
    // Initialize player speed from the slider value
    const speedRange = document.getElementById('speedRange');
    const speedValue = document.getElementById('speedValue');
    // set initial speed
    world.player.speed = Number(speedRange.value);
    speedValue.textContent = speedRange.value;
    // update speed live when slider changes
    speedRange.addEventListener('input', (e) => {
      const v = Number(e.target.value);
      world.player.speed = v;
      speedValue.textContent = v;
    });
    // Start the game loop
    world.start();
  }
</script>
