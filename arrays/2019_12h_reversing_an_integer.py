# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120 Output: 21 Note: Assume we are dealing with an environment which could only store integers within the
# 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0
#  when the reversed integer overflows.

import time


def reverse(x):
    
    MAX_INT = (2**31) - 1
    MIN_INT = (-2**31)

    isNeg = True if x < 0 else False
    strX = str(x)
    reverseX = strX[::-1]

    if not reverseX == "0":
        reverseX = reverseX.lstrip('0')

    if isNeg:
        reverseX = reverseX[:-1]
        reverseX = "-" + reverseX

    if not (MIN_INT < int(reverseX) < MAX_INT):
        reverseX = 0

    return int(reverseX)


if __name__ == "__main__":
    integer = int(input())

    start = time.time()
    output = reverse(integer)
    print(output)
    print("Execution time: {}s".format(time.time() - start))

