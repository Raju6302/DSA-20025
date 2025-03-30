from __future__ import annotations
from typing import Optional
from typing import List
from traversals.depthFirstSearch.preorder import preorder_iterative, preorder_morris, preorder_recursive
from traversals.depthFirstSearch.inorder import inorder_iterative, inorder_recursive, morris_traversal
from traversals.depthFirstSearch.postorder import postorder_iterative, postorder_recursive
from traversals.breadthFirstSearch.levelorder import level_order

class Node:
    """
    Represents a node in a Binary Search Tree (BST).
    
    Attributes:
        value: The value stored in the node.
        left: Reference to the left child (subtree with smaller values).
        right: Reference to the right child (subtree with larger values).
    """
    def __init__(self, value: int) -> None:
        """
        Initializes a Node with a given value.
        
        Args:
            value: The integer value to store in the node.
        """
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


class BinarySearchTree:
    """
    Implements a Binary Search Tree (BST).
    
    A BST is a node-based binary tree data structure which maintains the property that
    for any given node, the values in its left subtree are less than its value, and the
    values in its right subtree are greater than its value.
    """
    def __init__(self) -> None:
        """
        Initializes an empty Binary Search Tree.
        """
        self.root: Optional[Node] = None

    def insert(self, value: int) -> None:
        """
        Inserts a new value into the BST.
        
        Args:
            value: The integer value to insert.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Optional[Node], value: int) -> Node:
        """
        Helper method to insert a value recursively in the BST.
        
        Args:
            node: The current node in the recursive traversal.
            value: The value to insert.
        
        Returns:
            The updated node after insertion.
        """
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # If the value already exists, we do not insert duplicates.
        return node

    def search(self, value: int) -> Optional[Node]:
        """
        Searches for a node with the specified value in the BST.
        
        Args:
            value: The value to search for.
        
        Returns:
            The Node containing the value, or None if not found.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[Node], value: int) -> Optional[Node]:
        """
        Helper method to search for a value recursively.
        
        Args:
            node: The current node in the recursive traversal.
            value: The value to search for.
        
        Returns:
            The Node containing the value, or None if not found.
        """
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value: int) -> None:
        """
        Deletes a node with the specified value from the BST.
        
        Args:
            value: The value to delete.
        """
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node: Optional[Node], value: int) -> Optional[Node]:
        """
        Helper method to delete a node recursively.
        
        Args:
            node: The current node in the recursive traversal.
            value: The value to delete.
        
        Returns:
            The updated node after deletion.
        """
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with the value found.
            # Case 1: Node is a leaf.
            if node.left is None and node.right is None:
                return None
            # Case 2: Node has one child.
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3: Node has two children.
            # Find the inorder successor (smallest in the right subtree).
            successor = self._find_min(node.right)
            # Replace node's value with successor's value.
            node.value = successor.value
            # Delete the inorder successor.
            node.right = self._delete_recursive(node.right, successor.value)
        return node

    def _find_min(self, node: Node) -> Node:
        """
        Finds the node with the minimum value in a BST (leftmost node).
        
        Args:
            node: The root node of the subtree.
        
        Returns:
            The node with the minimum value.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def __repr__(self) -> str:
        """
        Returns a string representation of the BST via in-order traversal.
        """
        # Here we use the recursive in-order traversal imported from traversals.inorder.
        traversal: List[int] = inorder_recursive(self.root)
        return "BinarySearchTree(" + str(traversal) + ")"


# ------------------ Working Example ------------------ #

if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Insert values into the BST.
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    for value in values_to_insert:
        bst.insert(value)
    print("BST (using recursive in-order traversal):")
    print(bst)

    # Search for a value.
    search_val = 40
    found_node = bst.search(search_val)
    print(f"\nSearching for {search_val}:")
    print(found_node if found_node else f"Value {search_val} not found.")

    # Delete a value.
    delete_val = 30
    bst.delete(delete_val)
    print(f"\nBST after deleting {delete_val}:")
    print(bst)


    # Traversal Methods practical demonstration:

    print("\nDepth First Search Traversals:")

    print("\nIn-Order Traversals:")
    print("In-order Iterative traversal of BST (sorted values):", inorder_iterative(bst.root))
    print("In-order Morris traversal of BST (sorted values):", morris_traversal(bst.root))

    print("\nPre-Order Traversals:")
    print("Pre-order (Recursive):", preorder_recursive(bst.root))
    print("Pre-order (Iterative):", preorder_iterative(bst.root))
    print("Pre-order (Morris Iterative):", preorder_morris(bst.root))

    print("\nPost-Order Traversals:")
    print("Post-order (Recursive):", postorder_recursive(bst.root))
    print("Post-order (Iterative):", postorder_iterative(bst.root))

    print("\nBreadth First Search Traversals:")

    print("\nLevel-Order Traversal:", level_order(bst.root))
