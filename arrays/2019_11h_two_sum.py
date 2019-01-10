# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# def twoSum(nums, target):
#     for idx, val in enumerate(nums):
#         for idx2, val2 in enumerate(nums[idx+1:]):
#             if val == (target - val2):
#                 return [idx, idx2 + idx + 1]

import time


def twoSum(nums, target):
    dictionary = {}

    for idx, val in enumerate(nums):
        if (target - val) in dictionary.keys():
            return [dictionary[target - val], idx]
        else:
            dictionary[val] = idx


if __name__ == "__main__":
    arrayInput = [int(z) for z in input().strip().split()]
    targetSum = int(input())

    start = time.time()
    output = twoSum(arrayInput, targetSum)
    print(output)
    print("Execution time: {}s".format(time.time() - start))
