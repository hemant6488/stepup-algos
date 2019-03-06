package LinkedList;

/**
 * Created by hemantkumar on 08/02/19.
 */

class ListNode{
    int val;
    ListNode next;

    ListNode(int val){
        this.val = val;
    }
}

public class ReverseLinkedListKGroup {

    static class LinkedList{
        ListNode root;

        LinkedList(int val){
            ListNode node = new ListNode(val);
            this.root = node;
        }

        public void insert(int val){
            ListNode node = new ListNode(val);

            ListNode iterator = root;
            while(iterator.next != null){
                iterator = iterator.next;
            }
            iterator.next = node;
        }

        public void print(){
            ListNode iterator = root;
            while(iterator != null){
                System.out.print(iterator.val + " -> ");
                iterator=iterator.next;
            }
            System.out.println("null");
        }
    }

    public static void main(String args[]){
        LinkedList linkedList = new LinkedList(1);
        linkedList.insert(2);
        linkedList.insert(3);
        linkedList.insert(4);
        linkedList.insert(5);
        linkedList.insert(6);
        int k = 3;
        linkedList.print();
        reverseKGroup(linkedList.root, k);
    }

    public static ListNode reverseKGroup(ListNode head, int k) {
        return head;
    }


}
