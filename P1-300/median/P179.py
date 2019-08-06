import functools


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num = [str(x) for x in nums]
        num.sort(key=functools.cmp_to_key(lambda b, a: ((a + b) > (b + a)) - ((a + b) < (b + a))))
        return ''.join(num).lstrip('0') or '0'

if __name__ == '__main__':
    a = Solution()
    print(a.largestNumber([3, 30, 34, 5, 9]))