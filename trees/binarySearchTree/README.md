# 🌳 Binary Search Tree (BST) 

*A hierarchical data structure that maintains sorted order for efficient search/insert operations*

## Table of Contents
- [🌳 Binary Search Tree (BST)](#-binary-search-tree-bst)
  - [Table of Contents](#table-of-contents)
  - [📖 Overview](#-overview)
  - [🔑 Core Properties](#-core-properties)
  - [🛠️ Basic Operations](#️-basic-operations)
  - [➕ Insertion](#-insertion)
    - [How Insertion Works](#how-insertion-works)
    - [Pseudocode for Insertion](#pseudocode-for-insertion)
    - [Insertion Visualization](#insertion-visualization)
    - [🕒 Complexity Analysis](#-complexity-analysis)
  - [🔍 Lookup](#-lookup)
    - [How Lookup Works](#how-lookup-works)
    - [Pseudocode for Lookup](#pseudocode-for-lookup)
    - [Lookup Visualization](#lookup-visualization)
    - [🕒 Complexity](#-complexity)
  - [⚖️ Tradeoffs Analysis](#️-tradeoffs-analysis)
    - [✅ Advantages](#-advantages)
    - [❌ Challenges](#-challenges)
  - [🧠 Key Implementation Notes](#-key-implementation-notes)
    - [Duplication Handling](#duplication-handling)
    - [Recursive vs Iterative](#recursive-vs-iterative)
    - [Null Checks](#null-checks)
  - [📈 Complexity Comparison Table](#-complexity-comparison-table)
  - [🔗 Related Structures](#-related-structures)
    - [Self-Balancing Trees](#self-balancing-trees)
    - [Space Optimization](#space-optimization)
  - [🚀 Further Reading](#-further-reading)
  - [👥 Contributors Welcome!](#-contributors-welcome)

## 📖 Overview
- **Hierarchical Structure**: Each node has ≤ 2 children
- **Order Property**: 
  - Left subtree values < Node value < Right subtree values
- **Key Applications**:
  - Database indexing
  - Filesystem hierarchies
  - Auto-completion features

## 🔑 Core Properties
1. **Left Subtree Rule**: All left descendants ≤ parent node
2. **Right Subtree Rule**: All right descendants ≥ parent node
3. **Uniqueness**: No duplicate values allowed
4. **Recursive Structure**: Subtrees must also follow BST rules

## 🛠️ Basic Operations

## ➕ Insertion

### How Insertion Works
1. If the tree is empty, the new node becomes the **root**.
2. Start at the root and compare the new value with the current node’s value.
3. If the new value is **smaller**, move to the **left subtree**.
4. If the new value is **greater**, move to the **right subtree**.
5. Repeat until an empty position is found, then insert the new node.

### Pseudocode for Insertion
```pseudo
InsertNode(root, value):
    Create a new node with given value
    If root is NULL:
        root = new node
        Return true

    temp = root
    While true:
        If value == temp.value:
            Return false  // No duplicates allowed

        If value < temp.value:
            If temp.left is NULL:
                temp.left = new node
                Return true
            Move temp to temp.left
        Else:
            If temp.right is NULL:
                temp.right = new node
                Return true
            Move temp to temp.right
```

### Insertion Visualization
![Insertion Visualization](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Binary-search-tree-insertion-animation.gif/640px-Binary-search-tree-insertion-animation.gif)  

### 🕒 Complexity Analysis

| Case        | Time Complexity | Space Complexity |
|-----------------|-----------------|------------------|
| **Best/Average** | O(log n)        | O(1) (iterative approach)            |
| **Worst (Skewed)**   | O(n)            | O(1) (iterative approach)           |

---

## 🔍 Lookup

### How Lookup Works

1. Start at the root and compare the target value with the current node’s value.
2. If the target value is equal to the current node’s value, return true (value found).
3. If the target value is smaller, move to the left subtree.
4. If the target value is greater, move to the right subtree.
5. If the search reaches a NULL node, return false (value not found).

### Pseudocode for Lookup

```pseudo
Lookup(root, value):
    temp = root
    While temp is NOT NULL:
        If temp.value == value:
            Return true
        If value < temp.value:
            Move temp to temp.left
        Else:
            Move temp to temp.right
    Return false

```
### Lookup Visualization
![LookUp Visualization](https://upload.wikimedia.org/wikipedia/commons/9/9b/Binary_search_tree_example.gif)
### 🕒 Complexity

| Scenario        | Time Complexity | Space Complexity |
|-----------------|-----------------|------------------|
| **Balanced Tree** | O(log n)        | O(1)             |
| **Skewed Tree**   | O(n)            | O(1)             |

---

## ⚖️ Tradeoffs Analysis

### ✅ Advantages
- **Efficient Operations**: O(log n) for balanced trees  
- **Order Maintenance**: Automatic sorting during insertion  
- **Flexible Size**: Dynamic memory allocation  

### ❌ Challenges
- **Balance Dependency**: If the tree becomes unbalanced, performance can degrade to O(n), similar to a linked list.
- **Complex Balancing**: Requires the use of self-balancing trees like AVL/Red-Black Trees for optimization. 

---

## 🧠 Key Implementation Notes

### Duplication Handling
*Why prevent duplicates?*  
Maintains strict ordering for predictable behavior  

### Recursive vs Iterative
- **Recursive**: Cleaner code but risks stack overflow  
- **Iterative**: Better for large trees, manual stack management  

### Null Checks
Essential for preventing null pointer exceptions  

---

## 📈 Complexity Comparison Table

| Operation | BST (Avg) | BST (Worst) | Array  | Linked List |
|-----------|-----------|-------------|--------|-------------|
| Insert    | O(log n)  | O(n)        | O(n)   | O(1)        |
| Search    | O(log n)  | O(n)        | O(1)   | O(n)        |
| Delete    | O(log n)  | O(n)        | O(n)   | O(n)        |

---

## 🔗 Related Structures

### Self-Balancing Trees
- [AVL Tree](https://en.wikipedia.org/wiki/AVL_tree)
- [Red-Black Tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)

### Space Optimization
- [B-Tree](https://en.wikipedia.org/wiki/B-tree) (for disk storage)

---

## 🚀 Further Reading
- [BST Applications in Databases](https://www.geeksforgeeks.org/applications-of-bst/)  
- [Balancing Techniques Deep Dive](https://hayksimonyan.substack.com/p/deep-dive-into-binary-avl-and-red)  
- [Interactive BST Visualization](https://www.cs.usfca.edu/~galles/visualization/BST.html) **(highly recommended!)**

---

## 👥 Contributors Welcome!  
![Open in GitHub](https://img.shields.io/badge/Contribute-GitHub-brightgreen?logo=github)

---
*Happy coding and happy learning! This repository is designed to be a go-to resource for understanding DSA fundamentals, and we welcome contributions and improvements from the community.*