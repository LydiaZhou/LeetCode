class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start = []
        end = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        start.sort()
        end.sort()
        s = e = 0
        roomCount = 0
        while s < len(start):
            if start[s] < end[e]:
                roomCount += 1
                s += 1
            else:
                s += 1
                e += 1
        return roomCount

if __name__ == '__main__':
    obj = Solution()
    print(obj.minMeetingRooms([[5, 10],[15, 20],[0, 30]]))