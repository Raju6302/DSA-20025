package sorting.mergeSort;

import java.util.Arrays;

public class MergeSort {

  public static void main(String[] args) {
    int[] arr1 = {3, 5, 7,1, 2, 4, 6, 11, 8, 9};
    int[] ans = mergetSort(arr1);
    System.out.println(Arrays.toString(ans));
  }


  public static int[] mergetSort(int[] arr) {
    if (arr.length == 1) return arr;
    int midIndex = arr.length / 2;
    int[] left = mergetSort(Arrays.copyOfRange(arr, 0, midIndex));
    int[] right = mergetSort(Arrays.copyOfRange(arr, midIndex, arr.length));

    return sortedArray(left, right);
  }



  //combine two sorted arrays into one sorted array
  public static int[] sortedArray(int[] arr1, int[] arr2) {
    int[] combinedArray = new int[arr1.length + arr2.length];
    int index = 0, i = 0, j = 0;

    while (i < arr1.length && j < arr2.length) {
      if (arr1[i] < arr2[j]) {
        combinedArray[index] = arr1[i];
        index++;
        i++;
      }else {
        combinedArray[index] = arr2[j];
        index++;
        j++;
      }
    }

    while (i < arr1.length) {
      combinedArray[index] = arr1[i];
        index++;
        i++;
    }

    while (j < arr2.length) {
      combinedArray[index] = arr2[j];
        index++;
        j++;
    }

    return combinedArray;
  }
  
}