class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        remaining = [x for x in range(1, N+1)]
        index = 1
        arrangement = 0
        for i in range(N):
            newRemain = remaining.copy()
            newRemain.pop(i)
            arrangement += self.backtrack(index, newRemain)
        return arrangement

    def backtrack(self, index, remaining):
        if len(remaining) == 0:
            return 1
        index += 1
        arrangement = 0
        for remains in remaining:
            if remains%index == 0 or index%remains == 0:
                newRemain = remaining.copy()
                newRemain.remove(remains)
                arrangement += self.backtrack(index, newRemain)
        return arrangement

if __name__ == '__main__':
    obj = Solution()
    print(obj.countArrangement(4))
