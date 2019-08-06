class Solution(object):
    def __init__(self):
        self.data = None

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.data = s
        palindrome = ""
        for i in range(len(s)):
            # Even situation
            currentVal = self.helper(s, i, i)
            if len(currentVal) > len(palindrome):
                palindrome = currentVal
            # Odd situation
            currentVal = self.helper(s, i, i+1)
            if len(currentVal) > len(palindrome):
                palindrome = currentVal
        return palindrome

    def helper1(self, left, right):
        if left < 0:
            return self.s[0:right]
        if right >= len(self.s):
            return self.s[left+1:]
        if self.s[left] == self.s[right]:
            left -= 1
            right += 1
            return self.helper(self.s, left, right)
        else:
            return self.s[left+1:right]

    def helper(self, s, left, right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return s[left+1:right]

if __name__ == '__main__':
    obj = Solution()
    print(obj.longestPalindrome("cbbd"))