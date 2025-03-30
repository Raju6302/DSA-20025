from __future__ import annotations
from typing import Optional, List
from collections import deque

# Minimal Node definition for demonstration.
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


def level_order(root: Optional[Node]) -> List[int]:
    """
    Performs level order traversal on a binary tree.
    
    Level Order Traversal (Breadth-First Search):
      1. Start at the root node.
      2. Visit nodes level by level from left to right.
      3. Use a queue (FIFO) to keep track of nodes at the current level.
    
    Pseudocode:
      function levelOrder(root):
          if root is null:
              return []
          initialize queue with root
          initialize result as empty list
          while queue is not empty:
              current = dequeue from queue
              add current.value to result
              if current.left exists, enqueue current.left
              if current.right exists, enqueue current.right
          return result
    
    Args:
        root (Optional[Node]): The root node of the binary tree.
    
    Returns:
        List[int]: A list of node values in level order.
    """
    result: List[int] = []
    if not root:
        return result
    
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
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
    
    print("Level Order Traversal:")
    print(level_order(root))  # Expected output: [4, 2, 6, 1, 3, 5, 7]