import math

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        right = sum(weights)
        left = max(weights)
        while left<right:
            mid = (left+right)//2
            oneDay = 0
            dayCount = 0
            for weight in weights:
                oneDay += weight
                if oneDay > mid:
                    oneDay = weight
                    dayCount += 1
                    if dayCount > D:
                        break
            if dayCount < D:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    obj = Solution()
    print(obj.shipWithinDays([1,2,3,1,1], 4))