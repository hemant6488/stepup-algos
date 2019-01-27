# Given a singly linked list of N nodes. The task is to find middle of the linked list. For example, if given linked list is 1->2->3->4->5 then output should be 3. 

# If there are even nodes, then there would be two middle nodes, we need to print second middle element. For example, if given linked list is 1->2->3->4->5->6 then output should be 4.

# Input:
# First line of input contains number of testcases T. For each testcase, first line of input contains length of linked list and next line contains data of nodes of linked list.

# Output:
# For each testcase, there will be a single line of output containing data of middle element of linked list.

# User Task:
# The task is to complete the function getMiddle() which takes head reference as the only argument and should return the data at the middle node of linked list.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 100

# Example:
# Input:
# 2
# 5
# 1 2 3 4 5
# 6
# 2 4 6 7 5 1

# Output:
# 3
# 7

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = node(data)
        else:
            newNode = node(data)
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = newNode

def createLinkedListFromList(l):
    linkedList = LinkedList()
    for value in l:
        linkedList.insert(value)
    return linkedList


def findMid(linkedList):
    counter = 0
    itr = linkedList.head
    mid = linkedList.head

    while itr.next:
        if counter % 2 != 0:
            mid = mid.next
        itr = itr.next
        counter += 1

    if counter % 2 != 0:
        mid = mid.next

    return mid.data


def printLinkedList(linkedList):

    if linkedList.head == None:
        print("Empty List")

    itr = linkedList.head
    while itr is not None:
        print(str(itr.data), end=" -> ")
        if itr.next is None:
            print("None")
        itr = itr.next



if __name__ == "__main__":
    totalCases = int(input())

    for case in range(totalCases):
        numberOfElements = int(input())
        inputList = [int(z) for z in input().strip().split(" ")]
        linkedList = createLinkedListFromList(inputList)
        printLinkedList(linkedList)

        print(findMid(linkedList))





