# Given a binary number, write a program that prints 1 if given binary number is a multiple of 3.  Else prints 0. The given number can be big upto 2^100. It is recommended to finish the task using one traversal of input binary string.

# Input:
# The first line contains T denoting the number of testcases. Then follows description of testcases. 
# Each case contains a string containing 0's and 1's.

# Output:
# For each test case, output a 1 if string is multiple of 3, else 0.

# Constraints:
# 1<=T<=100
# 1<=Length of Input String<=100

# Example:
# Input:
# 2
# 011
# 100

# Output:
# 1
# 0


import time


def isMultipleOf3(binaryString):
    if binaryString == '0':
        return 1
    if binaryString == '1':
        return 0

    stringAsList = list(binaryString)
    i, N = 0, len(stringAsList)
    oddCount, evenCount = 0, 0
    while i < N:
        if stringAsList[i] == '1' and i % 2 == 0:
            evenCount += 1
        elif stringAsList[i] == '1' and i % 2 != 0:
            oddCount += 1
        i += 1
    if abs(oddCount - evenCount) % 3 == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    numberOfTests = int(input())
    for _ in range(numberOfTests):
        binaryString = input()
        # start = time.time()
        output = isMultipleOf3(binaryString)
        print(output)
        # print("Time elapsed: {}".format(time.time() - start))
