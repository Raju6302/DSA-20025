from typing import List

class SelectionSort:
  """
  Implements the Selection Sort Algorithm.
  """
  def __init__(self, nums : List[int]) -> None:
    """
    Initializes the SelectionSort object with a list of numbers.

    Args:
        nums: The list of numbers to be sorted.
    """
    self.nums = nums

  def sort(self) -> None:
    """
    Sorts the 'nums' list in-place using Selection Sort Algo.

    Time-Complexity:
      - Worst/Average/Best Case: O(n^2) due to nested loops.

    Space Complexity:
      - O(1) as the sorting is done in-place.
    """
    N = len(self.nums)

    for i in range(N-1):
      min_idx = i
      for j in range(i + 1, N):
        if self.nums[j] < self.nums[min_idx]: min_idx = j
      
      if min_idx != i:
        self.nums[min_idx], self.nums[i] = self.nums[i], self.nums[min_idx]
  
  def __str__(self) -> str:
    """
    Returns a string representation of the sorted list.
    """
    return ' '.join(map(str, self.nums))



if __name__ == "__main__":

  example = SelectionSort([5, 2, 9, 1, 5, 6])
  # Before Sorting
  print("Before Sorting", example)

  example.sort() # Perform Sorting

  # After Sorting
  print("After Sorting", example) # The list [5, 2, 9, 1, 5, 6] is sorted to [1, 2, 5, 5, 6, 9].

