class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        result = []
        pos = (0, 0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        directIndex = 0
        while(len(result) != m*n):
            if pos[0] < 0 or pos[1] < 0 or pos[0] >= m or pos[1] >= n:
                directIndex += 1