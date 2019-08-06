class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return
        nums = sorted(nums)
        dp = [[nums[0]]]
        for i in range(1, len(nums)):
            itr = i - 1
            tmpSet= []
            while itr >= 0:
                if nums[i] % nums[itr] == 0 and len(dp[itr]) > len(tmpSet):
                    tmpSet = dp[itr].copy()
                itr -= 1
            tmpSet.append(nums[i])
            dp.append(tmpSet)
        result = []
        for subdp in dp:
            if len(subdp) > len(result):
                result = subdp
        return result

if __name__ == '__main__':
    obj = Solution()
    print(obj.largestDivisibleSubset([1,2,3]))