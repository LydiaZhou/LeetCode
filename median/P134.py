class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # if sum(cost) > sum(gas):
        #     return -1
        startPoint = 0
        currentGas = 0
        for j in range(len(gas)*2 -1):
            i = j
            if j >= len(gas):
                i = j - len(gas)
            currentGas += (gas[i] - cost[i])
            if currentGas < 0:
                if startPoint >= len(gas):
                    return -1
                startPoint = i + 1
                currentGas = 0
        return startPoint

if __name__ == '__main__':
    a = Solution()
    print(a.canCompleteCircuit([4,5,2,6,5,3],[3,2,7,3,2,9]))
