import math

# better solution possible
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        disPoint = []
        for point in points:
            dis = math.sqrt(pow(point[0], 2) + pow(point[1], 2))
            disPoint.append((dis, point))
        disPoint = sorted(disPoint)
        returnVal = []
        for i in range(K):
            returnVal.append(disPoint[i][1])
        return returnVal

if __name__ == '__main__':
    obj = Solution()
    print(obj.kClosest( [[3,3],[5,-1],[-2,4]], 2))
