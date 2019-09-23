class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dpList = [[0]* len(A) for i in range(len(B))]
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                if i == 0 or j == 0:
                    dpList[i][j] = 1 if a == b else 0
                else:
                    if a == b:
                        dpList[i][j] = dpList[i - 1][j - 1] + 1
                    else:
                        dpList[i][j] = 0
        return max(max(x) for x in dpList)

if __name__ == '__main__':
    obj = Solution()
    print(obj.findLength([1,2,3,2,1], [3,2,1,4,7]))