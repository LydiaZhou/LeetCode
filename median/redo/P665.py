class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        decreaseCount = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if i < 1 or nums[i - 1] < nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                decreaseCount += 1
            if decreaseCount >= 2:
                return False
        return True


if __name__ == '__main__':
    obj = Solution()
    print(obj.checkPossibility([3,4,2,3]))

