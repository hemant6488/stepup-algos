import java.util.Arrays;
import java.util.Random;

/**
 * Created by hemantkumar on 06/02/19.
 */
public class FindKeyInRotatedSortedArray {
    static int iterations;

    public static void main(String args[]){
        Random random = new Random(50);
        int arr[] = {5, 6, 7, 8, 9, 0, 1, 2, 3, 4};
        int arr2[] = {1, 2, 3, 4};
        int arr3[] = {1, 2, 3, 4, 7};
        int arr4[] = {8, 1, 2, 3, 4, 7};
        int arr5[] = {1};

        int bigArr[] = new int[10000];

        for(int i = 0; i < 10000; i++){
            bigArr[i] = random.nextInt(200000);
        }

        Arrays.sort(bigArr);

        for (int i=0; i<10000; i++){
//            System.out.print(bigArr[i] + ", ");
        }

//        System.out.println(binarySearch(bigArr, 0, 0, bigArr.length-1));
//        System.out.println("Iterations: " + iterations);

        /**
         * 1. Use modification of binary search to find the pivot element.
         * 2. Once we have the pivot element, we have two sorted arrays, apply binary search.
         */

//        System.out.println("Pivot: " + findPivot(arr, 0, arr.length -1));
//        System.out.println("Pivot: " + findPivot(arr2, 0, arr2.length -1));
//        System.out.println("Pivot: " + findPivot(arr3, 0, arr3.length -1));
//        System.out.println("Pivot: " + findPivot(arr4, 0, arr4.length -1));
//        System.out.println("Pivot: " + findPivot(arr5, 0, arr5.length -1));
        int pivot = findPivot(arr, 0, arr.length - 1);
        System.out.println("pivot: "+ pivot);

        int index = binarySearch(arr, 3, 0, pivot - 1);
        if (index == -1){
            index = binarySearch(arr, 3, pivot, arr.length - 1);
        }

        System.out.println("Index: "+ index);


    }

    public static int findPivot(int[] array, int start, int end){
        if(start > end){
            return 0;
        }

        if(start == end){
            return 0;
        }

        int mid = (start + end) /2;

        if(mid < end && array[mid] > array[mid+1]){
            return mid+1;
        }
        if(mid > start && array[mid] < array[mid-1]){
            return mid;
        }

        if(array[mid] < array[start]){
            return findPivot(array, start, mid-1);
        } else {
            return findPivot(array, mid+1, end);
        }
    }

    public static int binarySearch(int[] array, int key, int start, int end){
        iterations++;
        if (start >= end){
            return -1;
        }

        int mid = (start + end) /2;

        if (array[mid] == key){
            return mid;
        } else if (array[mid] > key) { // search in left sub array
            return binarySearch(array, key, start, mid-1);
        } else {
            return binarySearch(array, key, mid+1, end);
        }

    }

}
