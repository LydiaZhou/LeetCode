class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            currentVal = matrix[i][j]
            if currentVal < target:
                i += 1
            elif currentVal > target:
                j -= 1
            else:
                return True
        return False

if __name__ == '__main__':
    obj = Solution()
    print(obj.searchMatrix([], 0))