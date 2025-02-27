# 🎲 The Doomed Dice Challenge  

  This project solves the **Doomed Dice Challenge**, a mathematical probability problem involving rolling two six-sided dice and modifying them under constraints.  

The challenge is divided into two parts:  

- **Part A:** Compute dice roll combinations, sum distributions, and probabilities.  
- **Part B:** Modify dice under Loki’s constraints while keeping probabilities unchanged.  

## 📌 Part A: Dice Probability Analysis  
### 🔹 Problem Statement  
Given two six-sided dice, **Die A** and **Die B**, we calculate:  
1. The total number of possible combinations.  
2. The frequency of each possible sum (distribution).  
3. The probability of obtaining each sum.  

### 🔹 Code Explanation  
- **`calculate_combinations()`**: Finds total possible dice rolls.  
- **`calculate_distribution()`**: Counts occurrences of each sum.  
- **`calculate_probabilities()`**: Computes probabilities for each sum.  

### 🔹 Example Output  

Total possible combinations: 36

Sum distribution: Sum 2: 1 times Sum 3: 2 times Sum 4: 3 times ... Sum 12: 1 times

Probability of each sum: P(Sum=2) = 0.0278 P(Sum=3) = 0.0556 ... P(Sum=12) = 0.0278


## 📌 Part B: Rebuilding the Doomed Dice  
### 🔹 Problem Statement  
Loki removes the spots from our dice. We must **reassign numbers** such that:  
- **Die A** can have numbers only from 1 to 4.  
- **Die B** can take any number (even greater than 6).  
- The probability of sums must remain the same.  

### 🔹 Code Explanation  
- **`calculate_distribution()`**: Finds original probability distribution.  
- **`undoom_dice()`**: Modifies the dice while maintaining sum probabilities.  

### 🎲 New Dice Values  
New Die A: [1, 2, 3, 4, 1, 2] New Die B: [6, 5, 4, 3, 6, 5]





