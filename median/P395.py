class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for char in set(s):
            if s.count(char) < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
        return len(s)

if __name__ == '__main__':
    obj = Solution()
    print(obj.longestSubstring("ababacb", 3))