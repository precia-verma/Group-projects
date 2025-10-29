---
layout: base
title: Background with Object 
description: Use Javascript to have an in motion
sprite: images/platformer/sprites/test_sprite_sheet.png
background: images/platformer/backgrounds/spookyforestforgame.png
permalink: /backupplswork
---


<canvas id="world"></canvas> <!-- Canvas element for rendering the game world -->

<script>
  // Simple world with a single controllable sprite (WASD keys)
  const canvas = document.getElementById("world"); // Get the canvas element
  const ctx = canvas.getContext('2d'); // Get the 2D drawing context
  const backgroundImg = new Image(); // Create a new Image for the background
  const spriteImg = new Image(); // Create a new Image for the sprite (sprite sheet)
  backgroundImg.src = 'images/platformer/backgrounds/spookyforestforgame.png';
  // Use the provided sprite sheet (assumed horizontal strip of frames)
  spriteImg.src = 'images/platformer/sprites/test_sprite_sheet.png';

  let imagesLoaded = 0; // Track number of loaded images
  backgroundImg.onload = () => { imagesLoaded++; startGameWorld(); };
  spriteImg.onload = () => { imagesLoaded++; startGameWorld(); };

  // Simple key state for WASD
  const keys = { w: false, a: false, s: false, d: false };
  window.addEventListener('keydown', (e) => {
    const k = e.key.toLowerCase();
    if (k in keys) { keys[k] = true; e.preventDefault(); }
  });
  window.addEventListener('keyup', (e) => {
    const k = e.key.toLowerCase();
    if (k in keys) { keys[k] = false; e.preventDefault(); }
  });

  function startGameWorld() {
    if (imagesLoaded < 2) return; // wait until background and sprite are loaded

    // Base drawable object
    class GameObject {
      constructor(image, width, height, x = 0, y = 0) {
        this.image = image;
        this.width = width;
        this.height = height;
        this.x = x;
        this.y = y;
      }
      update() {}
      draw(ctx) { if (this.image) ctx.drawImage(this.image, this.x, this.y, this.width, this.height); }
    }

    // Background stretches to fill canvas and scrolls slowly
    class Background extends GameObject {
      constructor(image, gameWorld) {
        super(image, gameWorld.width, gameWorld.height, 0, 0);
        this.gameWorld = gameWorld;
        this.offset = 0;
      }
      update() { this.offset = (this.offset + 0.2) % this.width; }
      draw(ctx) {
        // Draw two copies for simple horizontal wrap
        ctx.drawImage(this.image, -this.offset, 0, this.width, this.height);
        ctx.drawImage(this.image, -this.offset + this.width, 0, this.width, this.height);
      }
    }

    // Player that responds to WASD and animates from a horizontal sprite sheet
    class Player extends GameObject {
      constructor(image, gameWorld, customX, customY) {
        // Assume sprite sheet is a horizontal strip of frames (default 4 frames)
        const frameCount = 4;
        const naturalW = image.naturalWidth || 64;
        const naturalH = image.naturalHeight || 64;
        const frameWidth = Math.floor(naturalW / frameCount);
        const frameHeight = naturalH;

        const width = Math.max(32, frameWidth); // drawn width
        const height = Math.max(32, frameHeight); // drawn height
        const x = customX !== undefined ? customX : (gameWorld.width - width) / 2;
        const y = customY !== undefined ? customY : (gameWorld.height - height) / 2;
        super(image, width, height, x, y);
        this.gameWorld = gameWorld;
        this.speed = 6; // pixels per frame

        // Animation state
        this.frameCount = frameCount;
        this.frameWidth = frameWidth;
        this.frameHeight = frameHeight;
        this.frameIndex = 0;
        this.ticksPerFrame = 8; // lower = faster animation
        this.frameTick = 0;
        this.moving = false;
      }

      update() {
        let dx = 0, dy = 0;
        if (keys.w) dy -= this.speed;
        if (keys.s) dy += this.speed;
        if (keys.a) dx -= this.speed;
        if (keys.d) dx += this.speed;

        // Apply movement and clamp to canvas bounds
        const newX = Math.max(0, Math.min(this.x + dx, this.gameWorld.width - this.width));
        const newY = Math.max(0, Math.min(this.y + dy, this.gameWorld.height - this.height));
        this.moving = (newX !== this.x) || (newY !== this.y);
        this.x = newX;
        this.y = newY;

        // Update animation frame only when moving
        if (this.moving) {
          this.frameTick++;
          if (this.frameTick >= this.ticksPerFrame) {
            this.frameTick = 0;
            this.frameIndex = (this.frameIndex + 1) % this.frameCount;
          }
        } else {
          // reset to first (idle) frame
          this.frameIndex = 0;
          this.frameTick = 0;
        }
      }

      draw(ctx) {
        if (!this.image) return;
        // source x for current frame
        const sx = this.frameIndex * this.frameWidth;
        const sy = 0;
        const sWidth = this.frameWidth;
        const sHeight = this.frameHeight;
        ctx.drawImage(this.image, sx, sy, sWidth, sHeight, this.x, this.y, this.width, this.height);
      }
    }

    // Game world
    class GameWorld {
      constructor(backgroundImg, spriteImg) {
        this.canvas = document.getElementById('world');
        this.ctx = this.canvas.getContext('2d');
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.canvas.width = this.width;
        this.canvas.height = this.height;
        this.canvas.style.position = 'absolute';
        this.canvas.style.left = '0px';
        this.canvas.style.top = '0px';

        // Only a single player sprite
        this.gameObjects = [
          new Background(backgroundImg, this),
          new Player(spriteImg, this, 150, Math.floor(this.height / 2) - 60)
        ];
      }
      gameLoop() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        for (const obj of this.gameObjects) { obj.update(); obj.draw(this.ctx); }
        requestAnimationFrame(this.gameLoop.bind(this));
      }
      start() { this.gameLoop(); }
    }

    const world = new GameWorld(backgroundImg, spriteImg);
    world.start();
  }
</script>
