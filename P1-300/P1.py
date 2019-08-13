class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedNums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = sortedNums[left] + sortedNums[right]
            if sum > target:
                right -= 1
            elif sum == target:
                if sortedNums[left] == sortedNums[right]:
                    indexLeft = nums.index(sortedNums[left])
                    return [indexLeft, nums.index(sortedNums[right], indexLeft + 1, len(nums))]
                return [nums.index(sortedNums[left]), nums.index(sortedNums[right])]
            else:
                left += 1

if __name__ == '__main__':
    obj = Solution()
    print(obj.twoSum([3,3], 6))
