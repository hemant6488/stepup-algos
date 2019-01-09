#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    pairs = 0

    i = 0
    while i < n-1:
        if ar[i] == ar[i+1]:
            pairs += 1
            i += 2
        else:
            i += 1
    return pairs

if __name__ == '__main__':
    n = int(input())
    ar = [int(z) for z in input().rstrip().split()]
    result = sockMerchant(n, ar)
    print(result)
