import core.BinarySearchTree;
import core.Node;

import java.util.ArrayList;
import java.util.List;

/**
 * BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting each
 * element. Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
 *
 * Created by hemantkumar on 05/03/19.
 */
public class PrintAllPermutationsOfBSTArray {
    public static void main(String args[]){
        /** Multiple arrays for test cases **/
        int[] arr1= {50, 20, 60, 10, 25, 70, 5, 15, 65, 80};
        int[] arr3 = {50, 60, 20, 10, 70, 80, 15, 25, 65, 5};
        int[] arr = {2, 1, 3};
        int[] arr4 = {3, 1, 2, 4, 5};

        BinarySearchTree binarySearchTree = new BinarySearchTree();


        for (int i: arr4){
            binarySearchTree.insertNode(i);
        }

        binarySearchTree.printTree();
        List<List<Integer>> permutations = findAllPermutations(binarySearchTree.root, null);

        printFormattedResult(permutations);
    }

    private static void printFormattedResult(List<List<Integer>> permutations) {
        System.out.println();
        for (List<Integer> list: permutations){
            System.out.print("[");
            int index = 0;
            for (Integer integer: list){
                System.out.print(integer.toString());
                index++;

                if(index < list.size()){
                    System.out.print(", ");
                }

            }
            System.out.println("]");
        }
    }

    private static List<List<Integer>> findAllPermutations(Node root, List<Node> queue) {
        List<List<Integer>> result = new ArrayList<>();
        if (queue == null) {
            queue = new ArrayList<>();
        }
        if (root.right != null) {
            queue.add(root.right);
        }
        if (root.left != null) {
            queue.add(root.left);
        }

        if (queue.size() == 0){
            List<Integer> r = new ArrayList<>();
            r.add(root.value);
            result.add(r);
        }

        for (int i=0; i < queue.size(); i++){
            List<Node> updatedQueue =  cloneList(queue);
            updatedQueue.remove(i);
            for (List<Integer> r: findAllPermutations(queue.get(i), updatedQueue)){
                r.add(0, root.value);
                result.add(r);
            }
        }

        if (queue.size() != 0){
            queue.remove(0);
        }

        return result;
    }

    private static List<Node> cloneList(List<Node> list){
        if (list.size() == 0){
            return null;
        }
        List<Node> newArrayList = new ArrayList<>();

        for (Node s: list){
            newArrayList.add(s);
        }

        return newArrayList;
    }
}
