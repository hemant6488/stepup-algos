# Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

# Input:
# The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow. Each testcases contains two lines of input. The first line denotes the size of the array N. The second lines contains the elements of the array A separated by spaces.

# Output: 
# For each testcase, print the sorted array.

# Constraints: 
# 1 <= T <= 500
# 1 <= N <= 106
# 0 <= Ai <= 2

# Example:
# Input :
# 2
# 5
# 0 2 1 2 0
# 3
# 0 1 0

# Output:
# 0 0 1 2 2
# 0 0 1

totalTests = int(input())

for i in range(totalTests):
    numberOfElements = int(input().strip())
    array = [int(z) for z in (input().strip().split(" "))]

    low = 0
    mid = 0
    high = len(array) - 1

    while mid <= high:
        if array[mid] == 0:
            array[mid], array[low] = array[low], array[mid]
            mid += 1
            low += 1
        
        elif array[mid] == 1:
            mid += 1

        else:
            array[mid], array[high] = array[high], array[mid]
            high -= 1

    # Print array
    outputStr = ""
    for j in range(len(array)):
        outputStr += str(array[j]) + " "

    print(outputStr)