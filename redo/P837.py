class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0:
            return 1
        dpList = [0] * (N + 1)
        dpList[0] = 1
        theNum = 1
        for i in range(1, N+1):
            dpList[i] = theNum / W
            if i < K:
                theNum += dpList[i]
            if i - W >= 0:
                theNum -= dpList[i - W]
            # for j in range(max(0, i - W), min(i, K)):
            #     dpList[i] += dpList[j] * 1/W

        return sum(dpList[K:])


if __name__ == '__main__':
    obj = Solution()
    print(obj.new21Game(1, 0, 1))
    print(obj.new21Game(21, 17, 10))