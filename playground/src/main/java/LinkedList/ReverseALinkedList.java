package LinkedList;

import java.util.Random;

/**
 * Created by hemantkumar on 06/02/19.
 */

class Node{
    int value;
    Node next;

    Node(int value){
        this.value = value;
        this.next = null;
    }
}

class LinkedList{
    Node root;

    LinkedList(int value){
        this.root = new Node(value);
    }

    public void insert(int value){
        Node node = new Node(value);

        Node itr = this.root;
        while(itr.next != null){
            itr = itr.next;
        }
        itr.next = node;
    }

    public void print(){
        Node itr = this.root;
        while(itr != null){
            System.out.print(itr.value + " -> ");
            itr = itr.next;
        }
        System.out.print("null\n");
    }
}
public class ReverseALinkedList {
    public static void main(String args[]){
        Random random = new Random(20);
        LinkedList linkedList = new LinkedList(25);

        for(int i=0; i<10; i++){
            linkedList.insert(random.nextInt(50));
        }

        linkedList.print();
        reverseList(linkedList);
        linkedList.print();
    }

    private static void reverseList(LinkedList linkedList) {
        Node prev, current, next;

        prev = null;
        current = linkedList.root;

        if(current == null){
            return;
        }


        while (current != null){
            next = current.next;
            current.next = prev;

            prev = current;
            current = next;
        }

        linkedList.root = prev;
    }
}
