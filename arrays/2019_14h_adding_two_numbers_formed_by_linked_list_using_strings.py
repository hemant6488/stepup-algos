import time


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1, l2):

    numberStr1, numberStr2 = "", ""
    while l1 is not None:
        numberStr1 = str(l1.val) + numberStr1
        l1 = l1.next
    while l2 is not None:
        numberStr2 = str(l2.val) + numberStr2
        l2 = l2.next

    total = int(numberStr1) + int(numberStr2)
    return createLinkedListFromList(list(str(total))[::-1])
    




def createLinkedListFromList(l):
    linkedList = None
    prevNode = None
    for val in l: 
        listNode = ListNode(val)

        if linkedList is None:
            linkedList = listNode
             
        if prevNode is not None:
            prevNode.next = listNode
        prevNode = listNode

    return linkedList


def printLinkedList(linkedList):
    if linkedList == None:
        print("Empty List")

    while linkedList is not None:
        print(str(linkedList.val), end=" -> ")
        if linkedList.next is None:
            print("None")
        linkedList = linkedList.next


if __name__ == "__main__":
    list1 = [int(z) for z in input().strip().split()]
    list2 = [int(z) for z in input().strip().split()]

    linkedList1 = createLinkedListFromList(list1)
    linkedList2 = createLinkedListFromList(list2)

    start = time.time()
    result = addTwoNumbers(linkedList1, linkedList2)
    print("Execution time: {}s".format(time.time() - start))
    printLinkedList(result)


    







