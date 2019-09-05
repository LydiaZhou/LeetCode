class Solution(object):
    # add a momerization to reduce the time comsumption
    def splitArrayBFS(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        localMax = int(sum(nums)/m)
        memory = [[-1]*len(nums) for x in range(m + 1)]

        def bfs(index, localM):
            if memory[localM][index] != -1:
                return memory[localM][index]
            if localM == 1:
                returnVal = sum(nums[index:])
                memory[localM][index] = returnVal
                return returnVal
            # several types of deviding
            minVal = float('inf')
            curSum = 0
            for i in range(index, len(nums) - 1):
                curSum += nums[i]

                tryVal = max(curSum, bfs(i + 1, localM - 1))
                if tryVal < minVal:
                    minVal = tryVal
                i += 1
            memory[localM][index] = minVal
            return minVal

        bfs(0, m)
        return memory[m][0]

    # binarysearch
    def splitArray(self, nums, m):
        def check(mid):
            count = 0
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > mid:
                    curSum = num
                    count += 1
            count += 1
            return count <= m

        right = sum(nums)
        left = max(nums)
        while left < right:
            mid = (left + right)//2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    obj = Solution()
    # print(obj.splitArray([10,5,13,4,8,4,5,11,14,9,16,10,20,8], 8))
    print(obj.splitArray([2,3,1,2,4,3], 5))


# def bfs(index, localM, maxVal):
#     if localM == 1:
#         returnVal = sum(nums[index:])
#         memory[localM][index] = returnVal
#         return returnVal
#     partSum = 0
#     while index < len(nums):
#         if memory[localM][index] != -1:
#             return memory[localM][index]
#         partSum += nums[index]
#         if partSum >= maxVal:
#             lessThanTry = max(maxVal, bfs(index, localM - 1, maxVal))
#             largerThanTry = max(partSum, bfs(index + 1, localM - 1, partSum))
#             returnVal = min(lessThanTry, largerThanTry)
#             memory[localM][index + 1] = returnVal
#             return returnVal
#         index += 1
