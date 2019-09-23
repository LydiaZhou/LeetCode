class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        cur = lower
        result = []

        for i, num in enumerate(nums):
            if num > cur + 1:
                result.append(str(cur) + "->" + str(num - 1))
            elif num == cur + 1:
                result.append(str(cur))
            cur = num + 1

        # check ending
        if upper > cur:
            result.append(str(cur) + "->" + str(upper))
        elif upper == cur:
            result.append(str(cur))
        return result

if __name__ == '__main__':
    obj = Solution()
    print(obj.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
    print(obj.findMissingRanges([1], 1, 1))
    print(obj.findMissingRanges([], 1, 1))
