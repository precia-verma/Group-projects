---
title: Array Hack Challenge - Answer Sheet
comments: true
layout: base
permalink: /javascript/array/hack/answers
description: Array Hack Challenge Answer Sheet
author: The Coders!
---

# Array Hack Challenge - Answer Sheet

This document provides sample solutions for the Array Hack challenges. Remember that there are often multiple valid ways to solve programming problems.

## Hack #1: The Food Array

```javascript
// 1. Create an array with 5 favorite foods
let favoriteFoods = ["pizza", "ice cream", "burgers", "tacos", "pasta"];

// 2. Print the first food in your array
console.log("First food:", favoriteFoods[0]);  // Should print "pizza"

// 3. Change the third food (index 2) to something different
favoriteFoods[2] = "sushi";
// Now the array is ["pizza", "ice cream", "sushi", "tacos", "pasta"]

// 4. Add a new food to the end of your array
favoriteFoods.push("chocolate");
// Now the array is ["pizza", "ice cream", "sushi", "tacos", "pasta", "chocolate"]

// 5. Print the new length of your array
console.log("Number of foods:", favoriteFoods.length);  // Should print 6

// 6. Print the whole array to see all the changes you've made
console.log("My favorite foods are now:", favoriteFoods);
// Should print ["pizza", "ice cream", "sushi", "tacos", "pasta", "chocolate"]

// BONUS CHALLENGE: Add another food at the beginning of the array
favoriteFoods.unshift("waffles");
console.log("After adding to the front:", favoriteFoods);
// Should print ["waffles", "pizza", "ice cream", "sushi", "tacos", "pasta", "chocolate"]
console.log("New length:", favoriteFoods.length);  // Should print 7
```

### Expected Output

```
First food: pizza
Number of foods: 6
My favorite foods are now: [ 'pizza', 'ice cream', 'sushi', 'tacos', 'pasta', 'chocolate' ]
After adding to the front: [ 'waffles', 'pizza', 'ice cream', 'sushi', 'tacos', 'pasta', 'chocolate' ]
New length: 7
```

### Key Concepts Demonstrated

- Creating an array with initial values
- Accessing array elements by index
- Modifying array elements
- Adding elements to the end with `push()`
- Getting array length with the `length` property
- Adding elements to the beginning with `unshift()`

## Hack #2: The Temperature Array

```javascript
// 1. Create an array with 7 daily temperatures
let weekTemps = [72, 68, 74, 80, 76, 72, 67];

// 2. Print the temperatures for Monday and Friday
console.log("Monday temperature:", weekTemps[0]);  // Should print 72
console.log("Friday temperature:", weekTemps[4]);  // Should print 76

// 3. Calculate and print the average temperature
// Method 1: Manual addition
let sum = weekTemps[0] + weekTemps[1] + weekTemps[2] + weekTemps[3] + 
          weekTemps[4] + weekTemps[5] + weekTemps[6];
let average = sum / weekTemps.length;
console.log("Average temperature:", average.toFixed(1));  // Format to 1 decimal place

// Method 2: Using a loop (alternative solution)
/*
let total = 0;
for (let i = 0; i < weekTemps.length; i++) {
    total += weekTemps[i];
}
let avgTemp = total / weekTemps.length;
console.log("Average temperature:", avgTemp.toFixed(1));
*/

// Method 3: Using reduce (advanced solution)
/*
let avgTemp = weekTemps.reduce((sum, temp) => sum + temp, 0) / weekTemps.length;
console.log("Average temperature:", avgTemp.toFixed(1));
*/

// 4. Find and print the highest temperature
let highestTemp = Math.max(...weekTemps);
console.log("Highest temperature:", highestTemp);  // Should print 80

// 5. Check if any day was above 80 degrees and print a message
// Method 1: Using a simple conditional with the highest temp
if (highestTemp > 80) {
    console.log("It was hot this week!");
} else {
    console.log("It was mild this week.");
}

// Method 2: Loop through each day (alternative solution)
/*
let wasHot = false;
for (let i = 0; i < weekTemps.length; i++) {
    if (weekTemps[i] > 80) {
        wasHot = true;
        break;  // No need to check further
    }
}

if (wasHot) {
    console.log("It was hot this week!");
} else {
    console.log("It was mild this week.");
}
*/

// Method 3: Using some() (advanced solution)
/*
if (weekTemps.some(temp => temp > 80)) {
    console.log("It was hot this week!");
} else {
    console.log("It was mild this week.");
}
*/
```

### Expected Output

```
Monday temperature: 72
Friday temperature: 76
Average temperature: 72.7
Highest temperature: 80
It was mild this week.
```

### Key Concepts Demonstrated

- Creating an array with numeric values
- Accessing array elements by index
- Calculating statistics from array values (sum, average)
- Using `Math.max()` with the spread operator (`...`)
- Using conditional logic with array data
- Various methods to iterate through arrays

## Common Mistakes and How to Avoid Them

### Indexing Issues
Remember that array indices start at 0, not 1. The first element is at index 0, the second at index 1, etc.
```javascript
let array = ["a", "b", "c"];
console.log(array[0]);  // "a" (not array[1])
```

### Length vs. Index
The length of an array is always one more than the highest index.
```javascript
let array = ["a", "b", "c"];
console.log(array.length);  // 3
console.log(array[array.length - 1]);  // "c" (last element)
```

### Adding vs. Changing Elements
Using index assignment (`array[index] = value`) changes an existing element, while methods like `push()` and `unshift()` add new elements.
```javascript
let array = ["a", "b", "c"];
array[1] = "x";  // Changes ["a", "b", "c"] to ["a", "x", "c"]
array.push("d");  // Adds "d" to become ["a", "x", "c", "d"]
```

## Extended Challenges

For students who want more practice:

1. **Sort the temperatures** from lowest to highest using the `sort()` method.
   ```javascript
   weekTemps.sort((a, b) => a - b);
   console.log("Sorted temperatures:", weekTemps);
   ```

2. **Find the temperature range** (difference between highest and lowest).
   ```javascript
   let range = Math.max(...weekTemps) - Math.min(...weekTemps);
   console.log("Temperature range:", range);
   ```

3. **Convert all temperatures to Fahrenheit** if they're in Celsius (or vice versa).
   ```javascript
   // F to C: (F - 32) * 5/9
   // C to F: (C * 9/5) + 32
   let fahrenheitTemps = weekTemps.map(temp => (temp * 9/5) + 32);
   console.log("Temperatures in Fahrenheit:", fahrenheitTemps);
   ```
