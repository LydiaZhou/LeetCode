import copy

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                aliveNeigh = 0
                # Upper eadge
                if i - 1 >= 0:
                    aliveNeigh += board[i - 1][j]%2
                # Upper left neighbor
                if i - 1 >= 0 and j - 1 >= 0:
                    aliveNeigh += board[i - 1][j - 1]%2
                # Upper right
                if i - 1 >= 0 and j + 1 < len(board[0]):
                    aliveNeigh += board[i - 1][j + 1]%2
                # right
                if j + 1 < len(board[0]):
                    aliveNeigh += board[i][j + 1]%2
                # left
                if j - 1 >= 0:
                    aliveNeigh += board[i][j - 1]%2
                # lower
                if i + 1 < len(board):
                    aliveNeigh += board[i + 1][j]%2
                # lower left
                if i + 1 < len(board) and j - 1 >= 0:
                    aliveNeigh += board[i + 1][j - 1]%2
                # lower right
                if i + 1 < len(board) and j + 1 < len(board[0]):
                    aliveNeigh += board[i + 1][j + 1]%2

                # justify the status
                if board[i][j] == 0:
                    if aliveNeigh == 3:
                        board[i][j] = 2
                else:
                    if aliveNeigh < 2:
                        board[i][j] = 3
                    elif aliveNeigh > 3:
                        board[i][j] = 3
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
        return board

if __name__ == '__main__':
    obj = Solution()
    print(obj.gameOfLife([[1,1],[1,0]]))