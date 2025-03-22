from typing import List

class MergeSort:
  """
  Implements the Merge Sort Algorithm.
  """
  def __init__(self, nums : List[int]) -> None:
    """
    Initializes the MergeSort object with a list of numbers.

    Args:
        nums: The list of numbers to be sorted.
    """
    self.nums = nums

  def sort(self) -> None:
    """
    Sorts the 'nums' list in-place using Merge Sort Algo.

    Time-Complexity:
      - O(n log n).

    Space Complexity:
      - O(n) due to recursion and temporary lists.
    """
    self.nums = self._merge_sort(self.nums)

  def _merge_sort(self, arr : List[int]) -> List[int]:
    """
    Recursive function to perform merge sort on the given list.
    """
    if len(arr) <= 1:
      return arr
  
    mid = len(arr) >> 1

    left_half = self._merge_sort(arr[:mid])
    right_half = self._merge_sort(arr[mid:])

    return self._merge(left_half, right_half)
  
  def _merge(self, left : List[int], right : List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list.
    """
    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        merged.append(left[i])
        i += 1
      else:
        merged.append(right[j])
        j += 1
    
    merged.extend(left[i:] or right[j:])

    return merged

  
  def __str__(self) -> str:
    """
    Returns a string representation of the sorted list.
    """
    return ' '.join(map(str, self.nums))



if __name__ == "__main__":

  example = MergeSort([5, 2, 9, 1, 5, 6])
  # Before Sorting
  print("Before Sorting", example)

  example.sort() # Perform Sorting

  # After Sorting
  print("After Sorting", example) # The list [5, 2, 9, 1, 5, 6] is sorted to [1, 2, 5, 5, 6, 9].

