import bisect


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return nums
        counts = [-1] * (len(nums) - 1) + [0]
        sortedRight = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            count = bisect.bisect_left(sortedRight, nums[i])
            sortedRight.insert(count, nums[i])
            counts[i] = count
        return counts
