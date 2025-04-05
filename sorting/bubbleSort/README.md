# 🫧 Bubble Sort

*A simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.*

## Table of Contents
- [🫧 Bubble Sort](#-bubble-sort)
  - [📖 Overview](#-overview)
  - [⚙️ How It Works](#️-how-it-works)
  - [🔁 Pseudocode](#-pseudocode)
  - [💻 Java Implementation](#-java-implementation)
  - [🎞️ Visualization](#-visualization)
  - [🕒 Complexity Analysis](#-complexity-analysis)
  - [⚖️ Tradeoffs Analysis](#️-tradeoffs-analysis)
    - [✅ Advantages](#-advantages)
    - [❌ Disadvantages](#-disadvantages)
  - [🧠 Key Implementation Notes](#-key-implementation-notes)
    - [Optimized Version](#optimized-version)
    - [Stable Sort](#stable-sort)
  - [📈 Comparison with Other Sorts](#-comparison-with-other-sorts)
  - [🔗 Related Algorithms](#-related-algorithms)
  - [🚀 Further Reading](#-further-reading)
  - [👥 Contributors Welcome!](#-contributors-welcome)

---

## 📖 Overview

- **Type**: Comparison-based sorting algorithm
- **Strategy**: Repeatedly swaps adjacent elements if they are in the wrong order
- **In-place**: Yes
- **Stable**: Yes

---

## ⚙️ How It Works

1. Traverse the array from the beginning.
2. Compare each pair of adjacent elements.
3. Swap them if the left element is greater than the right.
4. Repeat until no swaps are needed (array is sorted).

---

## 🔁 Pseudocode

```pseudo
bubbleSort(arr):
    n = length of arr
    for i = 0 to n-2:
        swapped = false
        for j = 0 to n-2-i:
            if arr[j] > arr[j+1]:
                swap arr[j] and arr[j+1]
                swapped = true
        if not swapped:
            break
```

🎞️ Visualization

![Bubble Sort Visualization](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)


### 🕒 Complexity

| Case        | Time Complexity | Space Complexity |
|-----------------|-----------------|------------------|
| **Best** | O(n) (when array is already sorted)        | O(1)             |
| **Average**   | O(n²)            | O(1)             |
| **Worst**   | O(n²)            | O(1)             |


⚖️ Tradeoffs Analysis

  ✅ Advantages
    Simple to implement

    Stable: Maintains the relative order of equal elements

    Good for small or nearly sorted data

  ❌ Disadvantages
    Inefficient for large datasets due to O(n²) time

    Redundant comparisons in worst cases

🧠 Key Implementation Notes
Optimized Version
  Use a `swapped` flag to break early if no swaps occurred (already sorted).

Stable Sort
Bubble Sort is stable: it does not change the relative order of equal elements.

