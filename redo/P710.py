import random

class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.N = N
        self.length = N - len(blacklist)
        blacklist.sort()
        blacklistSet = set(blacklist)
        self.dict = {}
        index = 0
        for i in range(self.length, N):
            if i not in blacklistSet:
                self.dict[blacklist[index]] = i
                index += 1

    def pick(self):
        """
        :rtype: int
        """
        num = random.randint(0, self.length - 1)
        if num in self.dict:
            return self.dict[num]
        return num
