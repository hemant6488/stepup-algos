# Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array.
# Equilibrium position in an array is a position such that the sum of elements below it is equal to the sum of elements after it.

# Input:
# The first line of input contains an integer T denoting the no of test cases then T test cases follow. First line of each test case contains an integer N denoting the size of the array. Then in the next line are N space separated values of the array A.

# Output:
# For each test case in a new  line print the position at which the elements are at equilibrium if no equilibrium point exists print -1.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 106
# 1 <= Ai <= 108

# Example:
# Input:
# 2
# 1
# 1
# 5
# 1 3 5 2 2

# Output:
# 1
# 3


def getIndexForEquilibrium(numberOfElements, array):
    totalSum = sum(array)
    rightSum = totalSum 
    i, leftSum = 0, 0

    while i < numberOfElements:
        # print("index: {}, left sum: {}, right sum: {}".format(i, leftSum, rightSum))
        leftSum += array[i] 
        if leftSum == rightSum:
            return i + 1
        rightSum -= array[i]
        i += 1
    return -1


if __name__ == "__main__":
    totalTests = int(input())

    for test in range(totalTests):
        numberOfElements = int(input())
        array = [int(z) for z in input().strip().split()]

        print(getIndexForEquilibrium(numberOfElements, array))