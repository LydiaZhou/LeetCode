class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        intervals = sorted(intervals, key=lambda i: i[0])
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i][1] < intervals[i+1][1]:
                    intervals[i][1] = intervals[i+1][1]
                intervals.pop(i+1)
            else:
                i += 1
        return intervals

if __name__ == '__main__':
    obj = Solution()
    print(obj.merge([[1,4],[2,3]]))