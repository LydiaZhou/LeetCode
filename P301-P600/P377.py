class Solution(object):
    def combinationSum42(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 1
        if target < 0:
            return 0
        counts = []
        for num in nums:
            counts.append(self.combinationSum4(nums, target - num))
        return sum(counts)

    def combinationSum4(self, nums, target):
        dp = [1]
        for i in range(1, target + 1):
            count = 0
            for num in nums:
                if i - num >= 0:
                    count += dp[i - num]
            dp.append(count)
        return dp[target]


if __name__ == '__main__':
    obj = Solution()
    print(obj.combinationSum4([1, 2, 3], 4))
