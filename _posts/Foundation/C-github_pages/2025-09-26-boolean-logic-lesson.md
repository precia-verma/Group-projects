---
layout: post
title: Boolean Logic - Programming Basics
description: Learn about true/false values in programming with an interactive calculator
toc: True
permalink: /boolean-logic-lesson
categories: [Foundation, Lessons, Programming Concepts]
author: Open Coding Society
---

# � Boolean Logic: True or False?

## What You'll Learn

By the end of this lesson, you will:
- Know what boolean values are (true and false)
- Use comparison operators like `==` and `!=`
- Understand how computers make decisions
- Practice with an interactive calculator

## What Are Booleans?

Booleans are simple: they can only be **true** or **false**. Think of them like light switches - they're either ON or OFF.

Examples:
- `true` = yes, on, correct
- `false` = no, off, incorrect

Computers use booleans to make decisions, just like you do every day!

## Basic Boolean Operations

### Comparing Numbers

```javascript
console.log(5 == 5);     // true - equal
console.log(5 != 3);     // true - not equal
console.log(7 > 3);      // true - greater than
console.log(2 < 8);      // true - less than
```

### Combining Conditions

```javascript
// AND (&&) - BOTH must be true
console.log(true && true);    // true
console.log(true && false);   // false

// OR (||) - AT LEAST ONE must be true
console.log(true || false);   // true
console.log(false || false);  // false

// NOT (!) - FLIPS the value
console.log(!true);           // false
console.log(!false);          // true
```

## Try It Out: Interactive Calculator

See how booleans work in a real calculator:

<div id="lesson-animation">
  <div class="calculator-container">
      <div class="calculator-output" id="lesson-output">0</div>
      <div class="calculator-clear">AC</div>
      <div class="calculator-operation">+/-</div>
      <div class="calculator-operation">%</div>
      <div class="calculator-operation">÷</div>
      <div class="calculator-number">7</div>
      <div class="calculator-number">8</div>
      <div class="calculator-number">9</div>
      <div class="calculator-operation">*</div>
      <div class="calculator-number">4</div>
      <div class="calculator-number">5</div>
      <div class="calculator-number">6</div>
      <div class="calculator-operation">-</div>
      <div class="calculator-number">1</div>
      <div class="calculator-number">2</div>
      <div class="calculator-number">3</div>
      <div class="calculator-operation">+</div>
      <div class="calculator-number zero">0</div>
      <div class="calculator-number">.</div>
      <div class="calculator-equals">=</div>
  </div>
</div>

### What's Happening Behind the Scenes?

<div class="logic-analysis" style="margin-top: 20px; padding: 15px; background-color: #f8f9fa; border-radius: 8px; border-left: 4px solid #007acc;">
  <h4>Calculator Status</h4>
  <div id="boolean-breakdown">
    <p><strong>Last Action:</strong> <span id="current-expression">None</span></p>
    <p><strong>Calculator Checks:</strong></p>
    <ul id="boolean-evaluations">
      <li>Ready for new number: <span id="next-ready-eval">true</span></li>
      <li>Has decimal point: <span id="decimal-eval">false</span></li>
      <li>Number stored in memory: <span id="stored-number-eval">false</span></li>
      <li>Operation waiting: <span id="operation-eval">false</span></li>
    </ul>
  </div>
</div>

## How the Calculator Uses Booleans

The calculator makes decisions using true/false questions:

```javascript
// When you click a number button:
if (readyForNewNumber == true) {
    // Show the new number
    display = newNumber;
} else {
    // Add to existing number
    display = display + newNumber;
}
```

```javascript
// When you click an operation (+, -, *, /):
if (hasStoredNumber == false) {
    // Store the first number
    storedNumber = currentNumber;
} else {
    // Calculate with stored number
    result = calculate(storedNumber, currentNumber);
}
```

## Practice Exercises

### Exercise 1: Predict the Result

Try to guess what these will show before testing:

1. `5 == 5` → ?
2. `3 > 7` → ?
3. `true && false` → ?
4. `true || false` → ?
5. `!true` → ?

### Exercise 2: Real-World Examples

Think about these everyday decisions as booleans:

- "If it's raining AND I don't have an umbrella, then I'll get wet"
- "If I have homework OR there's a test tomorrow, then I need to study"
- "If it's NOT a school day, then I can sleep in"

## Boolean Truth Tables

Quick reference for how booleans combine:

### AND (&&) - Both must be true
| A | B | Result |
|---|---|--------|
| true | true | **true** |
| true | false | false |
| false | true | false |
| false | false | false |

### OR (||) - At least one must be true
| A | B | Result |
|---|---|----------|
| true | true | **true** |
| true | false | **true** |
| false | true | **true** |
| false | false | false |

## Why Booleans Matter

Booleans are everywhere in programming! They help computers:
- Make decisions (if this, then that)
- Check conditions (is the password correct?)
- Control what happens next in a program

## Quick Quiz

1. What are the only two boolean values?
2. What does `5 > 3` equal?
3. What does `true && false` equal?
4. Give an example of a boolean question from everyday life.

**Answers:** 1) true and false, 2) true, 3) false, 4) "Is it raining?" or "Am I hungry?"

---

*Great job! You now understand boolean logic - the foundation of how computers make decisions!*

<style>
  .calculator-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: 80px repeat(4, 60px);
    gap: 8px;
    width: 320px;
    margin: 20px auto;
    padding: 20px;
    background-color: #333;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
  }
  
  .calculator-output {
    grid-column: span 4;
    grid-row: 1/2;
    border-radius: 10px;
    padding: 15px;
    font-size: 24px;
    font-weight: bold;
    border: 2px solid #555;
    display: flex;
    align-items: center;
    background-color: #000;
    color: #0f0;
    text-align: right;
    justify-content: flex-end;
    min-height: 50px;
    overflow: hidden;
    font-family: 'Courier New', monospace;
  }
  
  .calculator-number, .calculator-operation, .calculator-clear, .calculator-equals {
    border-radius: 8px;
    padding: 0;
    margin: 0;
    font-size: 18px;
    font-weight: bold;
    border: 2px solid #555;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 50px;
    user-select: none;
  }
  
  .calculator-number {
    background-color: #666;
    color: white;
  }
  
  .calculator-operation {
    background-color: #ff9500;
    color: white;
  }
  
  .calculator-clear {
    background-color: #a6a6a6;
    color: black;
  }
  
  .calculator-equals {
    background-color: #ff9500;
    color: white;
  }
  
  .calculator-number.zero {
    grid-column: span 2;
    justify-content: flex-start;
    padding-left: 20px;
  }
  
  .calculator-number:hover, .calculator-operation:hover, .calculator-clear:hover, .calculator-equals:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    opacity: 0.9;
  }
  
  .calculator-number:active, .calculator-operation:active, .calculator-clear:active, .calculator-equals:active {
    transform: scale(0.95);
  }
  
  .logic-analysis {
    font-family: 'Courier New', monospace;
  }
  
  .logic-analysis span {
    font-weight: bold;
    color: #007acc;
    background-color: #f0f8ff;
    padding: 2px 4px;
    border-radius: 3px;
  }
  
  /* Enhanced code styling */
  code {
    background-color: #f8f9fa;
    color: #333;
    padding: 3px 6px;
    border-radius: 4px;
    font-family: 'Courier New', Monaco, 'Lucida Console', monospace;
    font-size: 0.9em;
    border: 1px solid #e9ecef;
  }
  
  pre {
    background-color: #f8f9fa;
    color: #333;
    padding: 15px;
    border-radius: 8px;
    border-left: 4px solid #007acc;
    overflow-x: auto;
    margin: 15px 0;
  }
  
  pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: 14px;
  }
  
  /* Syntax highlighting for code blocks */
  .highlight pre {
    background-color: #f8f9fa;
    color: #333;
    border: 1px solid #e9ecef;
  }
  
  .language-javascript {
    background-color: #2d3748;
    color: #e2e8f0;
  }
  
  .language-javascript code {
    background-color: transparent;
    color: #e2e8f0;
  }
  
  /* Table styling for truth tables */
  table {
    border-collapse: collapse;
    margin: 15px 0;
    width: 100%;
    max-width: 400px;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 8px 12px;
    text-align: center;
  }
  
  th {
    background-color: #f2f2f2;
    font-weight: bold;
  }
  
  tr:nth-child(even) {
    background-color: #f9f9f9;
  }
  
  /* Responsive design */
  @media (max-width: 480px) {
    .calculator-container {
      width: 280px;
      padding: 15px;
    }
    
    .calculator-output {
      font-size: 20px;
      padding: 10px;
    }
    
    .calculator-number, .calculator-operation, .calculator-clear, .calculator-equals {
      font-size: 16px;
      min-height: 45px;
    }
  }
  
  .highlight-true {
    background-color: #d4edda !important;
    color: #155724 !important;
  }
  
  .highlight-false {
    background-color: #f8d7da !important;
    color: #721c24 !important;
  }
</style>

<script>
// Enhanced lesson calculator with detailed boolean monitoring
var firstNumber = null;
var operator = null;
var nextReady = true;

const output = document.getElementById("lesson-output");
const numbers = document.querySelectorAll("#lesson-animation .calculator-number");
const operations = document.querySelectorAll("#lesson-animation .calculator-operation");
const clear = document.querySelectorAll("#lesson-animation .calculator-clear");
const equals = document.querySelectorAll("#lesson-animation .calculator-equals");

// Boolean analysis elements
const currentExpression = document.getElementById("current-expression");
const nextReadyEval = document.getElementById("next-ready-eval");
const decimalEval = document.getElementById("decimal-eval");
const storedNumberEval = document.getElementById("stored-number-eval");
const operationEval = document.getElementById("operation-eval");

// Function to update boolean analysis
function updateBooleanAnalysis(action = "idle") {
    if (!nextReadyEval) return; // Guard clause if elements don't exist
    
    // Update current expression
    if (currentExpression) {
        currentExpression.textContent = action;
    }
    
    // Update boolean evaluations with color coding
    const nextReadyResult = nextReady;
    nextReadyEval.textContent = nextReadyResult.toString();
    nextReadyEval.className = nextReadyResult ? 'highlight-true' : 'highlight-false';
    
    const hasDecimal = (output.innerHTML.indexOf(".") !== -1);
    decimalEval.textContent = hasDecimal.toString();
    decimalEval.className = hasDecimal ? 'highlight-true' : 'highlight-false';
    
    const hasStoredNumber = (firstNumber !== null);
    storedNumberEval.textContent = hasStoredNumber.toString();
    storedNumberEval.className = hasStoredNumber ? 'highlight-true' : 'highlight-false';
    
    const hasOperation = (operator !== null);
    operationEval.textContent = hasOperation.toString();
    operationEval.className = hasOperation ? 'highlight-true' : 'highlight-false';
}

// Number buttons listener
numbers.forEach(button => {
  button.addEventListener("click", function() {
    number(button.textContent);
    updateBooleanAnalysis(`Input number: ${button.textContent}`);
  });
});

// Enhanced number function with logging
function number(value) {
    console.log(`Boolean check: value != "." → ${value != "."}`);
    
    if (value != ".") {
        console.log(`Boolean check: nextReady == true → ${nextReady == true}`);
        if (nextReady == true) {
            output.innerHTML = value;
            console.log(`Boolean check: value != "0" → ${value != "0"}`);
            if (value != "0") {
                nextReady = false;
                console.log("Set nextReady = false");
            }
        } else {
            output.innerHTML = output.innerHTML + value;
            console.log("Appended to existing number");
        }
    } else {
        const hasDecimal = (output.innerHTML.indexOf(".") == -1);
        console.log(`Boolean check: no decimal exists → ${hasDecimal}`);
        if (output.innerHTML.indexOf(".") == -1) {
            output.innerHTML = output.innerHTML + value;
            nextReady = false;
            console.log("Added decimal point");
        } else {
            console.log("Decimal already exists - ignored");
        }
    }
}

// Operation buttons listener
operations.forEach(button => {
  button.addEventListener("click", function() {
    const op = button.textContent;
    if (op === "+/-" || op === "%") {
      handleSpecialOperation(op);
    } else {
      operation(op);
      updateBooleanAnalysis(`Operation: ${op}`);
    }
  });
});

// Enhanced operation function
function operation(choice) {
    // Convert division symbol
    if (choice === "÷") choice = "/";
    
    console.log(`Boolean check: firstNumber == null → ${firstNumber == null}`);
    if (firstNumber == null) {
        firstNumber = parseFloat(output.innerHTML);
        nextReady = true;
        operator = choice;
        console.log(`Stored first number: ${firstNumber}, operator: ${choice}`);
        return;
    }
    
    console.log("Calculating with existing number");
    if (operator !== null) {
        firstNumber = calculate(firstNumber, parseFloat(output.innerHTML)); 
        output.innerHTML = firstNumber.toString();
    }
    operator = choice;
    nextReady = true;
}

// Enhanced calculate function
function calculate(first, second) {
    let result = 0;
    console.log(`Calculating: ${first} ${operator} ${second}`);
    
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
            console.log(`Boolean check: second != 0 → ${second != 0}`);
            if (second != 0) {
                result = first / second;
            } else {
                result = "Error";
                console.log("Division by zero prevented");
            }
            break;
        default: 
            break;
    }
    return result;
}

// Equals button listener
equals.forEach(button => {
  button.addEventListener("click", function() {
    equal();
    updateBooleanAnalysis("Calculate result");
  });
});

// Equal action
function equal() {
    if (firstNumber !== null && operator !== null) {
        firstNumber = calculate(firstNumber, parseFloat(output.innerHTML));
        output.innerHTML = firstNumber.toString();
        operator = null;
        nextReady = true;
        console.log("Calculation completed");
    }
}

// Clear button listener
clear.forEach(button => {
  button.addEventListener("click", function() {
    if (button.textContent === "AC") {
      clearCalc();
      updateBooleanAnalysis("Clear all");
    }
  });
});

// Clear action
function clearCalc() {
    firstNumber = null;
    operator = null;
    output.innerHTML = "0";
    nextReady = true;
    console.log("Calculator cleared - all boolean flags reset");
}

// Add special operation handlers
function handleSpecialOperation(op) {
    const currentValue = parseFloat(output.innerHTML);
    let result;
    
    switch(op) {
        case "+/-":
            result = currentValue * -1;
            output.innerHTML = result.toString();
            updateBooleanAnalysis("Toggle sign");
            console.log(`Boolean operation: ${currentValue} * -1 = ${result}`);
            break;
        case "%":
            result = currentValue / 100;
            output.innerHTML = result.toString();
            updateBooleanAnalysis("Convert to percentage");
            console.log(`Boolean operation: ${currentValue} / 100 = ${result}`);
            break;
    }
}

// Initialize
updateBooleanAnalysis("Calculator ready");
</script>
