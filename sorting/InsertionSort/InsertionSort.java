package sorting.InsertionSort;

import java.util.Arrays;

public class InsertionSort {
  public static void main(String[] args) {
    int[] arr = {6, 9, 1, 4, 3, 2, 1};
    insertionSort(arr);
    System.out.println("Sorted: " + " " + Arrays.toString(arr));
  }

  public static void insertionSort(int[] arr) {
    for (int i = 1; i < arr.length; i++) {
      int temp = arr[i];
      int j = i - 1;
      while (j > -1 && temp < arr[j] ) {
        arr[j+1] = arr[j];
        arr[j] = temp;
        j--;
      }
    }
  }
}