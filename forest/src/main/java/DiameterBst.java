import core.BinarySearchTree;
import core.Node;

import java.util.Random;

public class DiameterBst {

    public static int findDiameter(Node node){
        int diameter = 0;

        if (node == null){
            diameter = 0;
        } else {
            int leftDiameter = findDiameter(node.left);
            int rightDiameter = findDiameter(node.right);

            int leftHeight = findHeight(node.left);
            int rightHeight = findHeight(node.right);

            /**
                * the diameter of T’s left subtree
                * the diameter of T’s right subtree
                * the longest path between leaves that goes through the root of T
             **/

            return Math.max((leftHeight + rightHeight + 1), Math.max(rightDiameter, leftDiameter));
        }
        return diameter;
    }

    private static int findHeight(Node node) {
        int maxHeight = 0;

        if(node == null){
            maxHeight = 0;
        } else {
            maxHeight = 1 + Math.max(findHeight(node.left), findHeight(node.right));
        }

        return maxHeight;
    }

    public static void main(String args[]) {
        BinarySearchTree bst = new BinarySearchTree();
        for (int i = 0; i < 15; i++) {
            bst.insertNode(new Random().nextInt(20));
        }
        bst.root.printTree();

        System.out.print("Height: ");
        System.out.println(findHeight(bst.root));

        System.out.print("Diameter: ");
        System.out.print(findDiameter(bst.root));
    }

}
