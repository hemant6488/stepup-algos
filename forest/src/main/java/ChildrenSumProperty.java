import core.BinarySearchTree;

import java.util.Random;

public class ChildrenSumProperty {
    public static void main(String args[]){
        BinarySearchTree bst = new BinarySearchTree();
        Random random = new Random(500);

        for (int i=0; i < 5; i++){
            int value = random.nextInt(30);
            bst.insertNode(value);
        }

        bst.root.printTree();
    }
}
