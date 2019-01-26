# Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of platforms required for the railway station so that no train waits.
# Note: Consider that all the trains arrive on the same day and leave on the same day. Also, arrival and departure times must not be same for a train.

# Input:
# The first line of input contains T, the number of test cases. For each test case, first line will contain an integer N, the number of trains. Next two lines will consist of N space separated time intervals denoting arrival and departure times respectively.
# Note: Time intervals are in the 24-hour format(hhmm), preceding zeros are insignificant. 200 means 2:00.
# Consider the example for better understanding of input.

# Output:
# For each test case, print the minimum number of platforms required for the trains to arrive and depart safely.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 1000
# 1 <= A[i] < D[i] <= 2359

# Example:
# Input:
# 1
# 6 
# 900  940 950  1100 1500 1800
# 910 1200 1120 1130 1900 2000

# Output:
# 3

import re


def getMinimumPlatformsNeeded(n, arr, dep):
    arr.sort()
    dep.sort()

    maxPlatforms = 1
    platformCount = 1

    i, j = 1,0

    # print(arr)
    # print(dep)
    while (i<n and j<n):
        if arr[i] < dep[j]:
            platformCount += 1
            i += 1

            if platformCount > maxPlatforms:
                maxPlatforms = platformCount
        else:
            platformCount -= 1
            j += 1

    return maxPlatforms


if __name__ == "__main__":
    totalCases = int(input())

    for case in range(totalCases):
        n = int(input())
        arrivalInput = re.sub(" +", " ", input())
        arrival = [int(z) for z in arrivalInput.strip().split(" ")]
        departureInput = re.sub(" +", " ", input())
        departure = [int(z) for z in departureInput.strip().split(" ")]

        minimumPlatforms = getMinimumPlatformsNeeded(n, arrival, departure)
        print(minimumPlatforms)