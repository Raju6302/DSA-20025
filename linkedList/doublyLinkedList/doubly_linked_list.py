from typing import Optional

class Node:
  """
  Represents a node in a doubly linked list.
  """
  def __init__(self, val: Optional[int] = None) -> None:
    """
    Initializes a Node with a given value.
    Args:
        val: The integer value stored in the node.
    """
    self.val: Optional[int] = val
    self.next: Optional[Node] = None
    self.prev: Optional[Node] = None

  def __repr__(self):
    return f"(Node({self.val}))"


class DoublyLinkedList:
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
    new_node: Node = Node(val)

    if not self.head:
      self.head = new_node
      self.tail = new_node
      self.length = 1
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
      self.length += 1
  
  def prepend(self, val: int) -> None:
    """
    Prepends a new node with the given value at the beginning of the list.
    Args:
        val: The value of prepend.
    """
    new_node: Node = Node(val)

    if not self.head:
      self.head = new_node
      self.tail = new_node
      self.length = 1
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
      self.length += 1

  def pop_right(self) -> Optional[Node]:
    """
    Removes the last node from the list and returns it.
    Returns:
        The removed node, or None if the list is empty.
    """
    if not self.head: return None
    temp: Node = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      temp.prev = None
    self.length -= 1
    return temp


  def pop_left(self) -> Optional[Node]:
    """
    Removes the first node from the list and returns it.
    Returns:
        The removed node, or None if the list is empty.
    """
    if not self.head: return None
    temp: Node = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
      temp.next = None
    self.length -= 1
    return temp
  

  def get(self, index: int) -> Optional[Node]:
    """
    Retrieves the node at the specified index in the list.
    Args:
        index: The index of the node to retrieve.
    Returns:
        The node at the specified index, or None if the index is out of bounds.
    """
    if index < 0 or index >= self.length: return None
    temp: Node
    if index < self.length >> 1:
      for _ in range(index):
        temp = temp.next
    else:
      temp = self.tail
      for _ in range(self.length - 1, index, -1):
        temp = temp.prev
    return temp
  
  def set(self, index: int, val: int) -> bool:
    """
    Updates the value of the node at the specified index in the list.
    Args:
        index: The index of the node to update.
        val: The new value to set.
    Returns:
        True if the update is successful, False otherwise.
    """
    temp: Optional[Node] = self.get(index)
    if temp:
      temp.val = val
      return True
    return False

  def insert(self, index: int, val: int) -> bool:
    """
    Inserts a new node with the given value at the specified index in the list.
    Args:
        index: The index at which to insert the new node.
        val: The value of the new node.
    Returns:
        True if the insertion is successful, False otherwise.
    """
    if index < 0 or index > self.length: return False
    if index == 0: 
      self.prepend(val)
      return True
    if index == self.length: 
      self.append(val)
      return True
    new_node: Node = Node(val)
    before: Node = self.get(index - 1)
    after: Node = before.next
    new_node.prev = before
    new_node.next = after
    before.next = new_node
    after.prev = new_node
    self.length += 1
    return True

  def remove(self, index: int) -> Optional[Node]:
    """
    Removes the node at the specified index from the list and returns it.
    Args:
        index: The index of the node to remove.
    Returns:
        The removed node, or None if the index is out of bounds.
    """
    if index < 0 or index >= self.length: return None
    if index == 0: return self.pop_left()
    if index == self.length - 1: return self.pop_right()
    temp: Node = self.get(index)
    temp.prev.next = temp.next
    temp.next.prev = temp.prev
    temp.next = None
    temp.prev = None
    self.length -= 1
    return temp

  def get_head(self) -> None:
    if self.head:
      print("head -> ", self.head.val)
    else:
      print("head -> None")

  def get_tail(self) -> None:
    if self.tail:
      print("tail ->", self.tail.val)
    else:
      print("tail -> None")

  def get_length(self) -> None:
    print("Length -> ", self.length)

  def print_list(self) -> None:
    """
    Prints the values of all nodes in the list.
    """
    temp: Optional[Node] = self.head
    print("None", end=" ")
    while temp:
      print(f"<- {temp.val} ->", end=" ")
      temp = temp.next
    print("None")



# < ------------ Working Example -------------> #

if __name__ == "__main__":
  dll = DoublyLinkedList(10)

  #Append elements to the list
  dll.append(20)
  dll.append(30)
  dll.append(40)

  #Prepend elements to the list
  dll.prepend(0)

  #print the list
  dll.print_list()

  #Get head, tail and length
  dll.get_head()
  dll.get_tail()
  dll.get_length()

  #Pop elements from the list
  dll.pop_right()
  dll.pop_left()
  #print the list
  dll.print_list()

  #Get head, tail and length
  dll.get_head()
  dll.get_tail()
  dll.get_length()

  #insert an element at index 2
  dll.insert(2, 25)
  #print the list
  dll.print_list()

  # Remove the element at index 3
  removed_node = dll.remove(3)
  print(f"\nRemoved node with value: {removed_node.val if removed_node else None}")
  dll.print_list()  