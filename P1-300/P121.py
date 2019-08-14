class Solution(object):
    # exceed time limit
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for i in range(len(prices) -1):
            profit = max(prices[i + 1:]) - prices[i]
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit

    def maxProfit(self, prices):
        maxProfit = 0
        minVal = float('inf')
        for i in range(len(prices)):
            minVal = min(minVal, prices[i])
            profit = prices[i] - minVal
            maxProfit = max(maxProfit, profit)
        return maxProfit


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxProfit([7,1,5,3,6,4]))
