class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        helper = 1
        result = []
        for i in range(len(nums)):
            result.append(helper)
            helper *= nums[i]
        # reversely
        helper = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= helper
            helper *= nums[i]
        return result

if __name__ == '__main__':
    obj = Solution()
    print(obj.productExceptSelf([1,2,3,4]))