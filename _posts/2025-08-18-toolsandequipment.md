---
layout: base
title: "🚀 Tools and Equipment"
permalink: /tools-blogs
---

<style>
/* --- Deep-Space Aesthetic --- */
body {
  background: radial-gradient(circle at 20% 20%, #0a0f2c, #000000);
  color: #f0f8ff;
  font-family: "Orbitron", sans-serif;
  line-height: 1.7;
  overflow-x: hidden;
}
.star {
  position: fixed;
  border-radius: 50%;
  background: white;
  opacity: 0.7;
  z-index: 0;
  pointer-events: none;
  animation: twinkle 3s infinite alternate;
}
@keyframes twinkle {
  0% {opacity: 0.3;}
  100% {opacity: 1;}
}
a {
  color: #7fffd4;
  text-decoration: none;
  font-weight: bold;
}
a:hover {
  color: #00ffff;
  text-shadow: 0 0 6px #00ffff;
}
h1, h2 {
  text-align: center;
  text-shadow: 0 0 10px #7fffd4;
}
</style>

<!-- Star layers -->
<div id="star-layer"></div>
<script>
// Sprinkle stars in the background
(function() {
  const layer = document.getElementById('star-layer');
  for (let i = 0; i < 80; i++) {
    const s = document.createElement('div');
    s.className = 'star';
    const size = Math.random() * 2 + 1;
    s.style.width = size + 'px';
    s.style.height = size + 'px';
    s.style.top = Math.random() * 100 + 'vh';
    s.style.left = Math.random() * 100 + 'vw';
    s.style.animationDuration = (2 + Math.random() * 3) + 's';
    s.style.animationDelay = (Math.random() * 3) + 's';
    layer.appendChild(s);
  }
})();
</script>

# 🚀 Tools and Equipment

Suit up, space cadet! These pages from **Open Coding Society** are your essential planets in the dev galaxy.  
Click the links, explore the knowledge, and level-up your mission control skills.

---

> ## 🪐 [Main Command Center](https://pages.opencodingsociety.com/tools/)
>
> **Mission Objective:** Big-picture overview of all the dev gear.  
> * Why version control and good tooling save you from black-hole chaos.  
> * How different tools—editors, GitHub, terminals—work together in a single orbit.  
> * Best practices for collaborating with other interstellar coders.

> ## 🌌 [Accounts](https://pages.opencodingsociety.com/tools/accounts)
>
> **Mission Objective:** Secure your digital identity before launch.  
> * Learn what counts as **Personally Identifiable Information (PII)** and how to guard it.  
> * Step-by-step creation of key accounts like GitHub, Slack/Discord, and any project-hosting platforms.  
> * Tips on strong passwords, multi-factor authentication, and keeping public vs. private data separated.  
> * Why a clean public profile matters for future collabs and job hunting across galaxies.

> ## 🚀 [GitHub](https://pages.opencodingsociety.com/tools/github)
>
> **Mission Objective:** Master the starship of version control.  
> * How repositories, commits, and branches track every line of code.  
> * Forking & Pull Requests: collaborate across galaxies without collision.  
> * Understanding issues, project boards, and roles (owner vs. contributor).  
> * Etiquette for commit messages and reviewing PRs so teammates don’t get lost in a wormhole.

> ## 🌠 [GitHub Pages](https://pages.opencodingsociety.com/tools/github_pages)
>
> **Mission Objective:** Deploy your cosmic creations to the universe.  
> * Free static-site hosting directly from your GitHub repo—perfect for portfolios and documentation.  
> * Setting up a site: enabling Pages, selecting a theme, configuring a custom domain.  
> * Using GitHub Actions to automate builds and updates, so your site stays as fresh as a nebula.  
> * Tips for markdown-driven sites and Jekyll basics.

> ## 🛰️ [Operating Systems](https://pages.opencodingsociety.com/tools/os)
>
> **Mission Objective:** Configure your home planet for coding.  
> * Windows + WSL, macOS, and Linux setup guides with package managers (Homebrew, apt, etc.).  
> * Installing shell tools like Git, Python, and compilers.  
> * Environment variables and PATH—so your commands work anywhere in the galaxy.  
> * Cross-platform quirks to watch out for when collaborating with devs on other OS planets.

> ## 🛸 [VSCode](https://pages.opencodingsociety.com/tools/vscode)
>
> **Mission Objective:** Build the ultimate coding cockpit.  
> * Installing VSCode and must-have extensions for linting, debugging, and Git integration.  
> * Setting up a project folder, using integrated terminal, and customizing the editor theme (dark mode = true space vibes).  
> * Using Live Server or dev containers to test code locally before you launch.  
> * Keyboard shortcuts and productivity hacks to move at lightspeed.

> ## 💫 [Troubleshooting](https://pages.opencodingsociety.com/tools/trouble)
>
> **Mission Objective:** Escape any black hole of bugs.  
> * Common issues when pushing to GitHub Pages, fixing merge conflicts, and broken builds.  
> * Debugging tips: reading stack traces, checking logs, and using the terminal like a pro.  
> * How to ask for help effectively (good error reports = faster rescue missions).  
> * Quick commands to reset, revert, or recover when something explodes mid-flight.

---

### 🌟 Final Star Tips

* **Test Locally First:** Don’t launch a broken starship—run and debug before committing.  
* **Commit Messages = Star Maps:** Descriptive logs help future explorers (including future-you).  
* **Stay Secure:** Guard your credentials like they’re oxygen tanks.  
* **Document Everything:** Good READMEs and comments are like leaving space beacons for your crew.

> *“Shoot for the stars, but push to GitHub first.”* 🌌
