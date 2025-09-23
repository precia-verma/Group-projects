---
title: "Welcome to the Brew Shop! 🍺"
layout: post
date: 2025-09-16
permalink: /homebrew-installation-shop/
---

## Welcome to the Brew Shop! 🍺

<style>
/* Reused scoped styles to restyle post with dark teal → navy gradient */
#frontpage-card{max-width:980px;margin:18px auto;padding:26px;border-radius:14px;background:linear-gradient(180deg,#043a3a 0%,#07305a 100%);box-shadow:0 18px 40px rgba(2,12,18,0.6);font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,'Helvetica Neue',Arial;color:#e6fbff}
#frontpage-card h2{font-size:2.1rem;margin:0 0 10px;color:#bfeef0;letter-spacing:-0.5px}
#frontpage-card hr{border:none;border-top:1px solid rgba(255,255,255,0.06);margin:18px 0}
#frontpage-card p{color:#d9f3f4;font-size:1.01rem;line-height:1.55}
#frontpage-card ul, #frontpage-card ol{color:#d9f3f4;margin-left:1.1rem}
#frontpage-card code, #frontpage-card pre{background:#02242b;color:#e6fbff;padding:10px;border-radius:8px;display:block;overflow:auto}
.cta-btn{display:inline-block;padding:14px 20px;background:linear-gradient(90deg,#5b8a72,#78b39a);color:#ffffff !important;border-radius:999px;font-weight:800;text-decoration:none;box-shadow:0 8px 18px rgba(0,0,0,0.06);transition:transform .18s ease,box-shadow .18s ease}
.cta-btn:hover{transform:translateY(-2px);box-shadow:0 12px 22px rgba(0,0,0,0.08)}
details{background:linear-gradient(90deg,#0b2a2a,#042737);padding:10px;border-radius:10px;margin:8px 0}
summary{cursor:pointer;font-weight:700;color:#bfeef0}
@media (max-width:640px){#frontpage-card{padding:16px}#frontpage-card h2{font-size:1.5rem}}
</style>

<div id="frontpage-card" markdown="1">



---

### If you're driving anything other than a MacOS car, then you can skip this pickup stop.

---

Your customer wants Homebrew, here’s how to get it:

First, let's check if you already have Homebrew in your car. In a new terminal, type `brew --version`. If the command is not found, then you need to order Homebrew. 

To do so, go to `https://brew.sh/` and follow the instructions.

On the website, it will tell you to run this code in your terminal:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
You may need enter your password into terminal. Then, wait for your order to finish. Finally, make sure to run this: (make sure to put the word `sudo` before pasting this code)
```bash
echo >> /Users/anshrathod/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' »> /Users/anshrathod/ •zprof
ile
eval "$(/opt/homebrew/bin/brew shellenv)"
```
Your order should be complete now! But first--take a sip to make sure it's ready for your customer! Run `brew --version` to make sure your Homebrew is correctly installed. If the output is `Homebrew (version number)` then your brew is perfect and ready for your customer. 
# 🎉🎉

</div>

<p style="text-align:center;margin:18px 0 32px;">
	<a href="https://precia-verma.github.io/Group-projects/background" target="_blank" rel="noopener" class="cta-btn">Leave Shop</a>
</p>
