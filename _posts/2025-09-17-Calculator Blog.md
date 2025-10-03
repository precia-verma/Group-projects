---
layout: base
title: Calculator Blog
permalink: /calculator-blog
---

<style>
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
  h1, h2, h3 {
    font-size: 3rem;
    margin-top: 2rem;
    letter-spacing: 2px;
    text-shadow: 0 0 30px #7dd3fc, 0 0 60px #2563eb;
  }
  p.description {
    font-size: 1.3rem;
    margin: 1rem auto 2rem;
    max-width: 650px;
    line-height: 1.8;
    color: #cbd5e1;
    text-shadow: 0 0 8px #1e293b;
  }
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
  .layer1 .star { width: 1px; height: 1px; animation-duration: 2s; }
  .layer2 .star { width: 2px; height: 2px; animation-duration: 3.5s; }
  .layer3 .star { width: 3px; height: 3px; animation-duration: 5s; }
  .nebula {
    position: fixed;
    width: 60vw;
    height: 60vw;
    background: radial-gradient(circle, rgba(60, 196, 255, 0.25) 0%, rgba(56,189,248,0) 70%);
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
  .button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 3rem;
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
    padding: 1.2rem 2.2rem;
    border-radius: 9999px;
    text-decoration: none;
    font-weight: bold;
    letter-spacing: 1px;
    transition: all 0.3s ease;
    box-shadow: 0 0 20px #6366f1, 0 0 40px #9333ea inset;
    font-size: 1.25rem;
    text-align: center;
    height: 70px;
  }
  .space-btn:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 0 25px #a78bfa, 0 0 60px #9333ea inset;
  }
  .section {
    background: rgba(30, 41, 59, 0.7);
    border-radius: 1.5rem;
    margin: 2rem auto;
    max-width: 800px;
    padding: 2rem 2.5rem;
    box-shadow: 0 0 30px #1e293b, 0 0 60px #2563eb33;
    border: 1px solid #334155;
    text-align: left;
  }
  .section img {
    display: block;
    margin: 2rem auto;
    border-radius: 1rem;
    box-shadow: 0 0 30px #9333ea44;
    max-width: 100%;
    height: auto;
  }
  .section table {
    width: 100%;
    margin: 1.5rem 0;
    background: rgba(30,41,59,0.5);
    border-radius: 1rem;
    overflow: hidden;
    color: #fff;
  }
  .section th, .section td {
    padding: 0.7em 1em;
    border-bottom: 1px solid #334155;
    text-align: left;
  }
  .section th {
    background: #3b82f6;
    color: #fff;
    font-weight: bold;
  }
  .section code, .section pre {
    background: #0f172a;
    color: #a5f3fc;
    border-radius: 0.5rem;
    padding: 0.2em 0.5em;
    font-size: 1em;
  }
</style>

<div class="nebula"></div>
<div id="layer1" class="layer1"></div>
<div id="layer2" class="layer2"></div>
<div id="layer3" class="layer3"></div>
<script>
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
  makeStars('layer1', 80);
  makeStars('layer2', 60);
  makeStars('layer3', 40);
</script>

# ✨ Calculator Blog

<p class="description">
  <b>Welcome to The Coders' Calculator Blog! Explore our project, features, and code in a cosmic-themed, interactive way. 🚀🪐</b>
</p>

<div class="button-container">
  <a class="space-btn" href="https://precia-verma.github.io/Group-projects/calculator" target="_blank">🧮 Try the Calculator</a>
  <a class="space-btn" href="https://github.com/precia-verma" target="_blank">👩‍💻 Precia Verma GitHub</a>
  <a class="space-btn" href="https://github.com/krystal-727" target="_blank">👩‍💻 Krystal GitHub</a>
  <a class="space-btn" href="https://github.com/StutiPandey19" target="_blank">👩‍💻 Tasha (Struti) GitHub</a>
  <a class="space-btn" href="https://github.com/user-attachments/files/22397696/calculator.md" target="_blank">📓 Calculator Notebook</a>
</div>

<div class="section">
  <h2>📝 Hack 1: Notebook</h2>
  <a href="https://github.com/user-attachments/files/22397696/calculator.md" target="_blank">calculator.md</a>
</div>

<div class="section">
  <h2>🚀 Hack 2: Your Own Feature</h2>
  <h3>Feature Name: JS Calculator</h3>
  <p><b>Purpose:</b> The JS Calculator is an interactive web-based calculator built with HTML, CSS, and JavaScript. Its purpose is to help users perform basic arithmetic operations (addition, subtraction, multiplication, division) directly in the browser. The calculator features a visually appealing, right-justified display, responsive buttons for numbers and operations, and supports decimal calculations. It also includes a clear (A/C) button to reset the calculation and an equals button to compute results, making it a practical tool for learning and practicing JavaScript DOM manipulation and event handling.</p>
  <h3>Feature Name: Right-Justified Output Display</h3>
  <p><b>Purpose:</b> This feature ensures that the calculator’s result/output is always aligned to the right side of the display area, mimicking the behavior of real-world calculators. It improves readability, especially for large or decimal numbers, and provides a familiar user experience. This makes it easy for users to read and interpret results as they perform calculations.</p>
  <pre><code>display: flex;
align-items: center;
justify-content: flex-end; /* right-align text */
</code></pre>
  <h3>Feature Name: Clear (A/C) Button</h3>
  <p><b>Purpose:</b> The calculator includes an "A/C" (All Clear) button that resets the calculator to its initial state. When clicked, it sets the display back to 0 and clears any stored numbers or operations, allowing the user to start a new calculation.</p>
  <pre><code>function clearCalc () {
	firstNumber = null;
	output.innerHTML = "0";
	nextReady = true;
}
</code></pre>
</div>

<div class="section">
  <h2>🖼️ Picture of Code</h2>
  <img width="836" height="816" alt="Image" src="https://github.com/user-attachments/assets/22a2fb7a-2a1e-482f-a0a6-88956cdc6266" />
</div>

<div class="section">
  <h2>🛠️ What We Changed and Why</h2>
  <ul>
    <li><b>Modernized the Calculator UI:</b> Used CSS Grid for a clean, responsive button layout. Added gradients, rounded corners, and shadows for a modern look.</li>
    <li><b>Right-Justified Output:</b> The display is now right-aligned for a more natural calculator feel.</li>
    <li><b>Improved Button Interactions:</b> Buttons highlight on hover and have smooth transitions for better UX.</li>
    <li><b>Added Vanta.js Animated Background:</b> The calculator sits on a fun, animated background for visual appeal.</li>
    <li><b>Clear (A/C) Button:</b> Resets the calculator to its initial state.</li>
    <li><b>Decimal Support:</b> You can enter and calculate with decimal numbers.</li>
    <li><b>All Basic Operations:</b> Supports +, -, ×, ÷ with correct order of operations.</li>
    <li><b>Responsive and Accessible:</b> Layout adapts to different screen sizes and uses accessible fonts.</li>
    <li><b>Code Comments:</b> The code is well-commented to help you understand each part.</li>
  </ul>
  <p>These changes make the calculator more visually appealing, easier to use, and a better learning tool for exploring JavaScript and UI design!</p>
</div>

<div class="section">
  <h2>🔍 How the Calculator Works: The <code>calculate</code> Function</h2>
  <pre><code>function calculate (first, second) {
  let result = 0;
  switch (operator) {
    case "+":
      result = first + second;
      break;
    case "-":
      result = first - second;
      break;
    case "*":
      result = first * second;
      break;
    case "/":
      result = first / second;
      break;
    default:
      break;
  }
  return result;
}
</code></pre>
  <p><b>What does this code mean and what does it do?</b></p>
  <ul>
    <li>The <code>calculate</code> function takes two numbers (<code>first</code> and <code>second</code>) and uses the current <code>operator</code> (like +, -, *, or /) to decide which math operation to perform.</li>
    <li>It uses a <code>switch</code> statement to check the operator:</li>
    <ul>
      <li>If the operator is "+", it adds the numbers.</li>
      <li>If "-", it subtracts.</li>
      <li>If "*", it multiplies.</li>
      <li>If "/", it divides.</li>
      <li>If the operator is not recognized, it does nothing.</li>
    </ul>
    <li>The function then returns the result of the calculation.</li>
  </ul>
  <p>This function is called whenever you press an operation or the equals button, so it’s the core of how the calculator computes answers!</p>
</div>

