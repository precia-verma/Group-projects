---
title: "The Team Retrospective!"
layout: post
date: 2025-09-16
permalink: /team-retrospective/
---

<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>The Coders — Retrospective</title>
  <style>
    :root{
      --bg:#0b0f16;
      --panel:#111827;
      --panel-2:#0e1522;
      --text:#c9d1d9;
      --muted:#93a0ad;
      --border:#1f2937;
      --neon:#58a6ff;
      --neon-2:#10b981;
      --neon-3:#f59e0b;
      --neon-4:#ff7b72;
      --shadow:0 0 24px rgba(88,166,255,.15);
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      background: radial-gradient(1200px 600px at 15% 5%, rgba(88,166,255,.08), transparent 60%),
                 radial-gradient(900px 480px at 85% 10%, rgba(16,185,129,.07), transparent 58%),
                 var(--bg);
      color:var(--text);
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Inter, Noto Sans, Arial, "Apple Color Emoji","Segoe UI Emoji";
      line-height:1.6;
    }
    .topbar{
      position:sticky; top:0; z-index:5;
      background:rgba(11,15,22,.75);
      backdrop-filter: blur(8px);
      border-bottom:1px solid var(--border);
    }
    .wrap{max-width:1120px; margin:0 auto; padding:0 20px}
    .topbar .wrap{display:flex; align-items:center; gap:14px; padding:12px 20px}
    .brand{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      color:var(--neon);
      letter-spacing:.4px; font-weight:700; font-size:14px;
      display:flex; align-items:center; gap:8px;
    }
    .chip{
      font-size:12px; padding:4px 8px; border:1px solid var(--border); border-radius:999px; color:var(--muted);
    }
    .nav{margin-left:auto; display:flex; gap:8px; flex-wrap:wrap;}
    .nav a{
      font-size:12px; text-decoration:none; color:var(--muted);
      padding:8px 10px; border-radius:10px; border:1px solid var(--border); background:linear-gradient(180deg, var(--panel), var(--panel-2));
    }
    .nav a:hover{ color:var(--text); border-color:#2a3a50; box-shadow:0 0 0 2px rgba(88,166,255,.10) inset}
    header.hero{padding:42px 0 22px; border-bottom:1px solid var(--border);}
    .hero h1{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size:28px; margin:6px 0 6px; color:var(--text); letter-spacing:.3px;
    }
    .hero p{ color:var(--muted); margin:8px 0 0; font-size:14px}
    .badges{display:flex; gap:8px; flex-wrap:wrap; margin-top:12px}
    .badge{font-size:11px; padding:6px 10px; border-radius:10px; border:1px solid var(--border); background:#0e1624; color:#a7b3c2}
    section{padding:26px 0}
    .grid{display:grid; gap:16px}
    @media (min-width:900px){ .grid-2{ grid-template-columns: 1fr 1fr } .grid-3{ grid-template-columns: repeat(3, 1fr) } }
    .card{
      background:linear-gradient(180deg, var(--panel), var(--panel-2));
      border:1px solid var(--border);
      border-radius:14px; padding:18px; box-shadow:var(--shadow);
    }
    .card h3{margin:0 0 8px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size:18px; color:var(--neon);}
    .muted{color:var(--muted)} .small{font-size:13px} .tiny{font-size:12px}
    ul.clean{list-style:none; padding-left:0; margin:10px 0}
    ul.clean li{padding:8px 10px; margin:6px 0; border:1px dashed #223044; border-radius:10px; background:#0b1320;}
    footer{margin-top:24px; padding:22px 0; border-top:1px solid var(--border); color:var(--muted); font-size:12px; text-align:center}
    .anchor{ position:relative; top:-68px; visibility:hidden }
  </style>
</head>
<body>

  <!-- Top Navigation -->
  <div class="topbar">
    <div class="wrap">
      <div class="brand">💻 THE CODERS<span class="chip">Retrospective</span></div>
      <nav class="nav">
        <a href="#purpose">Purpose</a>
        <a href="#features">Features</a>
        <a href="#wins">Wins</a>
        <a href="#challenges">Challenges</a>
        <a href="#lessons">Lessons</a>
        <a href="#future">Future</a>
        <a href="#timeline">Timeline</a>
      </nav>
    </div>
  </div>

  <!-- Hero -->
  <header class="hero">
    <div class="wrap">
      <h1>📓 The Coders’ Project Retrospective</h1>
      <p class="small">Mini-games (“hacks”) + UI polish + deployment practice across HTML, CSS, JavaScript, and Python.</p>
      <div class="badges">
        <span class="badge">🎮 Cookie Clicker Hack</span>
        <span class="badge">🧮 Calculator Hack</span>
        <span class="badge">🖱️ Dynamic Buttons</span>
        <span class="badge">📝 Blog System</span>
        <span class="badge">🚀 Homepage</span>
      </div>
    </div>
  </header>

  <main class="wrap">

    
# 📓 The Coders' Retrospective! 
## 🚀 Purpose
Our purpose in building these hacks was not just to create small games, but to **train ourselves to use coding as a practical tool**.  
Each hack acted as a challenge that introduced us to different parts of development:  

- Buttons taught us UI precision.  
- The homepage trained us in layout and navigation.  
- Blogs gave us practice structuring content.  
- The hacks helped us understand interactivity and logic.  

Together, these projects gave us a foundation for bigger builds in the future.  

---

## 🎨 Scope & Features  

### 🖱️ Button Design & Functionality  
Buttons were our main interactive components. We experimented with colors, hover effects, and states to make them responsive.  
The hardest part was precise positioning, which required adjusting `margin`, `padding`, and pixel values until the alignment clicked.  
This process showed us how small changes make big differences in user experience.  

### 🏠 Homepage & Navigation  
The homepage acted as the hub of our project. We focused on making it clean, functional, and visually engaging.  
Beyond just listing buttons, it created a structured flow that connected all parts of our work, giving the impression of a unified product.  

### ✍️ Blog Creation & Layouts  
Blogs let us practice long-form content design. We learned to format text with clear headings, smaller fonts, and consistent styling.  
By linking posts together with navigation buttons, we created a professional flow that tied our project together.  

### 🎮 Interactive Hacks  
- **Cookie Clicker:** taught us about event listeners, DOM updates, and incremental logic.  
- **Calculator:** forced us to handle operator precedence, clear/reset functions, and avoid errors like divide-by-zero.  

Both gave us real practice in JavaScript interactivity and problem-solving.  

---

## 🌟 What Went Well  
- Our final designs were consistent and visually polished.  
- Both mini-games worked smoothly, boosting our coding confidence.  
- We solved problems creatively, using online resources and trial-and-error.  
- By the end, our teamwork and communication were much stronger than when we began.  

---

## ⚡ Challenges  
- At first, communication wasn’t clear, leading to slower progress and overlap.  
- Button positioning and layout formatting took longer than expected.  
- Balancing looks with functionality was harder than it seemed at the start.  

---

## 📚 Lessons Learned  
- Communication is essential — regular updates prevent duplication and confusion.  
- Iteration works — small changes and tests are better than waiting for perfection.  
- Design consistency matters — even small details like spacing and color add up.  
- Teamwork multiplies skill — combining strengths created a better final product.  

---

## 🔮 Future Improvements  
- Plan roles and tasks earlier to save time.  
- Adopt advanced CSS tools like flexbox and grid for cleaner layouts.  
- Save hack progress with `localStorage` so data isn’t lost.  
- Improve accessibility with ARIA labels and color contrast checks.  
- Refactor game logic into smaller, testable functions for easier debugging.  

---

## ⏱️ Timeline  
- **Week 1:** Button prototypes — colors, hover, placement.  
- **Week 2:** Homepage structure and navigation system.  
- **Week 3:** Cookie Clicker prototype — click events and score display.  
- **Week 4:** Calculator Hack — operators, reset, error handling.  
- **Week 5:** Blog polish, styling adjustments, deployment.  

---

## 🎯 Final Thoughts  
As **The Coders 💻**, we didn’t just complete assignments — we built a set of connected tools and experiences  
that look good, work well, and taught us practical skills.  

We turned challenges into lessons and now have the confidence to tackle larger projects.  
Most importantly, we learned that *communication, iteration, and collaboration* are what turn small hacks into something that feels like a real product.  




  </main>

  <footer>
    Built with ❤️ by The Coders · Keep shipping, keep learning.
  </footer>

</body>
</html>
