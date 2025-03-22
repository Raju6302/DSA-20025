from __future__ import annotations
from typing import Optional


class Node:
    """
    Represents a node in the stack.
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


class Stack:
    """
    A simple Stack implementation using a singly linked list.
    """
    def __init__(self, value: int) -> None:
        """
        Initializes the Stack with a single element.

        Args:
            value: The initial value for the stack.
        """
        new_node = Node(value)
        self.top: Optional[Node] = new_node
        self.height: int = 1

    def push(self, value: int) -> int:
        """
        Pushes a new value onto the top of the stack.

        Args:
            value: The value to push onto the stack.

        Returns:
            The new height of the stack.
        """
        new_node = Node(value)
        if not self.height:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return self.height

    def pop(self) -> Optional[Node]:
        """
        Pops the top element off the stack.

        Returns:
            The popped Node if the stack is not empty; otherwise, None.
        """
        if not self.height:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None  # Help garbage collection.
        self.height -= 1
        return temp

    def get_top(self) -> Optional[Node]:
        """
        Retrieves the top element of the stack without removing it.

        Returns:
            The top Node of the stack, or None if the stack is empty.
        """
        return self.top

    def get_height(self) -> int:
        """
        Retrieves the height of the stack.

        Returns:
            The number of elements in the stack.
        """
        return self.height

    def __repr__(self) -> str:
        """
        Returns a string representation of the stack.
        """
        temp = self.top
        result = ""
        while temp:
            result += str(temp.value)
            temp = temp.next
            if temp:
                result += " -> "
        return result


# ------------ Working Example ------------ #

if __name__ == "__main__":
    my_stack = Stack(4)
    print("Stack height after push:", my_stack.push(3))
    print("Stack height after push:", my_stack.push(2))
    print("Stack height after push:", my_stack.push(1))

    print("Stack:", my_stack)
    print("Popped:", my_stack.pop())
    print("Popped:", my_stack.pop())

    print("Stack after pops:", my_stack)
    print("Top element:", my_stack.get_top())
    print("Current height:", my_stack.get_height())