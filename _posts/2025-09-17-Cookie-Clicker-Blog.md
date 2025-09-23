---
title: cookie-clicker-blog
layout: base
description: Cookie-Clicker BLOG!
permalink: /cookie-clicker-blog
---
# 🖥️ The Coders

| Name            | GitHub Profile                                   |
|-----------------|--------------------------------------------------|
| **Precia Verma**| [github.com/precia-verma](https://github.com/precia-verma) |
| **Krystal**     | [github.com/krystal-727](https://github.com/krystal-727) |
| **Tasha (Struti)** | [github.com/StutiPandey19](https://github.com/StutiPandey19) |

---

## 🍪 Hack 1: Quiz
<img width="1496" height="945" alt="Quiz Screenshot" src="https://github.com/user-attachments/assets/5bc12101-b14a-4927-a7b4-b506c3fc8bc2" />

### Notebook
[**2025-08-29-collaboration.ipynb**](https://github.com/user-attachments/files/22396858/2025-08-29-collaboration.ipynb)

---

## 🥛 Hack 2: Your Own Feature – **Milk Upgrade**

### Purpose  
The **Milk Upgrade** is a purchasable item in the Cookie Clicker game shop (Cost: **1000 cookies**).  
Buying Milk gives a sweet boost: it **doubles cookies per click** and makes the grind way more strategic.

| Screenshot | Screenshot | Screenshot | Screenshot |
|------------|-----------|-----------|-----------|
| <img width="1496" height="945" src="https://github.com/user-attachments/assets/2164306a-a41d-4ade-aeee-9862155b1692" /> | <img width="753" height="853" src="https://github.com/user-attachments/assets/9ab5cb70-de6e-4b7b-8d01-6e556067f26a" /> | <img width="745" height="818" src="https://github.com/user-attachments/assets/fe90b75b-75c8-4d3a-8a54-44dab56c934c" /> | <img width="836" height="664" src="https://github.com/user-attachments/assets/4f8c2c75-0be4-44f3-a5f3-88b263226100" /> |

---

## 🥛 How the Milk Upgrade Works (Code Explained)

```javascript
// --- Milk Upgrade Feature ---
const milkUpgrade = {
  name: "Milk",
  emoji: "🥛",
  price: 1000,
  itemEffected: "click",
  multiplier: 2,
};

// Add Milk to upgrades list
shop.upgrades.push(milkUpgrade);

// Restore Milk upgrade from localStorage
let hasMilk = localStorage.getItem("hasMilk") === "true";

// Listen for Milk button click
document.addEventListener("DOMContentLoaded", () => {
  const milkBtn = document.getElementById("milkBtn");
  if (milkBtn) {
    if (hasMilk) milkBtn.disabled = true;
    milkBtn.addEventListener("click", () => {
      if (hasMilk) {
        alert("You already own Milk!");
        return;
      }
      if (cookie.cookies >= milkUpgrade.price) {
        cookie.addCookies(-milkUpgrade.price);
        cookie.cookieMulti *= milkUpgrade.multiplier;
        hasMilk = true;
        localStorage.setItem("hasMilk", "true");
        milkBtn.disabled = true;
        alert("Milk purchased! Your cookies per click are doubled.");
      } else {
        alert("Not enough cookies!");
      }
    });
  }
});
```

### What does this code mean and what does it do?
- This code adds a new upgrade called "Milk" to the Cookie Clicker shop. The Milk upgrade costs 1000 cookies and, when purchased, doubles the number of cookies you get per click.
- The `milkUpgrade` object defines the upgrade's name, emoji, price, what it affects (clicks), and its multiplier (2x).
- The upgrade is added to the shop's list of upgrades so it appears in the game.
- The code checks if the player already owns Milk by looking in `localStorage` (so the upgrade is remembered even if you reload the page).
- When the Milk button is clicked:
  - If you already own Milk, it shows an alert and does nothing.
  - If you have enough cookies, it subtracts the price, doubles your cookies per click, marks Milk as owned, saves this to `localStorage`, disables the button, and shows a success alert.
  - If you don't have enough cookies, it shows an alert saying so.

This feature makes the game more strategic and rewarding, giving players a big boost when they buy Milk!

---

## 🎮 Play the Game
👉 **[Cookie Clicker Game Live Site](https://precia-verma.github.io/Group-projects/cookie-clicker-game/)**  

---