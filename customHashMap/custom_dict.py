from __future__ import annotations
from typing import Any, Optional, List, Iterator, Tuple


class Node:
    """
    Represents a key-value pair node in the custom dictionary.
    """
    def __init__(self, key: Any, value: Any) -> None:
        """
        Initializes a Node with the specified key and value.

        Args:
            key: The key (must be hashable).
            value: The value associated with the key.
        """
        self.key: Any = key
        self.value: Any = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"({self.key}: {self.value})"


class CustomDict:
    """
    A custom dictionary implementation using separate chaining for collision resolution.
    """
    def __init__(self, initial_capacity: int = 8, load_factor: float = 0.7) -> None:
        """
        Initializes the custom dictionary.

        Args:
            initial_capacity: The initial number of buckets.
            load_factor: The load factor threshold for resizing.
        """
        self.capacity: int = initial_capacity
        self.size: int = 0
        self.load_factor: float = load_factor
        self.buckets: List[Optional[Node]] = [None] * self.capacity

    def _hash(self, key: Any) -> int:
        """
        Computes the bucket index for a given key.

        Args:
            key: The key to hash.

        Returns:
            An index within the range of the buckets.
        """
        return hash(key) % self.capacity

    def put(self, key: Any, value: Any) -> None:
        """
        Inserts or updates the key-value pair into the dictionary.

        Args:
            key: The key (must be hashable).
            value: The value to associate with the key.
        """
        index = self._hash(key)
        head = self.buckets[index]
        current = head

        # Update value if key already exists.
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # Insert new node at the beginning of the chain.
        new_node = Node(key, value)
        new_node.next = head
        self.buckets[index] = new_node
        self.size += 1

        # Check if we need to resize.
        if self.size / self.capacity > self.load_factor:
            self._resize()

    def get(self, key: Any) -> Optional[Any]:
        """
        Retrieves the value associated with the specified key.

        Args:
            key: The key to look up.

        Returns:
            The value if found, or None otherwise.
        """
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key: Any) -> bool:
        """
        Removes the key-value pair from the dictionary.

        Args:
            key: The key to remove.

        Returns:
            True if the key was found and removed, False otherwise.
        """
        index = self._hash(key)
        current = self.buckets[index]
        prev: Optional[Node] = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next

        return False

    def _resize(self) -> None:
        """
        Resizes the dictionary when the load factor exceeds the threshold.
        """
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        old_size = self.size
        self.size = 0

        for head in old_buckets:
            current = head
            while current:
                self.put(current.key, current.value)
                current = current.next
        # Adjust size (it is re-calculated during re-insertions).
        self.size = old_size

    # Dunder methods for Python dictionary-like behavior.

    def __setitem__(self, key: Any, value: Any) -> None:
        """Sets the value for a key (e.g., d[key] = value)."""
        self.put(key, value)

    def __getitem__(self, key: Any) -> Any:
        """Retrieves the value for a key (e.g., value = d[key])."""
        result = self.get(key)
        if result is None:
            raise KeyError(key)
        return result

    def __delitem__(self, key: Any) -> None:
        """Deletes the key-value pair (e.g., del d[key])."""
        if not self.remove(key):
            raise KeyError(key)

    def __contains__(self, key: Any) -> bool:
        """Checks if the key is in the dictionary (e.g., key in d)."""
        return self.get(key) is not None

    def __len__(self) -> int:
        """Returns the number of key-value pairs."""
        return self.size

    def __iter__(self) -> Iterator[Tuple[Any, Any]]:
        """
        Iterates over key-value pairs.

        Yields:
            Tuples of (key, value).
        """
        for bucket in self.buckets:
            current = bucket
            while current:
                yield (current.key, current.value)
                current = current.next

    def __repr__(self) -> str:
        """
        Returns a string representation of the custom dictionary.
        """
        items = list(self)
        return "{" + ", ".join(f"{k}: {v}" for k, v in items) + "}"


# ------------------ Working Example ------------------ #

if __name__ == "__main__":
    custom_dict = CustomDict()

    # Insert key-value pairs.
    custom_dict.put("apple", 1)
    custom_dict.put("banana", 2)
    custom_dict.put("cherry", 3)

    print("CustomDict after insertion:")
    print(custom_dict)
    print("Size:", len(custom_dict))

    # Update an existing key.
    custom_dict.put("apple", 10)
    print("\nAfter updating 'apple':")
    print(custom_dict)

    # Retrieve values.
    print("\nValue for 'banana':", custom_dict.get("banana"))

    # Use dunder methods.
    custom_dict["date"] = 4
    print("\nAfter setting 'date' via __setitem__:")
    print(custom_dict)

    # Delete a key.
    del custom_dict["banana"]
    print("\nAfter deleting 'banana':")
    print(custom_dict)

    # Check containment.
    print("\nContains 'cherry'? :", "cherry" in custom_dict)
    print("Contains 'banana'? :", "banana" in custom_dict)

    # Iterate over key-value pairs.
    print("\nIterating over items:")
    for key, value in custom_dict:
        print(f"{key}: {value}")