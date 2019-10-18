# twitter OA P1
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#

def bisect(nums, num):
    """
    binary search function
    """
    left, right = 0, len(nums)
    while left + 1 < right:
        mid = (right - left) // 2 + left
        if nums[mid] < num:
            left = mid
        elif nums[mid] > num:
            right = mid
        else:
            return mid
    return left if left < len(nums) and nums[left]==num else right


def kDifference(a, k):
    # Write your code here
    a.sort()
    # the i as index tracking of the smaller number; j is the position of a[i]+k
    i = 0
    j = bisect(a, a[i] + k)
    count = 0
    while j < len(a):
        if a[i] + k == a[j]:
            count += 1
        # update i and j
        i += 1
        j = bisect(a[i+1:], a[i] + k) + i + 1
    return count

if __name__ == '__main__':
    print(kDifference([2, 4, 6, 8, 10, 12], 2))
    # print(kDifference([2,4,5,6,7,8,12], 2))