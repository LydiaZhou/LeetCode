#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindrome(s):
    resultSet = set()
    dpList = [[0]*len(s) for i in range(len(s))]
    for i in range(len(s), -1, -1):
        for j in range(i, len(s)):
            if (s[i] == s[j] and (j - i < 2 or dpList[i + 1][j - 1])):
                dpList[i][j] = 1
                resultSet.add(s[i:j + 1])
    return len(resultSet)

if __name__ == '__main__':
    print(palindrome("aabaa"))