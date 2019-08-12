class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # result = None
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        if n%2 == 1:
            return x * self.myPow(x, n - 1)
        return self.myPow(x*x, n/2)

if __name__ == '__main__':
    a = Solution()
    print(a.myPow(2.00000, -2))
