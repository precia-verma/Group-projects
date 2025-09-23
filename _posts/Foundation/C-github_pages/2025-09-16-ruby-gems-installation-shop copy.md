---
title: "Welcome to the Gem Shop! ‧⊹'💎♦️*⁠.⁠✧"
layout: post
date: 2025-09-16
permalink: /ruby-gems-installation-shop/
---

## Welcome to the Gem Shop! ‧⊹'💎♦️*⁠.⁠✧

<style>
/* Reused scoped styles to restyle gem shop post (presentation only) */
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

### If you're driving a Chromebook and/or a Kasm/Linux car, then these steps are for you:
###### If you're driving a MacOS, your instructions are further down.

---

Your customer wants a nice shiny ruby gem for a proposal, here at the Gem Shop, you can pick it up for them! Here's how:

First, in your Kasm workspace, open a new terminal window. Then, run these commands:
```bash 
sudo apt update
sudo apt install -y ruby-full
gem install bundler
# install any gem later with:
# gem install <gem_name>
```
Great! Now you have your ruby gem! But you need to make sure its a real gem. To do that, run these in your terminal:
```
ruby -v
gem -v
bundler -v
```
If they're real gems, then you should be met with the ruby version number, the gem version number, and the bundler version number.

Congrats! You picked up your customer's shiny ruby gem. Head onto the next button now!

# 🎉🎉

---

### If you're driving a MacOS car, then these steps are for you:

---
Your customer wants a nice shiny ruby gem for a proposal, here at the Gem Shop, you can pick it up for them! Here's how:

First, in your MacOS workspace, open a new terminal window. Then, run these commands:
```bash
echo 'export PATH="$(brew --prefix ruby)/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc


gem install bundler
```
Great! Now you have your ruby gem! But you need to make sure its a real gem. To do that, run these in your terminal:
```
ruby -v
gem -v
bundler -v
```
If they're real gems, then you should be met with the ruby version number, the gem version number, and the bundler version number.

Congrats! You picked up your customer's shiny ruby gem. Head onto the next button now!

# 🎉🎉

</div>

<p style="text-align:center;margin:18px 0 32px;">
	<a href="https://precia-verma.github.io/Group-projects/background" target="_blank" rel="noopener" class="cta-btn">Leave Shop</a>
</p>