
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            ## Select the number at the first position
            current = nums[i]
            if i > 0 and current == nums[i-1]:
                continue
            ## The 2,3nd position are slected by (left, right) using sorted List
            left = i+1
            right = len(nums) - 1
            while left < right:
                ## move left or right based on the sum
                sum = nums[left] + nums[right] + current
                if sum == 0:
                    result.append([nums[left], nums[right], current])
                    while left<right and nums[left + 1] == nums[left]:
                        left += 1
                    while left<right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < 0:
                    # while left<right and nums[left + 1] == nums[left]:
                    #     left += 1
                    left += 1
                else:
                    # while left<right and nums[right - 1] == nums[right]:
                    #     right -= 1
                    right -= 1
        return result


if __name__ == '__main__':
    a = Solution()
    # print(a.threeSum([-1, 0, 1, 2, -1, -4]))
    print(a.threeSum([0,0,0]))