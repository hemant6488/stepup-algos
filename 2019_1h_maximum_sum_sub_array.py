# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
#
# Input: The first line of input contains an integer T denoting the number of test cases. The description of T test
# cases follows. The first line of each test case contains a single integer N denoting the size of array. The second
# line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.
#
# Output:
# Print the maximum sum of the contiguous sub-array in a separate line for each test case.
#
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 106
# -107 ≤ A[i] <= 107
#
# Example:
# Input
# 2
# 5
# 1 2 3 -2 5
# 4
# -1 -2 -3 -4
# Output
# 9
# -1


totalTests = int(input().strip())


for t in range(totalTests):
    numOfInts = int(input().strip())
    inputStr = input()
    temporaryList = inputStr.strip().split(" ")
    intArray = [int(z) for z in temporaryList]

    maximumSum = 0
    currentSum = 0
    for i in range(len(intArray)):
        if i == 0:
            maximumSum = intArray[i]
            currentSum = intArray[i]
        else:
            currentSum = currentSum + intArray[i]
            # print("Maximum Sum: {}, Current Sum: {}, Int: {}".format(maximumSum, currentSum, intArray[i]))
            if currentSum < intArray[i]:
                currentSum = intArray[i]

            if maximumSum < currentSum:
                maximumSum = currentSum

    print(maximumSum)
