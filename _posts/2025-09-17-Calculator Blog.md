---
title: calculator-blog
layout: base
description: Calculator BLOG!
permalink: /calculator-blog
---
# 🖥️ The Coders (group name)

# 🧮 Calculator Project Blog

## 👩‍💻 The Coders 

| Name            | GitHub Profile                                   |
|-----------------|--------------------------------------------------|
| **Precia Verma**| [github.com/precia-verma](https://github.com/precia-verma) |
| **Krystal**     | [github.com/krystal-727](https://github.com/krystal-727) |
| **Tasha (Struti)** | [github.com/StutiPandey19](https://github.com/StutiPandey19) |

---

## 📝 Hack 1: Notebook
[calculator.md](https://github.com/user-attachments/files/22397696/calculator.md)

---

## 🚀 Hack 2: Your Own Feature

### Feature Name: JS Calculator
**Purpose:**  
The JS Calculator is an interactive web-based calculator built with HTML, CSS, and JavaScript. Its purpose is to help users perform basic arithmetic operations (addition, subtraction, multiplication, division) directly in the browser. The calculator features a visually appealing, right-justified display, responsive buttons for numbers and operations, and supports decimal calculations. It also includes a clear (A/C) button to reset the calculation and an equals button to compute results, making it a practical tool for learning and practicing JavaScript DOM manipulation and event handling.

### Feature Name: Right-Justified Output Display
**Purpose:**  
This feature ensures that the calculator’s result/output is always aligned to the right side of the display area, mimicking the behavior of real-world calculators. It improves readability, especially for large or decimal numbers, and provides a familiar user experience. This makes it easy for users to read and interpret results as they perform calculations.

#### Example CSS:
```css
display: flex;
align-items: center;
justify-content: flex-end; /* right-align text */
```

This makes numbers and results easy to read, especially for long or decimal values.

### Feature Name: Clear (A/C) Button
**Purpose:**  
The calculator includes an "A/C" (All Clear) button that resets the calculator to its initial state. When clicked, it sets the display back to 0 and clears any stored numbers or operations, allowing the user to start a new calculation.

#### Example JavaScript:
```javascript
function clearCalc () {
	firstNumber = null;
	output.innerHTML = "0";
	nextReady = true;
}
```

The button is styled and placed in the calculator grid for easy access.

---

## 🎮 Try the Calculator
[Link to Game: https://precia-verma.github.io/Group-projects/calculator](https://precia-verma.github.io/Group-projects/calculator)

---

## 🖼️ Picture of Code

<img width="836" height="816" alt="Image" src="https://github.com/user-attachments/assets/22a2fb7a-2a1e-482f-a0a6-88956cdc6266" />

## 🛠️ What We Changed and Why

- **Modernized the Calculator UI:**
  - Used CSS Grid for a clean, responsive button layout.
  - Added gradients, rounded corners, and shadows for a modern look.
- **Right-Justified Output:**
  - The display is now right-aligned for a more natural calculator feel.
- **Improved Button Interactions:**
  - Buttons highlight on hover and have smooth transitions for better UX.
- **Added Vanta.js Animated Background:**
  - The calculator sits on a fun, animated background for visual appeal.
- **Clear (A/C) Button:**
  - Resets the calculator to its initial state.
- **Decimal Support:**
  - You can enter and calculate with decimal numbers.
- **All Basic Operations:**
  - Supports +, -, ×, ÷ with correct order of operations.
- **Responsive and Accessible:**
  - Layout adapts to different screen sizes and uses accessible fonts.
- **Code Comments:**
  - The code is well-commented to help you understand each part.

These changes make the calculator more visually appealing, easier to use, and a better learning tool for exploring JavaScript and UI design!

---

## 🔍 How the Calculator Works: The `calculate` Function

Below is the main function that performs the math operations in our calculator:

```javascript
function calculate (first, second) {
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
```

### What does this code mean and what does it do?
- The `calculate` function takes two numbers (`first` and `second`) and uses the current `operator` (like +, -, *, or /) to decide which math operation to perform.
- It uses a `switch` statement to check the operator:
  - If the operator is "+", it adds the numbers.
  - If "-", it subtracts.
  - If "*", it multiplies.
  - If "/", it divides.
  - If the operator is not recognized, it does nothing.
- The function then returns the result of the calculation.

This function is called whenever you press an operation or the equals button, so it’s the core of how the calculator computes answers!

