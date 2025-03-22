from typing import List

class InsertionSort:
  """
  Implements the Insertion Sort Algorithm.
  """
  def __init__(self, nums : List[int]) -> None:
    """
    Initializes the InsertionSort object with a list of numbers.

    Args:
        nums: The list of numbers to be sorted.
    """
    self.nums = nums

  def sort(self) -> None:
    """
    Sorts the 'nums' list in-place using Insertion Sort Algo.

    Time-Complexity:
      - Worst/Average Case: O(n^2) when the list is in reverse order.
      - Best Case: O(n) when the list is already sorted.

    Space Complexity:
      - O(1) as the sorting is done in-place.
    """
    N = len(self.nums)

    for i in range(1, N):
      j = i
      while j > 0 and self.nums[j-1] > self.nums[j]:
        self.nums[j], self.nums[j-1] = self.nums[j-1], self.nums[j]
        j -= 1
  
  def __str__(self) -> str:
    """
    Returns a string representation of the sorted list.
    """
    return ' '.join(map(str, self.nums))



if __name__ == "__main__":

  example = InsertionSort([5, 2, 9, 1, 5, 6])
  # Before Sorting
  print("Before Sorting", example)

  example.sort() # Perform Sorting

  # After Sorting
  print("After Sorting", example) # The list [5, 2, 9, 1, 5, 6] is sorted to [1, 2, 5, 5, 6, 9].

