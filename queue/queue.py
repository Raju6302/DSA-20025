from __future__ import annotations
from typing import Optional, Any

class Node:
    """
    Represents a node in a linked list-based queue.
    """
    def __init__(self, value: Any) -> None:
        """
        Initializes a Node with the provided value.

        Args:
            value: The value stored in the node.
        """
        self.value: Any = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


class Queue:
    """
    A simple queue implementation using a linked list.

    In a queue, elements are added at the back (enqueue) and removed from the front (dequeue).
    This implementation provides methods for enqueueing, dequeueing, peeking at the front element,
    and checking if the queue is empty.
    """
    def __init__(self) -> None:
        """
        Initializes an empty queue.
        """
        self.head: Optional[Node] = None  # Front of the queue.
        self.tail: Optional[Node] = None  # Rear of the queue.
        self._size: int = 0               # Number of elements in the queue.

    def enqueue(self, value: Any) -> None:
        """
        Adds a new value to the end (rear) of the queue.

        Args:
            value: The value to add to the queue.
        """
        new_node = Node(value)
        if self.tail:
            # If the queue is not empty, append the new node at the end.
            self.tail.next = new_node
        self.tail = new_node  # Update the tail to the new node.
        if not self.head:
            # If the queue was empty, head also points to the new node.
            self.head = new_node
        self._size += 1

    def dequeue(self) -> Optional[Any]:
        """
        Removes and returns the value at the front of the queue.

        Returns:
            The value from the front of the queue, or None if the queue is empty.
        """
        if not self.head:
            return None
        removed_node = self.head
        self.head = self.head.next  # Move head to the next element.
        if self.head is None:
            # If the queue becomes empty, update tail to None as well.
            self.tail = None
        self._size -= 1
        return removed_node.value

    def peek(self) -> Optional[Any]:
        """
        Returns the value at the front of the queue without removing it.

        Returns:
            The value at the front of the queue, or None if the queue is empty.
        """
        return self.head.value if self.head else None

    def is_empty(self) -> bool:
        """
        Checks whether the queue is empty.

        Returns:
            True if the queue has no elements, otherwise False.
        """
        return self._size == 0

    def __len__(self) -> int:
        """
        Returns the number of elements in the queue.

        Returns:
            The size of the queue.
        """
        return self._size

    def __repr__(self) -> str:
        """
        Returns a string representation of the queue.

        Example:
            Queue: 10 -> 20 -> 30
        """
        values = []
        current = self.head
        while current:
            values.append(repr(current.value))
            current = current.next
        return "Queue: " + " -> ".join(values)


# ----------------- Working Example ----------------- #

if __name__ == "__main__":
    # Create an empty queue.
    q = Queue()
    print("Queue is empty?", q.is_empty())

    # Enqueue elements into the queue.
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("After enqueue operations:", q)
    print("Queue size:", len(q))

    # Peek at the front element without removing it.
    print("Front element (peek):", q.peek())

    # Dequeue elements from the queue.
    print("Dequeued element:", q.dequeue())
    print("After one dequeue:", q)
    print("Dequeued element:", q.dequeue())
    print("After another dequeue:", q)
    print("Queue size:", len(q))

    # Enqueue another element.
    q.enqueue(40)
    print("After enqueue 40:", q)

    # Dequeue all elements until the queue is empty.
    while not q.is_empty():
        print("Dequeued:", q.dequeue())
    print("Queue after emptying:", q)