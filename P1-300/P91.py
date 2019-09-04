class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if int(s[0]) != 0:
            dp = [1, 1]
        else:
            return 0
        for i in range(1, len(s)):
            two = int(s[i-1:i+1])
            curVal = 0
            if s[i] != "0":
                curVal += dp[i]
            if 9 < two <= 26:
                curVal += dp[i-1]
            dp.append(curVal)
        return dp[len(dp) - 1]

if __name__ == '__main__':
    obj = Solution()
    print(obj.numDecodings("110"))
    print(obj.numDecodings("101"))