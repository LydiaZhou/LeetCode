class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        hashmap = {}
        left = right = 0
        while right < len(s):
            char = s[right]
            if char in hashmap:
                ## Left cannot be move backward, so make sure the movement is towards right
                left = max(hashmap[char] + 1, left)
            hashmap[char] = right
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen

if __name__ == '__main__':
    a = Solution()
    print(a.lengthOfLongestSubstring("pwwkew"))





