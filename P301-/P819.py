import string, re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        record = dict()
        maxWord = ""
        maxTimes = 0
        words = re.split(';|,| ', paragraph)
        for word in words:
            if len(word) == 0:
                continue
            word = word.strip(string.punctuation).lower()
            if word not in banned:
                if word in record:
                    record[word] += 1
                else:
                    record[word] = 1
                if record[word] > maxTimes:
                    maxTimes = record[word]
                    maxWord = word
        return maxWord

if __name__ == '__main__':
    obj = Solution()
    print(obj.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
