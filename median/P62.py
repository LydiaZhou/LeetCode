class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        if n > m:
            return self.fractorial(n, m + n - 1) // self.fractorial(1, m)
        else:
            return self.fractorial(m, m + n - 1) // self.fractorial(1, n)

    def fractorial(self, m, n):
        res = 1
        for i in range(m, n):
            res *= i
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.uniquePaths(7, 3))