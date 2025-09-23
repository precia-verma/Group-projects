---
layout: base
title: Trouble Shooting Guide 
permalink: /trouble-blogs/
---

<style>
  body {
    background: radial-gradient(ellipse at center, #0a0f2c 0%, #000000 100%);
    color: #fff;
    font-family: 'Orbitron', 'Montserrat', Arial, sans-serif;
    margin: 0;
    padding: 0;
    min-height: 100vh;
    overflow-x: hidden;
  }
  .space-header {
    text-align: center;
    margin-top: 2.5rem;
    margin-bottom: 1.5rem;
    font-size: 3.2rem;
    letter-spacing: 2px;
    text-shadow: 0 0 30px #7dd3fc, 0 0 60px #2563eb;
  }
  .space-section {
    background: rgba(30, 41, 59, 0.7);
    border-radius: 1.5rem;
    margin: 2rem auto;
    max-width: 700px;
    padding: 2rem 2.5rem;
    box-shadow: 0 0 30px #1e293b, 0 0 60px #2563eb33;
    border: 1px solid #334155;
  }
  .space-section h2, .space-section h3 {
    color: #7dd3fc;
    text-shadow: 0 0 10px #2563eb;
  }
  .space-section code, .space-section pre {
    background: #0f172a;
    color: #a5f3fc;
    border-radius: 0.5rem;
    padding: 0.2em 0.5em;
    font-size: 1em;
  }
  .space-section ul, .space-section ol {
    text-align: left;
    margin-left: 1.5em;
  }
  .space-icon {
    font-size: 2.2rem;
    margin-right: 0.5rem;
    vertical-align: middle;
  }
  .star {
    position: fixed;
    border-radius: 50%;
    background: white;
    opacity: 0.7;
    z-index: 0;
    animation: twinkle 3s infinite alternate;
  }
  @keyframes twinkle {
    0% {opacity: 0.3;}
    100% {opacity: 1;}
  }
</style>

<div class="space-header">🪐 Trouble Shooting Guide <span class="space-icon">🚀</span></div>
<div id="layer1"></div>
<div id="layer2"></div>
<div id="layer3"></div>
<script>
  function makeStars(layerId, count, size, duration) {
    const layer = document.getElementById(layerId);
    for (let i = 0; i < count; i++) {
      const s = document.createElement('div');
      s.className = 'star';
      s.style.width = size + 'px';
      s.style.height = size + 'px';
      s.style.top  = Math.random() * 100 + 'vh';
      s.style.left = Math.random() * 100 + 'vw';
      s.style.animationDuration = duration + 's';
      s.style.animationDelay = (Math.random() * 3) + 's';
      layer.appendChild(s);
    }
  }
  makeStars('layer1', 60, 1, 2);
  makeStars('layer2', 40, 2, 3.5);
  makeStars('layer3', 25, 3, 5);
</script>

<div class="space-section">
  <h2>🛠️ Tool Setup Troubleshooting Guide</h2>
  <p>Use this page if something is not working.<br>Each section is independent — jump directly to the area you are stuck.<br><span class="space-icon">🌌</span></p>
</div>

<div class="space-section">
  <h3>🚀 GitHub Commit / Config Recovery</h3>
  <p>Use these commands if git commit is failing.</p>
  <ul>
    <li>✅ <b>Expectation:</b> You have a GitHub username + email</li>
  </ul>
  <pre><code>git config --list # shows your GitHub username + email.</code></pre>
  <ul>
    <li>❌ <b>If not personalized, run to match your credentials:</b></li>
  </ul>
  <pre><code>git config --global user.name "jm1021"        # change to your GitHub ID
git config --global user.email "jm1021@gmail.com"  # change to your Email</code></pre>
</div>

<div class="space-section">
  <h3>🛰️ Directory + Clone Recovery</h3>
  <ul>
    <li>✅ <b>Expectation:</b> You can <code>cd</code> into your personal directory, and an <code>ls</code> shows your repo folder (ex: student).</li>
  </ul>
  <b>Navigate</b>
  <pre><code>cd ~/jm1021 # change jm1021 to your user directory name</code></pre>
  <ul>
    <li>❌ If <code>cd</code> fails, run:</li>
  </ul>
  <pre><code>mkdir ~/jm1021
cd ~/jm1021</code></pre>
  <b>Check for repo folder</b>
  <pre><code>ls # should show "student"</code></pre>
  <ul>
    <li>❌ If missing, run:</li>
  </ul>
  <pre><code>git clone https://github.com/jm1021/student.git # change to personal location of repo</code></pre>
</div>

<div class="space-section">
  <h3>🌠 Virtual Environment Recovery</h3>
  <ul>
    <li>✅ <b>Expectation:</b> Your terminal prompt shows <code>(venv)</code> prefix.</li>
  </ul>
  <b>Run Virtual Environment</b>
  <pre><code>source venv/bin/activate</code></pre>
  <ul>
    <li>❌ If it fails</li>
  </ul>
  <pre><code>./scripts/venv.sh
source venv/bin/activate</code></pre>
  <b>VSCode Launch and Memories</b>
  <ul>
    <li>✅ Satisfying the pre-requisites</li>
    <ul>
      <li>In project directory of your repo <code>pwd</code></li>
      <li>Sourcing virtual environment <code>source venv/bin/activate</code></li>
      <li>Ensure your terminal prompt shows the active virtual environment <code>(venv)</code>.</li>
    </ul>
  </ul>
  <p>You are now ready to load VSCode and build a proper memory to open your project.</p>
  <pre><code>code .</code></pre>
  <ul>
    <li>✅ Verify VSCode launch</li>
    <ul>
      <li>Terminal and presence of <code>(venv)</code> prompt</li>
      <li>Open your Jokes IPYNB notebook and select the Python kernel with the <code>(venv)</code> prefix.</li>
    </ul>
    <li>❌ If you fail verification</li>
  </ul>
  <p>You may have opened your repo project without activating the proper <code>(venv)</code> environment.<br>Check the <b>Recent</b> listings. If there are entries that look incorrect or outdated (bad memories), remove them all.</p>
  <ul>
    <li>Shift-Cmd-P (Mac) or Shift-Ctl-P (Windows, KASM)</li>
    <li>type: Clear Recently Open -- select and confirm</li>
    <li>close VSCode</li>
    <li>Repeat VSCode Launch and Memories</li>
  </ul>
</div>

<div class="space-section">
  <h3>🪐 Version Checks</h3>
  <ul>
    <li>✅ <b>Expectation:</b> Run the bash script below</li>
    <ul>
      <li>Output is expected for each <code>### Command</code></li>
      <li>Version may be slightly different, but ask if you are not sure</li>
      <li><i>Java kernels are required for CSA only</i></li>
    </ul>
    <li>❌ If it fails</li>
  </ul>
  <p>Best course of action is to run OS specific activate scripts from <code>pages</code> project directory</p>
  <pre><code>./scripts/activate_ubuntu.sh # windows ubuntu
./scripts/activate_macos.sh # macos
./scripts/activate.sh # help setup git config options</code></pre>
  <pre><code># Define an array of commands
commands=("python --version" "pip --version" "ruby -v" "bundle -v" "gem -v" "jupyter --version" "jupyter kernelspec list" "git config --global user.name" "git config --global user.email")

for cmd in "${commands[@]}"; do
    echo "### Command: $cmd"
    bash -c "$cmd"
done</code></pre>
</div>

<!-- New Space-Themed Sections -->
<div class="space-section">
  <h3>🌌 404 Error on GitHub Pages</h3>
  <ul>
    <li>✅ <b>Expectation:</b> Your GitHub Pages site loads at the expected URL without a 404 error.</li>
    <li>❌ <b>If you see a 404 error when visiting your live site:</b></li>
  </ul>
  <pre><code>https://your-username.github.io/your-repo/</code></pre>
  <ul>
    <li>Check that your repository is set to public and GitHub Pages is enabled in the repo settings.</li>
    <li>Make sure your site is built from the correct branch (usually <code>main</code> or <code>gh-pages</code>).</li>
    <li>For project sites, ensure your URLs include the repo name (e.g., <code>/your-repo/</code>).</li>
    <li>Wait a few minutes after pushing changes—GitHub Pages can take time to update.</li>
    <li>Check for a valid <code>index.html</code> or <code>index.md</code> in the root or docs/ folder.</li>
    <li>If using custom domains, verify DNS and CNAME settings.</li>
    <li>Try a hard refresh or clear your browser cache if the error persists.</li>
  </ul>
</div>

<div class="space-section">
  <h3>🛸 Makefile Troubleshooting</h3>
  <ul>
    <li>✅ <b>Expectation:</b> Running <code>make</code> should build or run your project as intended.</li>
    <li>❌ <b>If you get errors like "No rule to make target" or unexpected failures:</b></li>
  </ul>
  <pre><code>make
make clean
cat Makefile</code></pre>
  <ul>
    <li>Check for typos or incorrect indentation (use tabs, not spaces, for commands in Makefiles).</li>
    <li>Ensure the target you are running exists in your <code>Makefile</code>.</li>
    <li>If you see permission errors, try: <code>chmod +x scripts/your_script.sh</code></li>
    <li>Run <code>make clean</code> to remove old build files and try again.</li>
    <li>If you edited the Makefile, make sure to save it before running <code>make</code>.</li>
    <li>For debugging, add <code>@echo</code> statements or run <code>make -n</code> to see what would be executed.</li>
  </ul>
</div>

<div class="space-section" style="text-align:center; margin-bottom:3rem;">
  <h3>🌟 Hopefully this helped!</h3>
  <p>If you made it this far, your troubleshooting journey is complete.<br>
  May your code be bug-free and your pages always load! 🚀✨</p>
</div>