---
layout: base
title: "🌠 LxD Plan — Interstellar Edition"
permalink: /lxd-plan
description: "All of my LxD plan wrapped in a star-filled sky with a rocket cursor."
---

<!-- === CSS === -->
<style>
/* ----- Starry Night Background ----- */
body {
  margin: 0;
  background: #000;
  color: #e0e6f8;
  font-family: "Trebuchet MS", sans-serif;
  overflow-x: hidden;
}

/* Twinkling stars canvas overlay */
#star-canvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: -1;
}

/* create layers of twinkling stars */
body::before, body::after {
  content: "";
  position: fixed;
  top: 0; left: 0;
  width: 200%; height: 200%;
  background: transparent url('https://raw.githubusercontent.com/andrewnakas/space-assets/main/stars.png') repeat;
  animation: moveStars 100s linear infinite;
  z-index: -2;
}
body::after {
  background-size: 50%;
  opacity: 0.6;
  animation-duration: 200s;
}

@keyframes moveStars {
  from {transform: translateY(0);}
  to   {transform: translateY(-1000px);}
}

/* ----- Headings ----- */
h1, h2, h3 {
  text-align: center;
  color: #a8d8ff;
  text-shadow: 0 0 10px #5dd0ff;
}

/* ----- Glowing Buttons ----- */
.space-btn {
  display: inline-block;
  margin: 12px;
  padding: 12px 24px;
  border-radius: 30px;
  text-decoration: none;
  background: rgba(28,37,65,0.6);
  color: #e0e6f8;
  border: 2px solid #5dd0ff;
  box-shadow: 0 0 15px #5dd0ff;
  transition: all 0.3s ease;
}
.space-btn:hover {
  background: #5dd0ff;
  color: #0d1b2a;
  box-shadow: 0 0 25px #5dd0ff;
}

/* ----- Section Cards ----- */
.star-card {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(93,208,255,0.4);
  border-radius: 20px;
  padding: 1.2em;
  margin: 2em auto;
  max-width: 750px;
  backdrop-filter: blur(4px);
}

/* ----- Rocket Cursor Follower ----- */
#rocket {
  position: absolute;
  width: 60px;
  height: 60px;
  pointer-events: none;
  left: 50vw;
  top: 50vh;
  z-index: 9999;
}
</style>


<!-- Twinkling Stars Canvas -->
<canvas id="star-canvas" style="position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:-1;"></canvas>


<!-- ====== Inline Rocket SVG (no image needed) ====== -->
<svg id="rocket" viewBox="0 0 64 64" style="position:absolute;width:60px;height:60px;pointer-events:none;left:50vw;top:50vh;z-index:9999;">
  <path fill="#ccc" d="M32 0C24 10 22 24 24 38l-6 8 8-4 4 10 4-10 8 4-6-8c2-14 0-28-8-38z"/>
  <path fill="orange" d="M28 56l4 8 4-8z"/>
</svg>

<!-- === JS === -->

<!-- Place canvas and script at the end of the body for reliability -->
<script>
// Make rocket cursor follow mouse smoothly (closer, but not instant)
const rocket = document.getElementById('rocket');
let targetX = window.innerWidth / 2;
let targetY = window.innerHeight / 2;
let currentX = targetX;
let currentY = targetY;

document.addEventListener('mousemove', function(e) {
  targetX = e.clientX;
  targetY = e.clientY;
});

function animateRocket() {
  currentX += (targetX - currentX) * 0.25;
  currentY += (targetY - currentY) * 0.25;
  rocket.style.left = currentX + 'px';
  rocket.style.top = currentY + 'px';
  requestAnimationFrame(animateRocket);
}
animateRocket();

// Twinkling stars canvas animation
window.addEventListener('DOMContentLoaded', function() {
  const starCanvas = document.getElementById('star-canvas');
  const ctx = starCanvas.getContext('2d');
  let stars = [];
  const STAR_COUNT = 200;
  function resizeCanvas() {
    starCanvas.width = window.innerWidth;
    starCanvas.height = window.innerHeight;
    starCanvas.style.width = '100vw';
    starCanvas.style.height = '100vh';
  }
  resizeCanvas();
  window.addEventListener('resize', () => {
    resizeCanvas();
    createStars();
  });

  function randomBetween(a, b) {
    return a + Math.random() * (b - a);
  }

  function createStars() {
    stars = [];
    for (let i = 0; i < STAR_COUNT; i++) {
      stars.push({
        x: Math.random() * starCanvas.width,
        y: Math.random() * starCanvas.height,
        r: randomBetween(1.2, 2.8),
        baseAlpha: randomBetween(0.7, 1),
        twinkleSpeed: randomBetween(0.01, 0.035),
        twinklePhase: Math.random() * Math.PI * 2
      });
    }
  }
  createStars();

  function drawStars() {
    ctx.clearRect(0, 0, starCanvas.width, starCanvas.height);
    let t = Date.now() * 0.002;
    for (let star of stars) {
      let twinkle = Math.sin(t * 2 + star.twinklePhase) * 0.5 + 0.5;
      let alpha = star.baseAlpha * (0.8 + 0.8 * twinkle);
      ctx.globalAlpha = alpha;
      ctx.beginPath();
      ctx.arc(star.x, star.y, star.r, 0, Math.PI * 2);
      ctx.fillStyle = '#fff';
      ctx.shadowColor = '#a8d8ff';
      ctx.shadowBlur = 16;
      ctx.fill();
      ctx.shadowBlur = 0;
    }
    ctx.globalAlpha = 1;
    requestAnimationFrame(drawStars);
  }
  drawStars();
});
</script>

# 🌌 Mission Control — LxD Plan

Ready for launch! This page charts every stop on the LxD journey.

---

## 🛰 Quick Jump Gates
<a class="space-btn" href="https://pages.opencodingsociety.com/github/pages/jokes">Jokes</a>
<a class="space-btn" href="https://pages.opencodingsociety.com/github/pages/anatomy">Anatomy</a>
<a class="space-btn" href="https://pages.opencodingsociety.com/github/pages/theme">Theme</a>
<a class="space-btn" href="https://pages.opencodingsociety.com/github/pages/markdown">Markdown</a>
<a class="space-btn" href="https://pages.opencodingsociety.com/github/pages/jekyll">Jekyll</a>
<a class="space-btn" href="https://pages.opencodingsociety.com/github/pages/hacks">Hacks</a>

---

> ### 🌠 1. Jokes  
> Fun JS jokes inside Jupyter notebooks—practice running JavaScript cells and moving files around GitHub Pages.  
> [Blast off →](https://pages.opencodingsociety.com/github/pages/jokes)

> ### 🪐 2. Anatomy  
> Map of your repo universe: `_posts`, `_layouts`, `_config.yml`—learn how Jekyll assembles sites from stardust.  
> [Orbit here →](https://pages.opencodingsociety.com/github/pages/anatomy)

> ### 🌌 3. Theme  
> Swap constellations (themes) with Makefile spells like `make use-minima` and override layouts locally.  
> [Dock here →](https://pages.opencodingsociety.com/github/pages/theme)

> ### ✍️ 4. Markdown  
> Markdown is your star chart—mix HTML, CSS, and images to design planets of content.  
> [Launch pad →](https://pages.opencodingsociety.com/github/pages/markdown)

> ### 🔧 5. Jekyll  
> Master Liquid templates and loops to auto-generate blog universes.  
> [Hyperjump →](https://pages.opencodingsociety.com/github/pages/jekyll)

> ### 🚀 6. Hacks  
> Apply everything: custom nav, JS in notebooks, Utterances comments—turn theory into a working interstellar station.  
> [Warp speed →](https://pages.opencodingsociety.com/github/pages/hacks)

---

## 🚗 Our LxD Design Process: Plan A, Plan B, and Teamwork

For our LxD (Learning Experience Design) project, we focused on planning, creativity, and collaboration:

- **Plan A & Plan B:**
  - We always made a primary plan (Plan A) and a backup plan (Plan B) to stay flexible and ready for any challenges.

- **Background Animation Hack:**
  - Using the `background.md` hack, we created a scene with a car passing by on a street. Above the animation, we placed different buttons to represent the steps of an LxD designer. Each button highlights a key phase, making the process interactive and visual.

- **Tracking Our Work:**
  - To stay organized, we documented everything in multiple blogs and GitHub issues. This helped us keep track of progress, ideas, and feedback.

- **Team Roles:**
  - We assigned one Scrum Master to lead the process, one Scrum Assistant to help coordinate, and the rest of the team as dedicated workers. This structure kept our workflow smooth and everyone engaged.

This approach helped us visualize the LxD journey, adapt to changes, and work efficiently as a team!

---

### 🌟 Launch Checklist
1. Fork/clone the repo.  
2. Drop this file in as `index.md`.  
3. Commit & push to GitHub Pages.  
4. Watch the stars twinkle and the rocket chase your cursor. ✨
