class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for i,num in enumerate(nums):
            oriLength = len(result)
            for j in range(oriLength):
                withNum = result[j].copy()
                withNum.append(num)
                result.append(withNum)
        return result
