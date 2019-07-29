class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = ones = 0
        for i in range(len(nums)):
            val = nums[i]
            nums[i] = 2
            if val < 2:
                nums[ones] = 1
                ones += 1
            if val == 0:
                nums[zeros] = 0
                zeros += 1
        return nums

if __name__ == '__main__':
    obj = Solution()
    print(obj.sortColors([2,0,2,1,1,0]))