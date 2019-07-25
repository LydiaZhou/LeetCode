class Solution(object):
    def maxArea(self, height):
        maxWater = 0
        i = 0
        j = len(height) - 1
        while i < j:
            leftHeight = height[i]
            rightHeight = height[j]
            maxWater = max(maxWater, min(leftHeight, rightHeight) * (j - i))
            if leftHeight < rightHeight:
                i += 1
            elif leftHeight > rightHeight:
                j -= 1
            else:
                i += 1
                j -= 1
        return maxWater

if __name__ == '__main__':
    a = Solution()
    print(a.maxArea([1,8,6,2,5,4,8,3,7]))