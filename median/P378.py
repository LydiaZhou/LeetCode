class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        min = matrix[0][0]
        max = matrix[len(matrix) - 1][len(matrix[0]) - 1] + 1
        while min < max:
            count = 0
            mid = (min + max) // 2
            for i in range(len(matrix)):
                j = 0
                while (j < len(matrix[0]) and matrix[i][j] <= mid):
                    j += 1
                count += j
            if count < k:
                min = mid + 1
            else:
                max = mid
            # k -= count
        return min

if __name__ == '__main__':
    obj = Solution()
    print(obj.kthSmallest([[1,2],[1,3]], 3))
