# 🏗️ Heap Data Structure (Min Heap)

*A specialized complete binary tree that satisfies the heap property for efficient priority queue operations*

## Table of Contents
- [🏗️ Heap Data Structure (Min Heap)](#️-heap-data-structure-min-heap)
  - [Table of Contents](#table-of-contents)
  - [📖 Overview](#-overview)
  - [🔑 Core Properties](#-core-properties)
  - [🛠️ Basic Operations](#️-basic-operations)
    - [➕ Insertion](#-insertion)
      - [How Insertion Works](#how-insertion-works)
      - [Pseudocode for Insertion](#pseudocode-for-insertion)
    - [Insertion Visualization](#insertion-visualization)
    - [🕒 Complexity Analysis](#-complexity-analysis)
  - [🔍 Extraction](#-extraction)
    - [How Extraction Works](#how-extraction-works)
    - [Pseudocode for Extraction](#pseudocode-for-extraction)
    - [Extraction Visualization](#extraction-visualization)
    - [🕒 Complexity](#-complexity)
  - [⚖️ Tradeoffs Analysis](#️-tradeoffs-analysis)
    - [✅ Advantages](#-advantages)
    - [❌ Challenges](#-challenges)
  - [🧠 Key Implementation Notes](#-key-implementation-notes)
    - [Array Representation](#array-representation)
    - [Heapify Operations](#heapify-operations)
    - [Iterative vs. Recursive Approaches](#iterative-vs-recursive-approaches)
  - [📈 Complexity Comparison Table](#-complexity-comparison-table)
  - [🔗 Related Structures](#-related-structures)
    - [Priority Queues](#priority-queues)
    - [Advanced Variants](#advanced-variants)
  - [🚀 Further Reading](#-further-reading)
  - [👥 Contributors Welcome!](#-contributors-welcome)

---

## 📖 Overview
- **Complete Binary Tree**: A Heap is always a complete binary tree.
- **Heap Property**:  
  - In a **Min Heap**, each parent node is **less than or equal** to its children.
  - In a **Max Heap**, each parent node is **greater than or equal** to its children.
- **Key Applications**:
  - Priority queues
  - Heap sort
  - Graph algorithms (e.g., Dijkstra’s shortest path, Prims's)
  - Scheduling systems

---

## 🔑 Core Properties
1. **Structural Property**: Complete binary tree shape - All levels are fully filled except possibly the last, which is filled from left to right.
2. **Heap Property (Min Heap)**: Every parent node's value is ≤ its children’s values.
3. **Efficient Operations**: O(1) to access to root element, Insertion and extraction (removal of the root) can be done in O(log n) time.
4. **Array Implementation**: Typically stored as array
---

## 🛠️ Basic Operations

### ➕ Insertion

#### How Insertion Works
1. **Insert at End**: Add the new element to the end of the heap (maintaining the complete tree property).
2. **Bubble Up (percolate up)**: Compare the new element with its parent.  
   - If the new element is smaller than its parent, swap them.
   - Continue this process until the new element is in the correct position or becomes the root.

#### Pseudocode for Insertion
```pseudo
Insert(heap, value):
    Append value to heap array
    index = last index of heap
    While index > 0:
        parent = (index - 1) // 2
        If heap[index] < heap[parent]:
            Swap(heap[index], heap[parent])
            index = parent
        Else:
            Break
```

### Insertion Visualization
![Insertion Visualization](https://cdn.devdojo.com/images/january2022/insertInHeap.gif) 

*Visualization courtesy of DevDojo.*

### 🕒 Complexity Analysis

| Case        | Time Complexity | Space Complexity |
|-----------------|-----------------|------------------|
| **Best/Average/Worst** | O(log n)        | O(1)            |

---

## 🔍 Extraction

### How Extraction Works

1. Remove the Root: The minimum element in a Min Heap is at the root.
2. Replace Root: Replace the root with the last element in the heap.
3. Bubble Down (Heapify Down): Compare the new root with its children.
   - Swap it with the smaller child if it is greater than that child.
   - Continue until the heap property is restored.

### Pseudocode for Extraction

```pseudo
ExtractMin(heap):
    If heap is empty:
        Return null
    minValue = heap[0]
    heap[0] = heap[last index]
    Remove last element from heap
    index = 0
    While index has a left child:
        left = 2 * index + 1
        right = 2 * index + 2
        smallerChild = left
        If right exists and heap[right] < heap[left]:
            smallerChild = right
        If heap[index] > heap[smallerChild]:
            Swap(heap[index], heap[smallerChild])
            index = smallerChild
        Else:
            Break
    Return minValue
```
### Extraction Visualization
![LookUp Visualization](https://media.geeksforgeeks.org/wp-content/uploads/20230324134257/minheap-.png)

*Animation showing removal of the root and subsequent heapification.*

### 🕒 Complexity

| Case        | Time Complexity | Space Complexity |
|-----------------|-----------------|------------------|
| **Best/Average/Worst** | O(log n)        | O(1)            |

---

## ⚖️ Tradeoffs Analysis

### ✅ Advantages
- **Optimal Extraction**: O(1) access to min/max element
- **Efficient Sorting**: Heap Sort achieves O(n log n)  
- **Space Efficient**: Array implementation uses minimal overhead  

### ❌ Challenges
- **Not Sorted Globally**: Only the root is guaranteed to be the smallest, the rest of the array isn’t fully sorted.
- **Fixed Order**: Only root element is directly accessible.
- **Search Limitations**: O(n) search for arbitrary elements.
- **Balance Dependency**: Heaps are inherently balanced (complete trees), but ensuring complete structure can complicate dynamic resizing.

---

## 🧠 Key Implementation Notes

### Array Representation
*Why use array?*  
 - Parent-child relationships calculable via indices
 - Index Formulas
   - Left Child: 2 * index + 1
   - Right Child: 2 * index + 2
   - Parent: (index - 1) // 2   

### Heapify Operations
- **Bubble Up**: Used after insertion to restore the heap property.
- **Bubble Down**: Used after extraction (or deletion) to re-establish the heap property. 

### Iterative vs. Recursive Approaches
- **Iterative** methods (as shown) are preferred for heaps due to their constant space (O(1)) overhead
- Recursive implementations exist but may lead to stack overflow with very large heaps 

---

## 📈 Complexity Comparison Table

| Operation | Heap       | BST (Avg) | Array  | Linked List |
|-----------|------------|-----------|--------|-------------|
| Insert    | O(log n)   | O(log n)  | O(n)   | O(1)        |
| Extract   | O(log n)   | N/A       | N/A    | N/A         |
| Search    | O(n)       | O(log n)  | O(1)   | O(n)        |

## 🔗 Related Structures

### Priority Queues
- [Binary Heap](https://www.geeksforgeeks.org/binary-heap/)
- [Fibonacci Heap](https://www.geeksforgeeks.org/fibonacci-heap-set-1-introduction/)

### Advanced Variants
- [Binomial Heap](https://www.geeksforgeeks.org/binomial-heap-2/)
- [Pairing Heap](https://www.geeksforgeeks.org/pairing-heap/)

## 🚀 Further Reading
- [Heap Applications in Real Systems](https://www.geeksforgeeks.org/applications-of-heap-data-structure/)  
- [Heap Sort Visualized](https://www.hackerearth.com/practice/algorithms/sorting/heap-sort/tutorial/)  
- [Interactive Heap Visualization](https://www.cs.usfca.edu/~galles/visualization/Heap.html)

---

## 👥 Contributors Welcome!  
![Open in GitHub](https://img.shields.io/badge/Contribute-GitHub-brightgreen?logo=github)

---
*Happy coding and happy learning! This repository is designed to be a go-to resource for understanding DSA fundamentals, and we welcome contributions and improvements from the community.*