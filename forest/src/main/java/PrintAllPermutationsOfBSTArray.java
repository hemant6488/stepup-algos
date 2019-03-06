import core.BinarySearchTree;
import core.Node;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by hemantkumar on 05/03/19.
 */
public class PrintAllPermutationsOfBSTArray {
    public static void main(String args[]){
        int[] arr1= {50, 20, 60, 10, 25, 70, 5, 15, 65, 80};
        int[] arr = {2, 1, 3};

        BinarySearchTree binarySearchTree = new BinarySearchTree();


        for (int i: arr){
            binarySearchTree.insertNode(i);
        }
        binarySearchTree.printTree();
        List<Node> list = binarySearchTree.toArrayList(binarySearchTree.root, null);
        List<List<Integer>> permutations = printAllPermutations(list);
        System.out.print("asd");
    }

    private static List<List<Integer>> printAllPermutations(List<Node> list) {
        List<Node> queue = new ArrayList<>();
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < list.size(); i++){
            queue.add(list.get(i));
            Node currentNode = queue.get(0);
            queue.remove(0);
            if (currentNode.left != null) {
                queue.add(currentNode.left);
            }
            if (currentNode.right != null) {
                queue.add(currentNode.right);
            }


            if (queue.size() > 0){
                for (List<Integer> r: printAllPermutations(queue)){
                    r.add(0, currentNode.value);
                    result.add(r);
                }
            } else {
                List<Integer> r = new ArrayList<>();
                r.add(currentNode.value);
                result.add(r);
            }
        }
        return result;
    }

    private static List<List<Integer>> getPermutationsForNode(Node currentNode) {
        List<List<Integer>> result = new ArrayList<>();
        List<List<Integer>> leftSubtree = null;
        List<List<Integer>> rightSubtree = null;

        if (currentNode.left != null) {
            leftSubtree = getPermutationsForNode(currentNode.left);
            for (List<Integer> list: leftSubtree){
                list.add(0, currentNode.value);
            }
        }
        if (currentNode.right != null) {
            rightSubtree = getPermutationsForNode(currentNode.right);
            for (List<Integer> list: rightSubtree){
                list.add(0, currentNode.value);
            }
        }

        if (currentNode.left == null && currentNode.right == null){
            List<Integer> list = new ArrayList<>();
            list.add(currentNode.value);
            result.add(list);
        }

        if (leftSubtree != null && leftSubtree.size() != 0){
            if (rightSubtree != null && rightSubtree.size() != 0) {
                for (List<Integer> list : leftSubtree) {
                    for (List<Integer> right: rightSubtree){
                        list.addAll(right);
                        result.add(list);
                    }
                }
            } else {
                result.addAll(leftSubtree);
            }
        } else {
            if (rightSubtree != null && rightSubtree.size() != 0){
                result.addAll(rightSubtree);
            }
        }

        return result;
    }

    private static List<Integer> cloneList(List<Integer> list){
        List<Integer> newArrayList = new ArrayList<>();

        for (Integer s: list){
            newArrayList.add(s);
        }

        return newArrayList;
    }
}
