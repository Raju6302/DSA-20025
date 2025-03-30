from __future__ import annotations
from typing import List, Optional

class MinHeap:
    """
    A Min Heap implementation using a list as the underlying storage.
    
    A Min Heap is a complete binary tree where each node is smaller than or equal 
    to its children. This implementation supports basic operations such as insertion,
    removal of the minimum element, and peeking at the minimum element.
    """

    def __init__(self, elements: Optional[List[int]] = None) -> None:
        """
        Initializes a new MinHeap. Optionally builds the heap from an initial list of elements.
        
        Args:
            elements: An optional list of integers to initialize the heap.
        """
        self.heap: List[int] = elements[:] if elements is not None else []
        if elements:
            self._build_heap()

    def _build_heap(self) -> None:
        """
        Converts the current list into a valid heap in-place.
        """
        n = len(self.heap)
        # A heap is a complete binary tree, meaning every level (except possibly the last) is completely filled, and all nodes are as far left as possible.

        # In an array representation of a binary tree (using 0-indexing), the leaves are the nodes in the second half of the array (indices n//2 to n-1). These nodes are already heaps (since they have no children), so we don't need to heapify them.

        # The last node that has children is at index n // 2 - 1.
        # Start from the last parent node and heapify down each node.
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index: int) -> None:
        """
        Maintains the min heap property by shifting the element at the given index downwards.
        
        Args:
            index: The index of the element to heapify down.
        """

        # In an array representation of a binary tree:
          # -> The left child of a node at index i is at 2 * i + 1.
          # -> The right child of a node at index i is at 2 * i + 2.

        # This formula comes from the properties of complete binary trees
        
        n = len(self.heap)
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            # Swap and continue heapifying down.
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def _heapify_up(self, index: int) -> None:
        """
        Maintains the min heap property by shifting the element at the given index upwards.
        
        Args:
            index: The index of the element to heapify up.
        """
        # In a 0-indexed array representation of a binary tree, the parent of the node at index i is located at (i - 1) // 2.
        parent = (index - 1) // 2 
        while index > 0 and self.heap[index] < self.heap[parent]:
            # Swap element with its parent.
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def push(self, value: int) -> None:
        """
        Inserts a new value into the heap.
        
        Args:
            value: The integer value to insert.
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self) -> Optional[int]:
        """
        Removes and returns the smallest element from the heap.
        
        Returns:
            The smallest integer in the heap, or None if the heap is empty.
        """
        if not self.heap:
            return None
        min_value = self.heap[0]
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            self._heapify_down(0)
        return min_value

    def peek(self) -> Optional[int]:
        """
        Returns the smallest element without removing it.
        
        Returns:
            The smallest integer in the heap, or None if the heap is empty.
        """
        return self.heap[0] if self.heap else None

    def __len__(self) -> int:
        """
        Returns the number of elements in the heap.
        
        Returns:
            The size of the heap.
        """
        return len(self.heap)

    def __repr__(self) -> str:
        """
        Returns a string representation of the heap.
        """
        return f"MinHeap({self.heap})"


# ------------------ Working Example ------------------ #

if __name__ == "__main__":
    # Create an empty MinHeap.
    min_heap = MinHeap()

    # Insert elements into the heap.
    for value in [5, 3, 8, 1, 2, 9]:
        min_heap.push(value)
        print(f"After pushing {value}: {min_heap}")

    print("\nCurrent heap:", min_heap)
    print("Minimum element (peek):", min_heap.peek())

    # Remove elements one by one.
    while len(min_heap) > 0:
        popped = min_heap.pop()
        print(f"Popped {popped}, heap now: {min_heap}")

    # Build a heap from a list of elements.
    print("\nBuilding heap from list [10, 4, 7, 1, 3]:")
    heap_from_list = MinHeap([10, 4, 7, 1, 3])
    print(heap_from_list)