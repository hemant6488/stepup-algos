# Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing
# number is to be found.
#
# Input: The first line of input contains an integer T denoting the number of test cases. For each test case first
# line contains N(size of array). The subsequent line contains N-1 array elements.
#
# Output:
# Print the missing number in array.
#
# Constraints:
# 1 ≤ T ≤ 200
# 1 ≤ N ≤ 107
# 1 ≤ C[i] ≤ 107
#
# Example:
# Input:
# 2
# 5
# 1 2 3 5
# 10
# 1 2 3 4 5 6 7 8 10
#
# Output:
# 4
# 9

totalTests = int(input())

for test in range(totalTests):
    numberOfIntegers = int(input())
    intArray = [int(z) for z in input().strip().split(" ")]

    # since integer list starts from 1 to N, the missing number can be found out by subtracting the calculated sum of
    # N-1 numbers from the total sum of numbers from 1 to N (which is N(N+1)/2)

    totalSum = (numberOfIntegers * (numberOfIntegers + 1)) / 2
    inputSum = sum(intArray)

    missingNumber = totalSum - inputSum
    print(int(missingNumber))
