---
layout: base
title: Blogs 
permalink: /homepage-blogs/
---

<style>
  /* ===== Cosmic Base ===== */
  body {
    margin: 0;
    padding: 0;
    height: 100vh;
    background: radial-gradient(ellipse at center, #0a0f2c 0%, #000000 100%);
    color: #fff;
    font-family: 'Orbitron', sans-serif;
    text-align: center;
    overflow: hidden;
  }

  h1 {
    font-size: 4.5rem;
    margin-top: 2rem;
    letter-spacing: 3px;
    text-shadow: 0 0 30px #7dd3fc, 0 0 60px #2563eb;
  }

  p.description {
    font-size: 1.3rem;
    margin: 1rem auto 3rem;
    max-width: 650px;
    line-height: 1.8;
    color: #cbd5e1;
    text-shadow: 0 0 8px #1e293b;
  }

  /* ===== Star Layers ===== */
  .star {
    position: fixed;
    border-radius: 50%;
    background: white;
    opacity: 0.8;
    animation: twinkle 3s infinite alternate;
  }
  @keyframes twinkle {
    0% {opacity: 0.3;}
    100% {opacity: 1;}
  }

  /* Different sizes + speeds for depth */
  .layer1 .star { width: 1px; height: 1px; animation-duration: 2s; }
  .layer2 .star { width: 2px; height: 2px; animation-duration: 3.5s; }
  .layer3 .star { width: 3px; height: 3px; animation-duration: 5s; }

  /* ===== Floating Nebula Glow ===== */
  .nebula {
    position: fixed;
    width: 60vw;
    height: 60vw;
    background: radial-gradient(circle, rgba(56,189,248,0.25) 0%, rgba(56,189,248,0) 70%);
    top: 20%;
    left: 10%;
    filter: blur(80px);
    animation: drift 40s infinite alternate ease-in-out;
    pointer-events: none;
  }
  @keyframes drift {
    from {transform: translate(0,0) rotate(0deg);}
    to   {transform: translate(10%, -10%) rotate(360deg);}
  }

  /* ===== Space Buttons ===== */
  .button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 4rem;
    width: 100%;
    max-width: 1100px;
    margin-left: auto;
    margin-right: auto;
    box-sizing: border-box;
  }
  .space-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    flex: 1 1 280px;
    min-width: 220px;
    max-width: 380px;
    box-sizing: border-box;
    background: linear-gradient(45deg, #3b82f6, #9333ea);
    color: #fff;
    padding: 1.5rem 2.8rem;
    border-radius: 9999px;
    text-decoration: none;
    font-weight: bold;
    letter-spacing: 1px;
    transition: all 0.3s ease;
    box-shadow: 0 0 20px #6366f1, 0 0 40px #9333ea inset;
    font-size: 1.45rem;
    text-align: center;
    height: 80px;
  }
  .space-btn:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 0 25px #a78bfa, 0 0 60px #9333ea inset;
  }
</style>

<!-- Star layers & nebula -->
<div class="nebula"></div>
<div id="layer1" class="layer1"></div>
<div id="layer2" class="layer2"></div>
<div id="layer3" class="layer3"></div>

<script>
  // helper to sprinkle stars
  function makeStars(layerId, count) {
    const layer = document.getElementById(layerId);
    for (let i = 0; i < count; i++) {
      const s = document.createElement('div');
      s.className = 'star';
      s.style.top  = Math.random() * 100 + 'vh';
      s.style.left = Math.random() * 100 + 'vw';
      s.style.animationDelay = (Math.random() * 3) + 's';
      layer.appendChild(s);
    }
  }
  makeStars('layer1', 80);  // tiny, fast
  makeStars('layer2', 60);  // medium
  makeStars('layer3', 40);  // big, slow
</script>

# 🌠 Blogs

<p class="description">
  <b>This is our Blogs Homepage! We have listed everything you may need to know in a very fun way! Have lots of fun!</b>
</p>

<div class="button-container">
  <a class="space-btn" href="https://precia-verma.github.io/Group-projects/agile-blogs/" target="_blank">🚀 Agile Manifesto</a>
  <a class="space-btn" href="https://precia-verma.github.io/Group-projects/ruby-gems-installation-shop/" target="_blank">🪐 Gem Shop</a>
  <a class="space-btn" href="https://precia-verma.github.io/Group-projects/python-installation-shop/" target="_blank">☄️ Pet Shop</a>
  <a class="space-btn" href="https://precia-verma.github.io/Group-projects/homebrew-installation-shop/" target="_blank">🛰️ Brew Shop</a>
  <a class="space-btn" href="https://precia-verma.github.io/Group-projects/trouble-blogs/" target="_blank">🧑‍🚀 Trouble-Shooting Guide</a>
  <a class="space-btn" href="https://precia-verma.github.io/Group-projects/cookie-clicker-blog" target="_blank">🌟 Cookie-Clicker Blog</a>
  <a class="space-btn" href="https://precia-verma.github.io/Group-projects/calculator-blog" target="_blank">✨ Calculator Blog</a>
  <a class="space-btn" href="https://precia-verma.github.io/Group-projects/tools-blogs" target="_blank">🛠️ Tools and Equipment</a>
  <a class="space-btn" href="https://precia-verma.github.io/Group-projects/retro-blogs/" target="_blank">🤝 Retrospective Blog</a>
</div>
