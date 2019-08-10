class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islands = []
        # dfs
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = self.bfs(grid, i, j)
                    (startI, startJ) = island[0]
                    for x in range(len(island)):
                        island[x] = (island[x][0] - startI, island[x][1] - startJ)
                    if island not in islands:
                        islands.append(island)
        return len(islands)

    def bfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == 1:
            grid[i][j] = -1
            returnList = [(i,j)]
            down = self.bfs(grid, i + 1, j)
            if down:
                returnList += down
            up = self.bfs(grid, i - 1, j)
            if up:
                returnList += up
            right = self.bfs(grid, i, j + 1)
            if right:
                returnList += right
            left = self.bfs(grid, i, j - 1)
            if left:
                returnList += left
            return returnList

if __name__ == '__main__':
    obj = Solution()
    # print(obj.numDistinctIslands([[1,1,0,0,0], [1,1,0,0,0], [0,0,0,1,1], [0,0,0,1,1]]))
    # print(obj.numDistinctIslands([[1,1,0,1,1], [1,0,0,0,0], [0,0,0,0,1], [1,1,0,1,1]]))
    print(obj.numDistinctIslands([[1, 1]]))