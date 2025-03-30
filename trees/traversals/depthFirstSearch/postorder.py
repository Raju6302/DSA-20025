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


def postorder_recursive(node: Optional[Node]) -> List[int]:
    """
    Performs recursive post-order traversal on a binary tree.
    
    Post-Order Traversal (Left → Right → Node):
      1. Traverse the left subtree by recursively calling postorder.
      2. Traverse the right subtree by recursively calling postorder.
      3. Visit the node (process its value).
    
    Pseudocode:
      function postorder(node):
          if node is null:
              return
          postorder(node.left)
          postorder(node.right)
          visit(node)
    
    Args:
        node (Optional[Node]): The root node of the binary tree.
    
    Returns:
        List[int]: A list of node values in post-order sequence.
    """
    result: List[int] = []
    if node:
        result.extend(postorder_recursive(node.left))
        result.extend(postorder_recursive(node.right))
        result.append(node.value)
    return result


def postorder_iterative(root: Optional[Node]) -> List[int]:
    """
    Performs iterative post-order traversal on a binary tree using two stacks.
    
    Approach:
      1. Push the root node onto the first stack.
      2. While the first stack is not empty:
           a. Pop a node from the first stack and push it onto the second stack.
           b. Push the left child (if exists) onto the first stack.
           c. Push the right child (if exists) onto the first stack.
      3. Once the first stack is empty, pop all nodes from the second stack;
         this yields the nodes in post-order (Left → Right → Node).
    
    Args:
        root (Optional[Node]): The root node of the binary tree.
    
    Returns:
        List[int]: A list of node values in post-order sequence.
    """
    result: List[int] = []
    if not root:
        return result
    stack1: List[Node] = [root]
    stack2: List[Node] = []
    
    while stack1:
        current = stack1.pop()
        stack2.append(current)
        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)
    
    while stack2:
        result.append(stack2.pop().value)
    
    return result


def postorder_iterative_one_stack(root: Optional[Node]) -> List[int]:
    """
    Performs iterative post-order traversal on a binary tree using one stack.
    
    Approach (One-Stack Method):
      1. Initialize an empty stack and set `current` to root. Also, maintain a pointer
         `last_visited` to track the last node that was visited.
      2. Traverse the tree:
         a. If current is not None, push it onto the stack and move to its left child.
         b. If current is None, peek at the node on the top of the stack.
            - If the peeked node has a right child that hasn't been visited yet,
              set current to that right child.
            - Otherwise, pop the node from the stack, visit it (append its value to result),
              and mark it as the last visited node.
      3. Continue until both the stack is empty and current is None.
    
    Pseudocode:
      initialize stack, last_visited = None, current = root
      while stack is not empty or current is not None:
          if current is not None:
              push current onto stack
              current = current.left
          else:
              peek_node = top of stack
              if peek_node.right exists and last_visited != peek_node.right:
                  current = peek_node.right
              else:
                  pop from stack, visit node, update last_visited
    
    Args:
        root (Optional[Node]): The root node of the binary tree.
    
    Returns:
        List[int]: A list of node values in post-order sequence.
    """
    result: List[int] = []
    stack: List[Node] = []
    last_visited: Optional[Node] = None
    current: Optional[Node] = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            # If right child exists and hasn't been visited, traverse right subtree.
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                result.append(peek_node.value)
                last_visited = stack.pop()
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

    print("Recursive Post-Order Traversal:")
    print(postorder_recursive(root))  # Expected: [1, 3, 2, 5, 7, 6, 4]

    print("\nIterative Post-Order Traversal (Two Stacks):")
    print(postorder_iterative(root))  # Expected: [1, 3, 2, 5, 7, 6, 4]

    print("\nIterative Post-Order Traversal (One Stack):")
    print(postorder_iterative_one_stack(root))  # Expected: [1, 3, 2, 5, 7, 6, 4]