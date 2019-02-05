package core;

public class Node {
    public Integer value;
    public Node left;
    public Node right;
    public Integer count;

    public Node(int value) {
        this.value = value;
        this.count = 1;
        this.left = null;
        this.right = null;
    }

    public void printTree() {
        if (right != null) {
            right.printTree(true, "");
        }
        printNodeValue();
        if (left != null) {
            left.printTree(false, "");
        }
    }

    private void printNodeValue() {
        if (value == null) {
            System.out.print("<null>");
        } else {
            System.out.print(value.toString() + "(" + count + ")");
        }
        System.out.print('\n');
    }

    // use string and not stringbuffer on purpose as we need to change the indent at each recursion
    private void printTree(boolean isRight, String indent) {
        if (right != null) {
            right.printTree(true, indent + (isRight ? "        " : " |      "));
        }
        System.out.print(indent);
        if (isRight) {
            System.out.print(" /");
        } else {
            System.out.print(" \\");
        }
        System.out.print("----- ");
        printNodeValue();
        if (left != null) {
            left.printTree(false, indent + (isRight ? " |      " : "        "));
        }
    }

}