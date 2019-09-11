class Solution(object):
    def updateMatrix(self, matrix):
        """m
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return
        resultMap = [list() for i in range(m)]

        # from top left
        for i in range(len(matrix)):
            for j in range(n):
                if matrix[i][j]== 0:
                    resultMap[i].append(0)
                else:
                    if i > 0 and j > 0:
                        resultMap[i].append(min(resultMap[i - 1][j], resultMap[i][j - 1]) + 1)
                    elif i > 0:
                        resultMap[i].append(resultMap[i - 1][j] + 1)
                    elif j > 0:
                        resultMap[i].append(resultMap[i][j - 1] + 1)
                    else:
                        resultMap[i].append(m+n)

        # from bottom right
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 0:
                    continue
                if i < m - 1 and j < n - 1:
                    resultMap[i][j] = min(min(resultMap[i + 1][j], resultMap[i][j + 1]) + 1, resultMap[i][j])
                elif i < m - 1:
                    resultMap[i][j] = (min(resultMap[i + 1][j] + 1, resultMap[i][j]))
                elif j < n - 1:
                    resultMap[i][j] = (min(resultMap[i][j + 1] + 1, resultMap[i][j]))
        return resultMap

if __name__ == '__main__':
    obj = Solution()
    print(obj.updateMatrix(
[[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]))
