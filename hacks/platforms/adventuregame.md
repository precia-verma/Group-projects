---
layout: base
title: Background with Object 
description: Use Javascript to have an in motion
sprite: images/platformer/sprites/gravestone_1.png
background: images/platformer/backgrounds/spookyforestforgame.png
permalink: /spookyforest
---

<<!-- Spooky Forest Game (embed version for GitHub Pages layout) -->

<h1 id="gameTitle" style="
  color: white;
  text-align: center;
  position: absolute;
  width: 100%;
  top: 20px;
  margin: 0;
  font-family: system-ui, sans-serif;
  z-index: 10;
  pointer-events: none;">
  Spooky Forest
</h1>

<!-- Buttons -->
<button id="startButton" style="
  font-size: 28px;
  padding: 12px 28px;
  background: red;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: 11;
  transition: opacity 0.8s ease;">
  Start Game
</button>

<button id="playAgainButton" style="
  font-size: 22px;
  padding: 10px 22px;
  background: #333;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  position: absolute;
  left: 50%;
  bottom: 40px;
  transform: translateX(-50%);
  display: none;
  z-index: 11;">
  Play Again
</button>

<!-- Fullscreen Canvas -->
<canvas id="world" style="
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: #0b0f14;
  margin: 0;
  border: none;
  z-index: 1;"></canvas>

<script>
const startButton = document.getElementById('startButton');
const playAgainButton = document.getElementById('playAgainButton');
const canvas = document.getElementById('world');
const ctx = canvas.getContext('2d');

function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

startButton.addEventListener('click', () => {
  startButton.style.opacity = '0';
  startButton.style.pointerEvents = 'none';
  setTimeout(() => {
    startButton.style.display = 'none';
    startGame();
  }, 800);
});

function startGame() {
  resizeCanvas();
  const bg = new Image(), s1=new Image(), s2=new Image(), s3=new Image(), s4=new Image(), s5=new Image(), s6=new Image();
  bg.src="images/platformer/backgrounds/spookyforestforgame.png";
  s1.src="images/platformer/sprites/gravestone_1.png";
  s2.src="images/platformer/sprites/gravestone_2.png";
  s3.src="images/platformer/sprites/gravestone_3.png";
  s4.src="images/platformer/sprites/gravestone_4.png";
  s5.src="images/platformer/sprites/gravestone_5.png";
  s6.src="images/platformer/sprites/gravestone_6.png";

  let loaded=0; const total=7;
  const onLoad=()=>{if(++loaded===total) startGameWorld();};
  [bg,s1,s2,s3,s4,s5,s6].forEach(i=>i.onload=onLoad);

  function startGameWorld(){
    let audioCtx=null, masterGain=null;
    const NOTE_FREQ={"e4":329.63,"g4":392,"d#4":311.13,"f#4":369.99,"c4":261.63,"f4":349.23,"c#4":277.18,"a3":220};
    const GRAVE_TO_NOTE={1:"e4",2:"g4",3:"d#4",4:"f#4",5:"c4",6:"f4"};
    const SUCCESS_NOTE="c#4", FAIL_NOTE="a3";
    function initAudio(){if(audioCtx)return;audioCtx=new(window.AudioContext||window.webkitAudioContext)();masterGain=audioCtx.createGain();masterGain.gain.value=.6;masterGain.connect(audioCtx.destination);}
    function playNote(note,ms=500,type="sine"){if(!audioCtx||!NOTE_FREQ[note])return;const now=audioCtx.currentTime;const osc=audioCtx.createOscillator();const g=audioCtx.createGain();osc.type=type;osc.frequency.value=NOTE_FREQ[note];g.gain.setValueAtTime(.0001,now);g.gain.exponentialRampToValueAtTime(1,now+.01);g.gain.exponentialRampToValueAtTime(.0001,now+ms/1000-.02);osc.connect(g);g.connect(masterGain);osc.start(now);osc.stop(now+ms/1000);}

    class Player {
      constructor(image,x,y,id,note){this.image=image;this.id=id;this.note=note;this.x=x;this.y=y;this.w=image.width/2;this.h=image.height/2;this.glowUntil=0;this.errorUntil=0;}
      glow(ms=500){this.glowUntil=performance.now()+ms;}
      flashError(ms=600){this.errorUntil=performance.now()+ms;}
      contains(px,py){return(px>=this.x&&px<=this.x+this.w&&py>=this.y&&py<=this.y+this.h);}
      draw(ctx){const now=performance.now();if(now<this.errorUntil){ctx.save();ctx.shadowColor="rgba(255,0,0,.95)";ctx.shadowBlur=18;ctx.drawImage(this.image,this.x,this.y,this.w,this.h);ctx.globalCompositeOperation="multiply";ctx.globalAlpha=.25;ctx.fillStyle="red";ctx.fillRect(this.x,this.y,this.w,this.h);ctx.restore();return;}
        if(now<this.glowUntil){ctx.save();ctx.shadowColor="rgba(0,255,255,.9)";ctx.shadowBlur=10;ctx.drawImage(this.image,this.x,this.y,this.w,this.h);ctx.globalCompositeOperation="screen";ctx.globalAlpha=.18;ctx.fillStyle="#aaf";ctx.fillRect(this.x,this.y,this.w,this.h);ctx.restore();return;}
        ctx.drawImage(this.image,this.x,this.y,this.w,this.h);}
    }

    class World {
      constructor(){
        this.width=canvas.width;this.height=canvas.height;
        const y=this.height/2-60, spacing=this.width/8;
        this.players=[new Player(s1,spacing*1.5,y,1,GRAVE_TO_NOTE[1]),new Player(s2,spacing*2.5,y,2,GRAVE_TO_NOTE[2]),new Player(s3,spacing*3.5,y,3,GRAVE_TO_NOTE[3]),new Player(s4,spacing*4.5,y,4,GRAVE_TO_NOTE[4]),new Player(s5,spacing*5.5,y,5,GRAVE_TO_NOTE[5]),new Player(s6,spacing*6.5,y,6,GRAVE_TO_NOTE[6])];
        this.seq=[2,4,1,6,3,5];this.round=1;this.i=0;this.accept=false;this.audio=false;this.error=false;this.msg="";
        canvas.addEventListener('click',async ev=>{
          const r=canvas.getBoundingClientRect(),x=ev.clientX-r.left,y=ev.clientY-r.top;
          if(!this.audio){initAudio();this.audio=true;this.round=1;this.msg="";await this.playRound();return;}
          if(this.error||!this.accept)return;
          const hit=this.players.find(p=>p.contains(x,y));if(!hit)return;
          hit.glow(420);playNote(hit.note,420);
          const expect=this.seq[this.i];
          if(hit.id===expect){this.i++;if(this.i===this.round){this.accept=false;if(this.round===this.seq.length){playNote(SUCCESS_NOTE,160);await this.sleep(150);playNote(SUCCESS_NOTE,200);await this.sleep(190);playNote(SUCCESS_NOTE,240);this.msg="You won! 🎉";playAgainButton.style.display="block";return;}this.round++;await this.sleep(400);await this.playRound();}}else await this.fail();});
        playAgainButton.onclick=async()=>{playAgainButton.style.display="none";this.reset();await this.playRound();};
      }
      reset(){this.round=1;this.i=0;this.accept=false;this.error=false;this.msg="";}
      sleep(ms){return new Promise(r=>setTimeout(r,ms));}
      async fail(){this.accept=false;this.error=true;this.msg="Wrong gravestone! Try again.";this.players.forEach(p=>p.flashError(650));playNote(FAIL_NOTE,180);await this.sleep(100);playNote(FAIL_NOTE,220);await this.sleep(500);playAgainButton.style.display="block";}
      async flashAndPlay(id,ms=620){const p=this.players.find(pl=>pl.id===id);if(!p)return;p.glow(ms-60);playNote(p.note,ms-80);await this.sleep(ms);}
      async playRound(){this.error=false;this.accept=false;this.i=0;this.msg=`Listen and repeat (Round ${this.round})`;await this.sleep(300);for(let i=0;i<this.round;i++){await this.flashAndPlay(this.seq[i],620);await this.sleep(180);}this.msg="Your turn!";this.accept=true;}
      drawHUD(){ctx.save();ctx.fillStyle="white";ctx.font="16px system-ui";ctx.fillText(this.audio?`Round ${this.round}/${this.seq.length}`:"Click the canvas to start sound",20,40);if(this.msg){ctx.font="20px system-ui";ctx.fillText(this.msg,20,70);}ctx.restore();}
      loop(){ctx.clearRect(0,0,canvas.width,canvas.height);ctx.drawImage(bg,0,0,canvas.width,canvas.height);this.players.forEach(p=>p.draw(ctx));this.drawHUD();requestAnimationFrame(()=>this.loop());}
      start(){this.loop();}
    }
    const w=new World();w.start();
  }
}
</script>

