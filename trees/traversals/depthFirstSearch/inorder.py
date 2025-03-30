from __future__ import annotations
from typing import Optional, List
# from binarySearchTree.binary_search_tree import Node

class Node:
    """
    Represents a node in a binary tree.
    
    Attributes:
        value (int): The value stored in the node.
        left (Optional[Node]): The left child node.
        right (Optional[Node]): The right child node.
    """
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


def inorder_recursive(node: Optional[Node]) -> List[int]:
    """
    Performs recursive in-order traversal on a binary tree.
    
    In-Order Traversal (Left → Node → Right):
      1. Traverse the left subtree by recursively calling the in-order function.
      2. Visit the node (process its value).
      3. Traverse the right subtree by recursively calling the in-order function.
    
    Pseudocode:
      function inorder(node):
          if node is null:
              return
          inorder(node.left)
          visit(node)
          inorder(node.right)
    
    Args:
        node (Optional[Node]): The root node of the binary tree.
        
    Returns:
        List[int]: A list of node values in in-order sequence.
    """
    result: List[int] = []
    if node:
        result.extend(inorder_recursive(node.left))
        result.append(node.value)
        result.extend(inorder_recursive(node.right))
    return result


def inorder_iterative(root: Optional[Node]) -> List[int]:
    """
    Performs iterative in-order traversal on a binary tree using a stack.
    
    Approach:
      1. Initialize an empty stack.
      2. Set the current node to the root.
      3. While the stack is not empty or the current node is not None:
         a. Push all the left children of the current node onto the stack.
         b. Pop a node from the stack, visit it (append its value to result), and set
            the current node to its right child.
    
    This method avoids recursion and uses an explicit stack.
    
    Args:
        root (Optional[Node]): The root node of the binary tree.
        
    Returns:
        List[int]: A list of node values in in-order sequence.
    """
    result: List[int] = []
    stack: List[Node] = []
    current: Optional[Node] = root

    while stack or current:
        # Reach the leftmost node of the current node
        while current:
            stack.append(current)
            current = current.left
        # Current must be None at this point, so pop from stack
        current = stack.pop()
        result.append(current.value)
        # Visit the right subtree
        current = current.right

    return result


def morris_traversal(root: Optional[Node]) -> List[int]:
    """
    Performs Morris Traversal on a binary tree to retrieve in-order sequence without extra space.
    
    Approach (Morris Traversal):
      1. Initialize current as root.
      2. While current is not None:
         a. If current.left is None:
             - Visit current (append its value).
             - Move to current.right.
         b. Else:
             - Find the rightmost node in current's left subtree (predecessor).
             - If predecessor.right is None, set it to current (create temporary link) and
               move current to current.left.
             - Else (the temporary link already exists), remove it, visit current, and
               move to current.right.
    
    Morris traversal uses the tree's unused right pointers to temporarily link nodes,
    achieving O(1) space complexity (ignoring the output list).
    
    Args:
        root (Optional[Node]): The root node of the binary tree.
        
    Returns:
        List[int]: A list of node values in in-order sequence.
    """
    result: List[int] = []
    current: Optional[Node] = root

    while current:
        if not current.left:
            result.append(current.value)
            current = current.right
        else:
            # Find the inorder predecessor of current
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                # Establish temporary link to current
                predecessor.right = current
                current = current.left
            else:
                # Temporary link exists, so remove it and visit current
                predecessor.right = None
                result.append(current.value)
                current = current.right

    return result


# ------------------- Working Example ------------------- #

if __name__ == "__main__":
    # Create a sample binary search tree:
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

    print("Recursive In-Order Traversal:")
    print(inorder_recursive(root))  # Expected: [1, 2, 3, 4, 5, 6, 7]

    print("\nIterative In-Order Traversal:")
    print(inorder_iterative(root))  # Expected: [1, 2, 3, 4, 5, 6, 7]

    print("\nMorris In-Order Traversal (Constant space):")
    print(morris_traversal(root))   # Expected: [1, 2, 3, 4, 5, 6, 7]