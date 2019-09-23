import string, random
import collections, itertools

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
   def guess(self, word):
       """
       :type word: str
       :rtype int
       """

class Solution:
    def match(self, a, b):
        return sum(i == j for i, j in zip(a, b))

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        rightCount = 0
        while rightCount < 6:
            zeroSameCount = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if self.match(w1, w2) == 0)
            guess = min(wordlist, key=lambda c: zeroSameCount[c])
            rightCount = master.guess(guess)
            wordlist = [word for word in wordlist if word != guess and self.match(word, guess) == rightCount]



if __name__ == '__main__':
    wordlist = set()
    while len(wordlist) != 100:
        word = ''.join(random.choice(string.ascii_lowercase) for x in range(6))
        wordlist.add(word)
    wordlist = list(wordlist)
    count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if match(w1, w2) == 0)

    obj = Solution()
    # testCase = set()
    # while len(testCase) != 100:
    #     word = ''.join(random.choice(string.ascii_lowercase) for x in range(6))
    #     testCase.add(word)
    # print(testCase)