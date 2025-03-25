from typing import List

class QuickSort:
  """
  Implements the Quick Sort Algorithm.
  """
  def __init__(self, nums: List[int]) -> None:
    """
    Initializes the QuickSort object with a list of numbers.

    Args:
        nums: The list of numbers to be sorted.
    """
    self.nums = nums

  def sort(self) -> None:
    """
    Sorts the 'nums' list in-place using Quick Sort Algo.

    Time-Complexity:
      - Average/Best Case: O(n log n).
      - Worst Case: O(n^2) (rare, when pivot selection is poor).

    Space Complexity:
      - O(log n) on average due to recursion.
    """
    self._quick_sort(0, len(self.nums) - 1)

  def _quick_sort(self, low: int, high: int) -> None:
    """
    Recursive function to perform merge sort on the given list.
    """
    if low < high:
      pivot_idx = self._partition(low, high)
      self._quick_sort(low, pivot_idx - 1)
      self._quick_sort(pivot_idx + 1, high)
  
  def _partition(self, low: int, high: int) -> int:
    """
    Partitions the subarray by selecting the last element as the pivot,
    placing the pivot at its correct position, and arranging smaller
    elements to its left and larger elements to its right.

    Returns:
        The index of the pivot element after partitioning.
    """
    pivot = self.nums[high]
    i = low

    for j in range(low, high):
      if self.nums[j] < pivot:
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        i += 1
      
    self.nums[i], self.nums[high] = self.nums[high], self.nums[i]

    return i
  
  def __str__(self) -> str:
    """
    Returns a string representation of the sorted list.
    """
    return ' '.join(map(str, self.nums))



if __name__ == "__main__":

  example = QuickSort([5, 2, 9, 1, 5, 6])
  # Before Sorting
  print("Before Sorting", example)

  example.sort() # Perform Sorting

  # After Sorting
  print("After Sorting", example) # The list [5, 2, 9, 1, 5, 6] is sorted to [1, 2, 5, 5, 6, 9].

