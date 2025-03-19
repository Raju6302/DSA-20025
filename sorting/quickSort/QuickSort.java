package sorting.quickSort;

import java.util.Arrays;

public class QuickSort {
  public static void main(String[] args) {
    int[] arr = {12,3, 5, 7,1, 2, 4, 6, 11, 8, 13, 9};
    quickSort(arr);
    System.out.println(Arrays.toString(arr));
    
  }

  public static void quickSort(int[] arr) {
    quickSortHelper(arr, 0, arr.length-1);
  }

  public static void quickSortHelper(int[] arr, int left, int right) {
    if (left < right) {
       int pivotIndex = pivot(arr, left, right);
       quickSortHelper(arr, left, pivotIndex);  
       quickSortHelper(arr, pivotIndex + 1, right);    
    }
  }

  public static int pivot(int[] arr, int pivotIndex, int endIndex) {
    int swapIndex = pivotIndex;
    for (int i = pivotIndex + 1; i <= endIndex; i++) {
      if (arr[i] < arr[pivotIndex]) {
        swapIndex++;
        swap(arr, swapIndex, i);
      }
    }

    swap(arr, pivotIndex, swapIndex);

    return swapIndex;
  }

  public static void swap(int[] arr, int leftIndex, int rightIndex) {
      int temp = arr[leftIndex];
      arr[leftIndex] = arr[rightIndex];
      arr[rightIndex] = temp;
  }

}