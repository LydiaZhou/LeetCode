class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left < right:
            count = 0
            for i in range(len(nums)):
                mid = (left + right) // 2
                if nums[i] <= mid:
                    count += 1
            if mid >= count:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == '__main__':
    obj = Solution()
    print(obj.findDuplicate([2,2,2,2,2]))