# class Solution(object):
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """
#         if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
#             return 0
#         return self.bfs((0,0), obstacleGrid)
#
#     def bfs(self, current, grid):
#         if current[0] + 1 == len(grid) and current[1] + 1 == len(grid[0]):
#             return 1
#         if current[0] >= len(grid) or current[1] >= len(grid[0]):
#             return 0
#         if grid[current[0]][current[1]] == 1:
#             return 0
#         return self.bfs((current[0], current[1]+1), grid) + self.bfs((current[0]+1, current[1]), grid)

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
                    continue
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                if i - 1 < 0 :
                    obstacleGrid[i][j] =obstacleGrid[i][j - 1]
                    continue
                if j - 1 < 0 :
                    obstacleGrid[i][j] =obstacleGrid[i - 1][j]
                    continue
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]

if __name__ == '__main__':
    obj = Solution()
    print(obj.uniquePathsWithObstacles([[0,0]]))