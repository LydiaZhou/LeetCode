import collections

class Solution(object):
    # Exceed the time limit
    def wordBreak3(self, s, wordDict):
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

    # backtracing (exceed the time limit)
    def wordBreak4(self, s, wordDict):
        if len(s) == 0:
            return True
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
                return True
        return False

    # dp
    def wordBreak2(self, s, wordDict):
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i-len(word)+1:i+1] and (i-len(word) == -1 or dp[i-len(word)]):
                    dp[i] = True
                    continue
        return dp[-1]

    # bfs
    def wordBreak(self, s, wordDict):
        visited = set()
        queue = collections.deque()
        queue.append(0)
        while queue:
            current = queue.pop()
            visited.add(current)
            for i in range(current + 1, len(s) + 1):
                if i not in visited and s[current:i] in wordDict:
                    queue.append(i)
                    if i == len(s):
                        return True
        return False

if __name__ == '__main__':
    obj = Solution()
    print(obj.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(obj.wordBreak("applepenapple", ["apple", "pen"]))
