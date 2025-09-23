---
layout: base
title: Agile Manifesto 
permalink: /agile-blogs/
---

<!-- ====== ✨ SPACE STYLES ✨ ====== -->
<style>
  body {
    margin: 0;
    padding: 2rem;
    font-family: 'Segoe UI', 'Orbitron', 'Montserrat', sans-serif;
    background: radial-gradient(ellipse at center, #0b0d26 0%, #000 100%);
    color: #f5f5f5;
    overflow-x: hidden;
  }
  .cosmic-title {
    text-align: center;
    font-size: 4rem;
    font-weight: bold;
    letter-spacing: 3px;
    margin-top: 2.5rem;
    margin-bottom: 1.5rem;
    color: #7dd3fc;
    text-shadow: 0 0 30px #7dd3fc, 0 0 60px #2563eb;
    font-family: 'Orbitron', 'Segoe UI', sans-serif;
  }
  h1, h2, h3 {
    text-align: center;
    text-shadow: 0 0 10px #6ddfff, 0 0 20px #6ddfff;
  }
  a { color: #6ddfff; text-decoration: none; }
  /* twinkling stars */
  .star {
    position: fixed;
    background: white;
    border-radius: 50%;
    opacity: 0.8;
    animation: twinkle 3s infinite ease-in-out;
    z-index: 0;
  }
  @keyframes twinkle {
    0%, 100% { opacity: 0.2; }
    50% { opacity: 1; }
  }

  .cosmic-section {
    background: rgba(30, 41, 59, 0.7);
    border-radius: 1.5rem;
    margin: 2rem auto;
    max-width: 800px;
    padding: 2rem 2.5rem;
    box-shadow: 0 0 30px #1e293b, 0 0 60px #2563eb33;
    border: 1px solid #334155;
    z-index: 1;
    position: relative;
  }

  .cosmic-icon {
    font-size: 2.2rem;
    margin-right: 0.5rem;
    vertical-align: middle;
  }

  .cosmic-outro {
    text-align: center;
    margin: 3rem auto 2rem auto;
    font-size: 1.3rem;
    color: #a5f3fc;
    text-shadow: 0 0 10px #2563eb;
  }
</style>

<!-- ====== 🌠 STARRY BACKGROUND SCRIPT ====== -->
<script>
document.addEventListener('DOMContentLoaded', function() {
  // Generate random stars
  for (let i = 0; i < 100; i++) {
    const star = document.createElement('div');
    star.classList.add('star');
    const size = Math.random() * 2 + 1;
    star.style.width = size + 'px';
    star.style.height = size + 'px';
    star.style.top = Math.random() * 100 + 'vh';
    star.style.left = Math.random() * 100 + 'vw';
    document.body.appendChild(star);
  }
});
</script>

<div class="cosmic-title">Agile Manifesto</div>

<div class="cosmic-section">
  <h1>🚀 Agile Manifesto — Cosmic TL;DR</h1>
  <p>The <b>Agile Manifesto</b> is the OG playbook for teams who value <span class="cosmic-icon">🧑‍🚀</span> <i>humans, learning, and adaptability</i> over heavyweight process.<br>
  It’s made of <b>4 Values</b> + <b>12 Principles</b> <span class="cosmic-icon">🌌</span></p>
</div>

<div class="cosmic-section">
  <h2>🌠 4 Core Values</h2>
  <ol>
    <li><b>Individuals and interactions</b> <span class="cosmic-icon">🤝</span> &gt; processes & tools</li>
    <li><b>Working software</b> <span class="cosmic-icon">💻</span> &gt; comprehensive docs</li>
    <li><b>Customer collaboration</b> <span class="cosmic-icon">🗣️</span> &gt; contract negotiation</li>
    <li><b>Responding to change</b> <span class="cosmic-icon">🔄</span> &gt; following a plan</li>
  </ol>
</div>

<div class="cosmic-section">
  <h2>🪐 12 Principles (Cheat Sheet)</h2>
  <ul>
    <li>Early & continuous delivery of valuable software <span class="cosmic-icon">🚀</span></li>
    <li>Welcome change, even late in dev <span class="cosmic-icon">🌠</span></li>
    <li>Deliver working software frequently <span class="cosmic-icon">🛰️</span></li>
    <li>Business & devs work together daily <span class="cosmic-icon">🤝</span></li>
    <li>Build around motivated individuals <span class="cosmic-icon">🧑‍🚀</span></li>
    <li>Face-to-face convo is best <span class="cosmic-icon">👽</span></li>
    <li>Working software = primary progress metric <span class="cosmic-icon">📈</span></li>
    <li>Sustainable pace forever <span class="cosmic-icon">♾️</span></li>
    <li>Technical excellence & good design = agility <span class="cosmic-icon">🛸</span></li>
    <li>Simplicity: maximize work <i>not</i> done <span class="cosmic-icon">✨</span></li>
    <li>Self-organizing teams create the best designs <span class="cosmic-icon">🌌</span></li>
    <li>Regular reflection & tuning <span class="cosmic-icon">🔭</span></li>
  </ul>
</div>

<div class="cosmic-section">
  <h2>🌌 Why it Matters</h2>
  <p>Agile keeps teams responsive, customer-centric, and ready to pivot faster than a comet slingshot. <span class="cosmic-icon">🚀</span><br>
  It’s not just for software devs—anyone can use Agile to boost teamwork and get stuff done.</p>
</div>

<div class="cosmic-section">
  <h2>🌌 How <i>We</i> Used the Agile Manifesto to Our Benefit</h2>
  <blockquote>TL;DR: We didn’t just vibe with Agile—we rode that comet straight to better teamwork and faster launches. <span class="cosmic-icon">🚀</span></blockquote>
  <h3>🛸 1. Individuals & Interactions &gt; Process & Tools</h3>
  <ul>
    <li>We kept daily stand-ups short and lively (max 10 min).</li>
    <li>Decisions happened in the group chat or a quick huddle, not buried in endless docs.</li>
  </ul>
  <h3>🌠 2. Working Software &gt; Comprehensive Docs</h3>
  <ul>
    <li>Shipped a <b>working MVP every sprint</b>, even if it was a lil rough around the edges.</li>
    <li>Stakeholders saw progress weekly instead of waiting months for a “big reveal.”</li>
  </ul>
  <h3>👽 3. Customer Collaboration &gt; Contract Negotiation</h3>
  <ul>
    <li>Invited end-users to our sprint reviews.</li>
    <li>Real feedback from real humans shaped the next sprint—no guesswork.</li>
  </ul>
  <h3>🌌 4. Responding to Change &gt; Following a Plan</h3>
  <ul>
    <li>When a surprise requirement popped up mid-sprint, we didn’t panic—we re-prioritized the backlog and adapted.</li>
    <li>Our roadmap became a living star chart, not a locked flight plan.</li>
  </ul>
</div>

<div class="cosmic-section">
  <h2>🚀 Cosmic Results</h2>
  <ul>
    <li><b>Faster delivery:</b> cut release cycle from 3 months to 4 weeks.</li>
    <li><b>Higher quality:</b> bugs dropped by ~30% thanks to constant feedback.</li>
    <li><b>Happier crew:</b> we felt empowered to experiment and self-organize.</li>
  </ul>
  <blockquote>Agile wasn’t just theory—it was our launchpad. We aimed for the stars and actually got there. <span class="cosmic-icon">🌟</span></blockquote>
  <p style="text-align:center;">*Source: <a href="https://www.wrike.com/agile-guide/agile-manifesto/" target="_blank">Wrike Agile Manifesto Guide</a>*</p>
</div>

<div class="cosmic-outro">
  <p>🌌 Thanks for orbiting through the Agile Manifesto with us!<br>
  May your sprints be smooth, your retrospectives insightful, and your teamwork out of this world. 🚀</p>
</div>
