from __future__ import annotations
from typing import Optional, Iterator, List

class Node:
    """
    Represents a node in a circular linked list.
    """
    def __init__(self, value: int) -> None:
        """
        Initializes a Node with a given value.

        Args:
            value: The integer value stored in the node.
        """
        self.value: int = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return str(self.value)


class CircularLinkedList:
    """
    Implements a circular linked list where the tail node's next pointer refers back to the head.
    """
    def __init__(self) -> None:
        """
        Initializes an empty circular linked list.
        """
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length: int = 0

    def append(self, value: int) -> None:
        """
        Appends a new node with the specified value to the end of the circular linked list.

        Args:
            value: The integer value to append.
        """
        new_node = Node(value)
        if not self.head:
            # List is empty; initialize head and tail.
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # Circular reference.
        else:
            assert self.tail is not None
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value: int) -> None:
        """
        Prepends a new node with the specified value to the beginning of the circular linked list.

        Args:
            value: The integer value to prepend.
        """
        new_node = Node(value)
        if not self.head:
            # List is empty; initialize head and tail.
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            # Update tail's next to point to new head.
            assert self.tail is not None
            self.tail.next = new_node
        self.length += 1

    def remove(self, value: int) -> bool:
        """
        Removes the first node found with the specified value from the circular linked list.

        Args:
            value: The integer value to remove.

        Returns:
            True if a node was removed, False if the value was not found.
        """
        if not self.head:
            return False

        current = self.head
        prev = self.tail  # For circular list, previous of head is tail.
        for _ in range(self.length):
            if current.value == value:
                if self.length == 1:
                    # Only one node in the list.
                    self.head = None
                    self.tail = None
                else:
                    prev.next = current.next
                    if current == self.head:
                        self.head = current.next
                        assert self.tail is not None
                        self.tail.next = self.head
                    if current == self.tail:
                        self.tail = prev
                self.length -= 1
                return True
            prev = current
            current = current.next
        return False

    def search(self, value: int) -> Optional[Node]:
        """
        Searches for the first node with the specified value.

        Args:
            value: The integer value to search for.

        Returns:
            The node containing the value if found, otherwise None.
        """
        if not self.head:
            return None
        current = self.head
        for _ in range(self.length):
            if current.value == value:
                return current
            current = current.next
        return None

    def __iter__(self) -> Iterator[int]:
        """
        Allows iteration over the circular linked list.

        Yields:
            The integer values of each node in the list.
        """
        if not self.head:
            return
        current = self.head
        for _ in range(self.length):
            yield current.value
            current = current.next

    def to_list(self) -> List[int]:
        """
        Converts the circular linked list into a standard Python list of integer values.

        Returns:
            A list containing all the node values in the circular linked list.
        """
        return list(iter(self))

    def __repr__(self) -> str:
        """
        Returns a string representation of the circular linked list.
        """
        if not self.head:
            return "CircularLinkedList: Empty"
        values = " -> ".join(str(value) for value in self)
        return f"CircularLinkedList: {values} -> (head)"

    def get_length(self) -> int:
        """
        Retrieves the current number of nodes in the list.

        Returns:
            The length of the circular linked list.
        """
        return self.length


# ------------------- Working Example ------------------- #

if __name__ == "__main__":
    cll = CircularLinkedList()

    # Append nodes to the list.
    cll.append(10)
    cll.append(20)
    cll.append(30)
    print("After appending 10, 20, 30:")
    print(cll)
    print("Length:", cll.get_length())

    # Prepend a node to the list.
    cll.prepend(5)
    print("\nAfter prepending 5:")
    print(cll)
    print("Length:", cll.get_length())

    # Search for a value.
    node = cll.search(20)
    print("\nSearching for value 20:")
    print("Found node:", node)

    # Remove a node.
    removed = cll.remove(20)
    print("\nAfter removing 20 (successful removal: " + str(removed) + "):")
    print(cll)
    print("Length:", cll.get_length())

    # Convert to list.
    print("\nAs Python list:")
    print(cll.to_list())