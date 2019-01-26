# Given an array of positive integers. Your task is to find the leaders in the array.
# Note: An element of array is leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader. 

# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
# The first line of each test case contains a single integer N denoting the size of array.
# The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

# Output:
# Print all the leaders.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 0 <= Ai <= 1018

# Example:
# Input:
# 3
# 6
# 16 17 4 3 5 2
# 5
# 1 2 3 4 0
# 5
# 7 4 5 7 3
# Output:
# 17 5 2
# 4 0
# 7 7 3


def findLeaders(length, array):
    leaders = []

    i = length - 2
    currentLeader = array[length - 1]
    while i >= 0:
        if array[i] >= currentLeader:
            leaders.append(currentLeader)
            currentLeader = array[i]
        i -=  1
    leaders.append(currentLeader)

    return leaders


if __name__ == "__main__":
    testCases = int(input())
    
    for case in range(testCases):
        length = int(input())
        array = [int(z) for z in input().strip().split(" ")]

        leaders = findLeaders(length, array)
        

        # Formatting output for submission.
        leaders = leaders[::-1]
        leaders = [str(z) for z in leaders]
        print(' '.join(leaders))

