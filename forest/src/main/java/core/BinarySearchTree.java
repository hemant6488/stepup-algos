package core;

import java.util.ArrayList;
import java.util.List;

public class BinarySearchTree {
    public Node root = null;

    public BinarySearchTree() {

    };

    public BinarySearchTree(int value) {
        insertNode(value);
    }

    public void insertNode(int value) {
        Node node = new Node(value);

        if (root == null) {
            root = node;
        } else {
            insertNode(node, root);
        }
    }

    public void insertNode(Node newNode, Node node) {
        if (newNode.value == node.value) {
            node.count++;
        } else if (newNode.value < node.value) {
            if (node.left == null) {
                node.left = newNode;
                return;
            } else {
                insertNode(newNode, node.left);
            }
        } else {
            if (node.right == null) {
                node.right = newNode;
            } else {
                insertNode(newNode, node.right);
            }
        }
    }

    public void preOrderTraversal() {
        preOrderTraversal(root);
    }

    public void inOrderTraversal(){
        inOrderTraversal(root);
    }

    public void postOrderTraversal(){
        postOrderTraversal(root);
    }

    public List<Node> toArrayList(Node root, List<Node> list){
        if (list == null){
            list = new ArrayList<>();
        }

        if (root == null){
            return list;
        } else {
            list.add(root);
            toArrayList(root.left, list);
            toArrayList(root.right, list);
        }
        return list;
    }
    public void inOrderTraversal(Node root) {
        if (root == null) {
            return;
        } else {
            inOrderTraversal(root.left);
            System.out.print(root.value + " ");
            inOrderTraversal(root.right);
        }
    }

    public void preOrderTraversal(Node root){
        if (root == null){
            return;
        } else {
            System.out.print(root.value + " ");
            preOrderTraversal(root.left);
            preOrderTraversal(root.right);
        }
    }

    public void postOrderTraversal(Node root){
        if (root == null){
            return;
        } else {

            postOrderTraversal(root.left);
            postOrderTraversal(root.right);
            System.out.print(root.value + " ");
        }
    }

    public void printTree() {
        this.root.printTree();
    }

}
