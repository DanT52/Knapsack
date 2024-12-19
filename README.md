# Knapsack Problem Solver

This project is a comprehensive implementation of the classic 0/1 Knapsack Problem. The objective is to maximize the total value of selected items while ensuring their total weight does not exceed a given limit. The solution is implemented in both C++ and Python.

---

## Features

### Implementation
- Uses a dynamic programming (iterative bottom up) approach to solve the knapsack problem efficiently.
- Tracks the selected items, total weight, and total value.
- Reads input from `stdin` and processes items defined in the format:
  ```
  item-name;item-weight;item-value
  ```
- Outputs the selected items in the order they appear in the input, followed by the total weight and total value.


### Testing Utility
- A testing script is provided to validate the implementation using sample inputs and expected outputs.
- Uses subprocesses to run the implementations and compare their outputs against the expected results.

---

## Input Format

The input consists of the maximum weight of the knapsack followed by a list of items. Each item is represented in the format:
```
item-name;item-weight;item-value
```
**Constraints:**
- Maximum weight: 1200
- Maximum number of items: 128
- Maximum length of item name: 127 characters

### Example Input
```
120
rusty mail leggings;10;2
electric piano;110;1500
battery-powered skateboard;4;100
boxing gloves;1;50
diamond-studded boxing gloves;1;2500
grand piano;120;2499
```

---

## Output Format

The output includes:
1. A list of selected items, with each item on a new line in the format:
   ```
    item-name, item-weight, item-value
   ```
2. Total weight and total value of the selected items:
   ```
    final weight: X
    final value: Y
   ```
### Example Output
```
diamond-studded boxing gloves, 1, 2500
battery-powered skateboard, 4, 100

final weight: 5
final value: 2600
```

---

## How to Run

### C++ Implementation
1. Compile the program:
   ```
   g++ -o knapsack knapsack.cpp
   ```
2. Run the program and provide input:
   ```
   ./knapsack < input.txt
   ```

### Python Implementation
1. Run the Python script:
   ```
   python3 knapsack.py < input.txt
   ```