class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        # Find pivot
        left = 0
        right = len(nums) -1
        while left < right:
            mid = (right + left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        # partition the left and right side
        if nums[0] > target:
            right = len(nums)
        elif nums[0] < target:
            if left == 0:
                right = len(nums)
            else:
                right = left
                left = 0
        else:
            return 0
        # normal binary search
        while left < right:
            mid = (left + right) //2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

if __name__ == '__main__':
    obj = Solution()
    print(obj.search([3, 5, 1], 5))