from __future__ import annotations
from typing import Optional

class Node:
  """
  Represents a node in a singly linked list.
  """
  def __init__(self, val: int = None) -> None:
    """
    Initializes a Node with a given value.

    Args:
        val: The integer value stored in the node.
    """
    self.val: Optional[int] = val
    self.next: Optional[Node] = None
  
  def __repr__(self):
    return f"(Node({self.val}))"

class SinglyLinkedList:
  """
  A Singly Linked List Implementation.
  """
  def __init__(self, val: int) -> None:
    """
    Initializes the linked list with a single node containing the provided value.

    Args:
        val: The initial value for the linked list.
    """
    self.head: Node = Node(val)
    self.tail: Node = self.head
    self.length: int = 1
  

  def append(self, val: int) -> None:
    """
    Appends a new node at the end of the list with the given value.

    Args:
        val: The value to append.
    """
    new_node = Node(val)

    if self.head:
      self.tail.next = new_node
      self.tail = new_node
      self.length += 1
    else:
      self.head = self.tail = new_node
      self.length = 1
    
  def prepend(self, val: int) ->  None:
    """
    Prepends a new node with the given value at the beginning of the list.

    Args:
        val: The value of prepend.
    """
    new_node = Node(val)

    if self.head:
      new_node.next = self.head
      self.head = new_node
      self.length += 1
    else:
      self.head = self.tail = new_node
      self.length = 1
  

  def pop_left(self) -> Optional[Node]:
    """
    Removes and returns the first node of the list.

    Returns:
        The removed node, or None if the list is empty.
    """
    if not self.length:
      return None
  
    temp = self.head
    self.head = temp.next
    self.length -= 1

    if not self.length:
      self.tail = None
    
    temp.next = None # Help garbage collection.
    return temp
  
  def pop_right(self) -> Optional[Node]:
    """
    Removes and returns the last node of the list.

    Returns:
        The removed node, or None if the list is empty.
    """
    if not self.length: return None

    temp = prev = self.head

    while temp.next:
      prev = temp
      temp = temp.next
    
    self.tail = prev
    prev.next = None
    self.length -= 1

    if not self.length:
      self.head = None

    return temp

  def get(self, index: int) -> Optional[Node]:
    """
    Retrieves the node at a specified index.

    Args:
        index: The index of the node to retrieve.

    Returns:
        The node at the specified index, or None if the index is invalid.
    """
    if not self._check_index(index):
      # raise IndexError(f"Provided index: {index} is out of bound")
      return None
    
    temp = self.head
    for _ in range(index):
      temp = temp.next
    
    return temp


  def set(self, val: int, index: int) -> bool:
    """
    Sets the value of the node at the specified index.

    Args:
        val: The new value.
        index: The index of the node to update.

    Returns:
        True if the update was successful, False otherwise.
    """
    node = self.get(index)

    if node:
      node.val = val
      return True
    
    return False
  
  def insert(self, val: int, index: int) -> bool:
    """
    Inserts a new node with the given value at the specified index.

    Args:
        val: The value to insert.
        index: The position at which to insert the new node.

    Returns:
        True if insertion was successful, False otherwise.
    """
    if index < 0 or index > self.length: return False

    if index == 0:
      self.prepend(val)
      return True
    elif index == self.length:
      self.append(val)
      return True
    else:
      new_node = Node(val)

      prev = self.get(index - 1)

      new_node.next = prev.next
      prev.next = new_node
    
      self.length += 1
      return True

  def remove(self, index: int) -> Optional[Node]:
    """
    Removes and returns the node at the specified index.

    Args:
        index: The index of the node to remove.

    Returns:
        The removed node, or None if the index is invalid.
    """
    if self._check_index(index): return None

    if index == 0: return self.pop_left()
    if index == self.length - 1: return self.pop_right()

    prev = self.get(index - 1)
    if prev is None or prev.next is None:
      return None
    
    removed = prev.next
    prev.next = removed.next

    self.length -= 1

    removed.next = None # Help garbage collection.
    return removed

  def reverse(self) -> None:
    """
    Reverses the linked list in place.
    """
    temp = self.head
    self.head, self.tail = self.tail, self.head

    before : Optional[Node] = None
    for _ in range(self.length):
      after: Optional[Node] = temp.next if temp else None

      if temp:
        temp.next = before

      before = temp
      temp = after
  
  def print_list(self) -> None:
    """
    Prints the linked list in a readable format.
    """
    temp = self.head

    while temp:
      print(f"{temp.val} ->", end=" ")
      temp = temp.next
    print("None")
    
  def get_head(self):
    print("head -> ", self.head.val)
  
  def get_tail(self):
    if self.tail:
        print("tail ->", self.tail.val)
    else:
        print("tail -> None")
  
  def get_length(self):
    print("Length -> ", self.length)


  def _check_index(self, index: int) -> bool:
    return 0 <= index < self.length




# ----------------- Working Example ----------------- #

if __name__ == "__main__":
    # Create a new linked list with an initial value.
    sll = SinglyLinkedList(10)
    
    # Append elements to the list.
    sll.append(20)
    sll.append(30)
    
    # Prepend an element to the list.
    sll.prepend(5)
    
    # Print the initial list.
    print("Initial list:")
    sll.print_list()
    
    # Get head, tail, and length.
    sll.get_head()
    sll.get_tail()
    sll.get_length()
    
    # Insert an element at index 2.
    sll.insert(15, 2)
    print("\nAfter inserting 15 at index 2:")
    sll.print_list()
    
    # Remove the element at index 3.
    removed_node = sll.remove(3)
    print(f"\nRemoved node with value: {removed_node.val if removed_node else None}")
    sll.print_list()
    
    # Reverse the list.
    sll.reverse()
    print("\nAfter reversing the list:")
    sll.print_list()

