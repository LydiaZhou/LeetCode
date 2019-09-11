class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        height = len(board)
        width = len(board[0])
        rotatedBoard = [[0]*height for i in range(width)]
        for i in range(height):
            for j in range(width):
                rotatedBoard[j][height - i - 1] = board[i][j]
        changed = True
        while(changed):
            changed = False
            zeros = [[0] * height for i in range(width)]
            for i in range(len(rotatedBoard)):
                for j in range(len(rotatedBoard[0])):
                    cur = rotatedBoard[i][j]
                    if cur == 0: continue
                    horizonCount = 1
                    while j + horizonCount < height and rotatedBoard[i][j+horizonCount] == cur:
                        horizonCount += 1
                    if horizonCount >= 3:
                        for x in range(horizonCount):
                            # changed the crushed as 0
                            zeros[i][j + x] = 1
                            changed = True
                    verticalCount = 1
                    while i + verticalCount < width and rotatedBoard[i + verticalCount][j] == cur:
                        verticalCount += 1
                    if verticalCount >= 3:
                        for x in range(verticalCount):
                            # changed the crushed as 0
                            zeros[i + x][j] = 1
                            changed = True
            a = 1
            # drop the uncrushed candys on top of zeros
            for i in range(len(rotatedBoard)):
                for j in range(len(rotatedBoard[0])):
                    if zeros[i][j] == 1:
                        rotatedBoard[i][j] = 0
                dropped = list(filter(lambda a: a != 0, rotatedBoard[i]))
                while len(dropped) != height:
                    dropped.append(0)
                rotatedBoard[i] = dropped
            a = 1
        for i in range(height):
            for j in range(width):
                board[i][j] = rotatedBoard[j][height - i - 1]
        return board


if __name__ == '__main__':
# Your MyCalendarTwo object will be instantiated and called as such:
    obj = Solution()
    # print(obj.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))
    print(obj.candyCrush([[2,1,3],[2,2,2],[2,2,2]]))
    # print(obj.candyCrush([[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]))