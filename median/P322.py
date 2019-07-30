class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        list = [0]
        for i in range(1, amount + 1):
            tmpList = []
            for coin in coins:
                if i-coin >= 0 and list[i-coin] >= 0:
                    tmpList.append(list[i-coin])
            if len(tmpList) == 0:
                list.append(-1)
            else:
                list.append(min(tmpList)+1)
        return list[amount]

if __name__ == '__main__':
    obj = Solution()
    print(obj.coinChange([186,419,83,408],
6249))
