class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0:
            return True
        returnVal = False
        for i in range(1, len(s) + 1):
            word = s[:i]
            if s[:i] in wordDict:
                returnVal |= self.wordBreak(s[i:], wordDict)
                if returnVal:
                    return True
        return returnVal


if __name__ == '__main__':
    obj = Solution()
    print(obj.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(obj.wordBreak("applepenapple", ["apple", "pen"]))
