class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        minArea = float('inf')
        rows = {}
        for point in points:
            row, col = point[0], point[1]
            if row in rows:
                rows[row].append(col)
            else:
                rows[row] = [col]

        while rows:
            minRow = min(rows.keys())
            curLine = rows[minRow]
            rows.pop(minRow)
            for (key, vals) in rows.items():
                joinedSet = set(curLine) & set(vals)
                if len(joinedSet) >= 2:
                    while joinedSet:
                        cur = joinedSet.pop()
                        for pos in joinedSet:
                            area = abs(minRow - key) * abs(cur - pos)
                            if area < minArea:
                                minArea = area
        if minArea == float('inf'):
            return 0
        return minArea

if __name__ == '__main__':
    obj = Solution()
    print(obj.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))

