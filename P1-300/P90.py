class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numDict = {}
        for num in nums:
            numDict[num] = numDict.get(num, 0) + 1
        result = [[]]
        for key, val in numDict.items():
            oriLen = len(result)
            for i in range(1, val+1):
                for j in range(oriLen):
                    withINum = result[j].copy()
                    withINum += [key] * i
                    result.append(withINum)
        return result