# Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given
# number.
#
# Input: The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
# Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and
#  S is the sum. The second line of each test case contains N space separated integers denoting the array elements.
#
# Output: For each test case, in a new line, print the starting and ending positions(1 indexing) of first such
# occurring subarray from the left if sum equals to subarray, else print -1.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 1 <= Ai <= 1010
#
# Example:
# Input:
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10
# Output:
# 2 4
# 1 5

totalTests = int(input())

for test in range(totalTests):
    inputStr = input().strip().split(" ")
    totalElements = int(inputStr[0])
    desiredSum = int(inputStr[1])

    intArray = [int(z) for z in input().strip().split(" ")]
    currentSum, startPos, found = intArray[0], 0, False

    i = 1
    while i <= len(intArray):
        while currentSum > desiredSum and startPos < i-1:
            currentSum = currentSum - intArray[startPos]
            startPos += 1

        if currentSum == desiredSum:
            found = True
            print("{} {}".format(startPos+1, i))
            break

        if i < len(intArray):
            currentSum += intArray[i]

        i += 1

    if not found:
        print(-1)
