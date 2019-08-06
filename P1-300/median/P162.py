class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (high - low) //2 + low
            mid2 = mid + 1
            if nums[mid2] > nums[mid]:
                low = mid2
            else:
                high = mid
        return low

if __name__ == '__main__':
    a = Solution()
    print(a.findPeakElement([1,2,1,3,5,6,4]))