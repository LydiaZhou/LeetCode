import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0, 1, 2, 3]
        for i in range(4, n + 1):
            sqrtNum = math.floor(math.sqrt(i))
            possibles = []
            for j in range(1, sqrtNum + 1):
                possibles.append(arr[i - j * j] + 1)
            arr.append(min(possibles))
        return arr[n]

if __name__ == '__main__':
    a = Solution()
    print(a.numSquares(12))