import time


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1, l2):
    number1, number2 = 0, 0

    multiplier = 1
    while l1 is not None:
        number1 += (l1.val * multiplier)
        l1 = l1.next
        multiplier *= 10

    multiplier = 1
    while l2 is not None:
        number2 += (l2.val * multiplier)
        l2 = l2.next
        multiplier *= 10

    total = number1 + number2

    if total == 0: 
        resultHead = ListNode(0)
    else:
        resultHead = None
        previousNode = None
        while 1 <= total:
            number = total % 10
            total //= 10

            listNode = ListNode(number)
            if resultHead is None:
                resultHead = listNode

            if previousNode is not None:
                previousNode.next = listNode

            previousNode = listNode

    return resultHead


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


    







