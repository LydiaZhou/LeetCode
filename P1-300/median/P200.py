class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islandCount = 0
        stack = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs((i, j), grid)
                    islandCount += 1
        return islandCount

    def dfs(self, tuple, grid):
        (i, j) = tuple
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "v"
        self.dfs((i + 1, j), grid)
        self.dfs((i - 1, j), grid)
        self.dfs((i, j + 1), grid)
        self.dfs((i, j - 1), grid)

if __name__ == '__main__':
    a = Solution()
    print(a.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))