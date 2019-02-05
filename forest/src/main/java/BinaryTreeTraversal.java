import core.BinarySearchTree;

import java.util.Random;

public class BinaryTreeTraversal {
    public static void main(String args[]) {
        Random random = new Random();
        BinarySearchTree bst = new BinarySearchTree();
//        bst.insertNode(1);
//        bst.insertNode(2);
//        bst.insertNode(3);
//        bst.insertNode(4);
//        bst.insertNode(5);
//        bst.insertNode(6);
//        bst.insertNode(6);

        for (int i=0; i < 5; i++){
            bst.insertNode(random.nextInt(30));
        }

        bst.root.printTree();

        System.out.println("\nPreOrder: ");
        bst.preOrderTraversal();

        System.out.println("\nPostOrder: ");
        bst.postOrderTraversal();

        System.out.println("\nInOrder: ");
        bst.inOrderTraversal();
    }

}
