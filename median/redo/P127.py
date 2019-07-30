import string

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        stack = [(beginWord, 1)]
        while stack:
            (word, length) = stack.pop(0)
            if word == endWord:
                return length

            for i in range(len(word)):
                for char in string.ascii_lowercase:
                    formed = word[:i] + char + word[i+1:]
                    if formed in wordList:
                        stack.append((formed, length + 1))
                        wordList.remove(formed)
        return 0

if __name__ == '__main__':
    obj = Solution()
    print(obj.ladderLength("a", "c", ["a","b","c"]))