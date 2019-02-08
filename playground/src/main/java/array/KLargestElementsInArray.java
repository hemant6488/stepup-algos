package array;

import utils.Timer;

import java.util.Arrays;
import java.util.Collections;
import java.util.Random;

/**
 * Created by hemantkumar on 07/02/19.
 */
public class KLargestElementsInArray {

    public static void main(String args[]) {
        int array[] = {1, 23, 12, 9, 30, 2, 50, 73, 86, 94, 24, 88, 26, 87, 3, 100};
//        int[] array = {12, 5, 787, 1, 23};
        int[] array2 = {1, 23, 12, 9, 30, 2, 50, 73, 86, 94, 24, 88, 26, 87, 3, 100};
        int k = 2;
        int[] resultArr, resultArr2;

        Timer timer1 = new Timer();
        resultArr = findKlargestUsingTempArray(array, k);
        System.out.println("Temp Array time: " + timer1);
        for(int i=0; i<resultArr.length; i++)
            System.out.print(resultArr[i] + " ");
        System.out.println();


        Timer timer2 = new Timer();
        resultArr2 = findKLargestSortingApproach(array2, k);
        System.out.println("Sort approach time: " + timer2);
        for(int i=resultArr2.length-1; i>=0; i--)
            System.out.print(resultArr2[i] + " ");

    }

    private static int[] findKlargestUsingTempArray(int[] array, int k){
        int[] resultArray = new int[k];

        for (int i=0; i<k; i++){
            resultArray[i] = array[i];
        }

        quickSort(resultArray);

        for(int i=k; i<(array.length); i++){
            if(resultArray[0] < array[i]){
                resultArray[0] = array[i];
                quickSort(resultArray);
            }
        }

        return resultArray;
    }

    private static int[] findKLargestSortingApproach(int[] array, int k){
        quickSort(array);
        int[] resultArray = new int[k];
        int last = array.length - 1;

        for (int i = 0; i < k; i++){
            resultArray[i] = array[last];
            last--;
        }
        return resultArray;
    }


    /**
     * Wrapper function for quick sort.
     * @param array
     * @return
     */
    private static void quickSort(int[] array) {
        quickSort(array, 0, array.length - 1);
    }

    private static void quickSort(int[] array, int start, int end){
        if (start < end){
            int pivot = partition(array, start, end);
            quickSort(array, start, pivot-1);
            quickSort(array, pivot+1, end);
        }
    }

    private static int partition(int[] array, int left, int right){
        if(left == right){
            return left;
        }

        /**
         *  Choosing the right most element as pivot point
         */
        int pivot = right;
        int partitionIndex = left;

        for (int i=left; i < right; i++){
            if (array[i] <= array[pivot]){
                swap(array, partitionIndex, i);
                partitionIndex++;
            }
        }
        swap(array, partitionIndex, right);

        return partitionIndex;
    }

    private static void swap(int[] array, int pos1, int pos2){
        if(pos1 != pos2) {
            int temp = array[pos1];
            array[pos1] = array[pos2];
            array[pos2] = temp;
        }
    }
}

