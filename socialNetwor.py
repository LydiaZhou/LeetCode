#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#

def countGroups(related):
    # DFS for counting islands
    visited = set()
    # following dictionary
    followings = {}
    for i in range(len(related)):
        for j in range(len(related)):
            if int(related[i][j]) == 1:
                if i in followings:
                    followings[i].append(j)
                else:
                    followings[i] = [j]
                # if j in followings:
                #     followings[j].append(i)
                # else:
                #     followings[j] = [i]

    # dfs helper function
    def dfs(i):
        if i in visited:
            return
        visited.add(i)
        for element in followings[i]:
            dfs(element)
        return
    count = 0
    for i in range(len(related)):
        for j in range(len(related)):
            if int(related[i][j]) == 1 and i not in visited:
                dfs(i)
                count += 1
    return count

if __name__ == '__main__':
    print(countGroups([[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]))