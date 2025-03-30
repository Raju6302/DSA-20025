from __future__ import annotations
from typing import Optional, List
# from binarySearchTree.binary_search_tree import Node

class Node:
    """
    Represents a node in a binary tree.
    
    Attributes:
        value (int): The value stored in the node.
        left (Optional[Node]): The left child.
        right (Optional[Node]): The right child.
    """
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


def preorder_recursive(node: Optional[Node]) -> List[int]:
    """
    Performs recursive pre-order traversal on a binary tree.
    
    Pre-Order Traversal (Node → Left → Right):
      1. Visit the node.
      2. Recursively traverse the left subtree.
      3. Recursively traverse the right subtree.
    
    Pseudocode:
      function preorder(node):
          if node is null:
              return
          visit(node)
          preorder(node.left)
          preorder(node.right)
    
    Args:
        node (Optional[Node]): The root node of the binary tree.
    
    Returns:
        List[int]: A list of node values in pre-order sequence.
    """
    result: List[int] = []
    if node:
        result.append(node.value)
        result.extend(preorder_recursive(node.left))
        result.extend(preorder_recursive(node.right))
    return result


def preorder_iterative(root: Optional[Node]) -> List[int]:
    """
    Performs iterative pre-order traversal on a binary tree using a stack.
    
    Approach:
      1. Initialize a stack with the root node.
      2. While the stack is not empty:
            a. Pop a node from the stack and visit it.
            b. Push its right child (if any) onto the stack.
            c. Push its left child (if any) onto the stack.
         This ensures that the left child is processed first.
    
    Args:
        root (Optional[Node]): The root node of the binary tree.
    
    Returns:
        List[int]: A list of node values in pre-order sequence.
    """
    result: List[int] = []
    if not root:
        return result
    stack: List[Node] = [root]
    while stack:
        current = stack.pop()
        result.append(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result


def preorder_morris(root: Optional[Node]) -> List[int]:
    """
    Performs Morris pre-order traversal on a binary tree without using extra space.
    
    Morris Pre-Order Traversal:
      1. Initialize current as root.
      2. While current is not None:
            a. If current.left is None:
                 - Visit current (append its value).
                 - Move to current.right.
            b. Else:
                 - Find the inorder predecessor (rightmost node in current.left subtree).
                 - If predecessor.right is None:
                      - Visit current.
                      - Set predecessor.right = current (create temporary thread).
                      - Move to current.left.
                 - Else (the thread already exists):
                      - Remove the temporary thread (set predecessor.right to None).
                      - Move to current.right.
    
    Args:
        root (Optional[Node]): The root node of the binary tree.
    
    Returns:
        List[int]: A list of node values in pre-order sequence.
    """
    result: List[int] = []
    current: Optional[Node] = root
    while current:
        if current.left is None:
            result.append(current.value)
            current = current.right
        else:
            # Find the inorder predecessor of current.
            predecessor = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right
            if predecessor.right is None:
                result.append(current.value)  # Visit the current node.
                predecessor.right = current   # Create a temporary thread to current.
                current = current.left
            else:
                predecessor.right = None  # Remove the temporary thread.
                current = current.right
    return result


# ------------------- Working Example ------------------- #

if __name__ == "__main__":
    # Construct a sample binary tree:
    #         4
    #       /   \
    #      2     6
    #     / \   / \
    #    1   3 5   7
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    print("Recursive Pre-Order Traversal:")
    print(preorder_recursive(root))  # Expected: [4, 2, 1, 3, 6, 5, 7]

    print("\nIterative Pre-Order Traversal (Stack):")
    print(preorder_iterative(root))  # Expected: [4, 2, 1, 3, 6, 5, 7]

    print("\nMorris Pre-Order Traversal (Constant Space):")
    print(preorder_morris(root))     # Expected: [4, 2, 1, 3, 6, 5, 7]