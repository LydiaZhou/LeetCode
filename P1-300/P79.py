class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        cur = word[0]
        returnVal = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                returnVal |= self.bfs(board, i, j, word)
                if returnVal:
                    return True
        return returnVal

    def bfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        cur = word[0]
        if cur != board[i][j]:
            return False
        # current right
        # newBoard = []
        # for x in range(len(board)):
        #     newBoard.append(board[x].copy())
        tmp = board[i][j]
        board[i][j] = ''
        res = self.bfs(board, i + 1, j, word[1:]) or self.bfs(board, i - 1, j, word[1:]) or \
               self.bfs(board, i, j + 1, word[1:]) or self.bfs(board, i, j - 1, word[1:])
        board[i][j] = tmp
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))


