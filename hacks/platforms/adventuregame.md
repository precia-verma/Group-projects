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
  
  window.onload = function() {}

 
  const canvas = document.getElementById("world");
  const ctx = canvas.getContext('2d');

  // Images
  const backgroundImg = new Image();
  const spriteImg = new Image();
  backgroundImg.src = 'images/platformer/backgrounds/spookyforestforgame.png';
  spriteImg.src      = 'images/platformer/sprites/gravestone_1.png';

  // The other 5 gravestones
  const sprite2Img = new Image(); sprite2Img.src = 'images/platformer/sprites/gravestone_2.png';
  const sprite3Img = new Image(); sprite3Img.src = 'images/platformer/sprites/gravestone_3.png';
  const sprite4Img = new Image(); sprite4Img.src = 'images/platformer/sprites/gravestone_4.png';
  const sprite5Img = new Image(); sprite5Img.src = 'images/platformer/sprites/gravestone_5.png';
  const sprite6Img = new Image(); sprite6Img.src = 'images/platformer/sprites/gravestone_6.png';

  // Wait for background + first sprite (enough to size/draw); others can stream in
  let imagesLoaded = 0;
  backgroundImg.onload = () => { imagesLoaded++; startGameWorld(); };
  spriteImg.onload     = () => { imagesLoaded++; startGameWorld(); };

  function startGameWorld() {
    if (imagesLoaded < 2) return; // only start once both are ready

  
    let audioCtx = null;
    let masterGain = null;

   
    const NOTE_FREQ = {
      "e4": 329.63, "g4": 392.00, "d#4": 311.13,
      "f#4": 369.99, "c4": 261.63, "f4": 349.23, "c#4": 277.18, "a3": 220.00 
    };
    
    const GRAVE_TO_NOTE = { 1:"e4", 2:"g4", 3:"d#4", 4:"f#4", 5:"c4", 6:"f4" };
    const SUCCESS_NOTE  = "c#4";
    const FAIL_NOTE = "a3";

    function initAudio() {
      if (audioCtx) return; 
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      masterGain = audioCtx.createGain();
      masterGain.gain.value = 0.6; 
      masterGain.connect(audioCtx.destination);
    }

    
    function playNote(noteName, ms = 500) {
      if (!audioCtx || !NOTE_FREQ[noteName]) return;
      const now = audioCtx.currentTime;

      const osc = audioCtx.createOscillator();
      osc.type = "sine";
      osc.frequency.value = NOTE_FREQ[noteName];

      const gain = audioCtx.createGain();
     
      gain.gain.setValueAtTime(0.0001, now);
      gain.gain.exponentialRampToValueAtTime(1.0, now + 0.01);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + ms/1000 - 0.02);

      osc.connect(gain);
      gain.connect(masterGain);

      osc.start(now);
      osc.stop(now + ms/1000);
    }

    class GameObject {
      constructor(image, width, height, x = 0, y = 0, speedRatio = 0) {
        this.image = image;
        this.width = width;
        this.height = height;
        this.x = x;
        this.y = y;
        this.speedRatio = speedRatio;
        this.speed = GameWorld.gameSpeed * this.speedRatio;
      }
      update() {}
      draw(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
      }
    }

    class Background extends GameObject {
      constructor(image, gameWorld) {
        super(image, gameWorld.width, gameWorld.height, 0, 0, 0);
      }
      update() {
        this.x = (this.x - this.speed) % this.width; 
      }
      draw(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
        ctx.drawImage(this.image, this.x + this.width, this.y, this.width, this.height);
      }
    }

 
    class Player extends GameObject {
      constructor(image, gameWorld, customX, customY, id, note) {
        const width  = image.naturalWidth  / 2;
        const height = image.naturalHeight / 2;
        const x = (customX !== undefined) ? customX : (gameWorld.width  - width ) / 2;
        const y = (customY !== undefined) ? customY : (gameWorld.height - height) / 2;
        super(image, width, height, x, y);
        this.id = id;
        this.note = note;        
        this.glowUntil = 0;       
      }
     
      glow(ms = 500) {
        this.glowUntil = performance.now() + ms;
      }
      
      containsPoint(px, py) {
        return (px >= this.x && px <= this.x + this.width &&
                py >= this.y && py <= this.y + this.height);
      }
      draw(ctx) {
        const now = performance.now();
        if (now < this.glowUntil) {
          
          ctx.save();
          ctx.shadowColor = "rgba(0, 255, 255, 0.9)";
          ctx.shadowBlur = 22;
          ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
          ctx.restore();

          ctx.save();
          ctx.globalCompositeOperation = "screen";
          ctx.globalAlpha = 0.18;
          ctx.fillStyle = "#aaf";
          ctx.fillRect(this.x, this.y, this.width, this.height);
          ctx.restore();
        } else {
          super.draw(ctx);
        }
      }
    }

    class GameWorld {
  static gameSpeed = 5;

  constructor(backgroundImg, spriteImg) {
    // canvas sizing
    this.canvas = document.getElementById("world");
    this.ctx = this.canvas.getContext('2d');
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.canvas.width  = this.width;
    this.canvas.height = this.height;
    this.canvas.style.width  = `${this.width}px`;
    this.canvas.style.height = `${this.height}px`;
    this.canvas.style.position = 'absolute';
    this.canvas.style.left = `0px`;
    this.canvas.style.top  = `${(window.innerHeight - this.height) / 2}px`;

    
    this.players = [
      new Player(spriteImg,  this, 150, this.height / 2 - 60, 1, GRAVE_TO_NOTE[1]),
      new Player(sprite2Img, this, 330, this.height / 2 - 60, 2, GRAVE_TO_NOTE[2]),
      new Player(sprite3Img, this, 496, this.height / 2 - 60, 3, GRAVE_TO_NOTE[3]),
      new Player(sprite4Img, this, 670, this.height / 2 - 60, 4, GRAVE_TO_NOTE[4]),
      new Player(sprite5Img, this, 835, this.height / 2 - 60, 5, GRAVE_TO_NOTE[5]),
      new Player(sprite6Img, this, 999, this.height / 2 - 60, 6, GRAVE_TO_NOTE[6])
    ];

    this.gameObjects = [
      new Background(backgroundImg, this),
      ...this.players
    ];

    
    this.sequence = [2, 4, 1, 6, 3, 5];
    this.acceptingInput = false;
    this.inputIndex = 0;
    this.audioUnlocked = false; 

    
    this.canvas.addEventListener('click', async (ev) => {
      const rect = this.canvas.getBoundingClientRect();
      const x = ev.clientX - rect.left;
      const y = ev.clientY - rect.top;

      
      if (!this.audioUnlocked) {
        initAudio();
        this.audioUnlocked = true;

        // tiny “start” ping before the pattern
        // playNote(SUCCESS_NOTE, 140);
        // await this.sleep(120);

        await this.playSequence();
        return;
      }

      if (!this.acceptingInput) return;

      const hit = this.players.find(p => p.containsPoint(x, y));
      if (!hit) return;

      hit.glow(420);
      playNote(hit.note, 420);

      const expectedId = this.sequence[this.inputIndex];
      if (hit.id === expectedId) {
        this.inputIndex++;
        if (this.inputIndex === this.sequence.length) {
          this.acceptingInput = false;
          // success jingle
          playNote(SUCCESS_NOTE, 160);
          await this.sleep(150);
          playNote(SUCCESS_NOTE, 200);
          await this.sleep(190);
          playNote(SUCCESS_NOTE, 240);
        }
      } else {
        // wrong answer → use your FAIL_NOTE here
        this.acceptingInput = false;
        playNote(FAIL_NOTE, 180);
        await this.sleep(90);
        playNote(FAIL_NOTE, 220);
        // click again to replay
      }
    });
  }

  sleep(ms) { return new Promise(res => setTimeout(res, ms)); }
  async flashAndPlayById(id, ms = 620) {
    const p = this.players.find(pl => pl.id === id);
    if (!p) return;
    p.glow(ms - 60);
    playNote(p.note, ms - 80);
    await this.sleep(ms);
  }
  async playSequence() {
    this.acceptingInput = false;
    this.inputIndex = 0;
    await this.sleep(300);
    for (const id of this.sequence) {
      await this.flashAndPlayById(id, 620);
      await this.sleep(180);
    }
    this.acceptingInput = true;
  }
  gameLoop() {
    this.ctx.clearRect(0, 0, this.width, this.height);
    for (const obj of this.gameObjects) {
      obj.update();
      obj.draw(this.ctx);
    }
    requestAnimationFrame(this.gameLoop.bind(this));
  }
  start() { this.gameLoop(); }
}
