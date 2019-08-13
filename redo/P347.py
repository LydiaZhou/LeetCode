import collections

class Solution(object):
    # Bucket sort
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freqHashMap = collections.Counter(nums)
        # freqHashMap = {}
        # for num in nums:
        #     # freqHashMap.setdefault(num, 0)
        #     if num not in freqHashMap:
        #         freqHashMap[num] = 1
        #     else:
        #         freqHashMap[num] += 1

        # Start bucket sort
        bucket = [list() for i in range(len(nums) + 1)]
        for (key, val) in freqHashMap.items():
            bucket[val].append(key)

        # Using the result of bukcets
        ptr = len(bucket) - 1
        resultList = []
        count = 0
        while ptr >= 0 and count < k:
            if len(bucket[ptr]) != 0:
                count += len(bucket[ptr])
                resultList += bucket[ptr]
            ptr -= 1
        return resultList

if __name__ == '__main__':
    a = Solution()
    print(a.topKFrequent([4,1,-1,2,-1,2,3], 2))