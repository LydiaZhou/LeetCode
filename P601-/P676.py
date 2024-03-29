class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordsdic={}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i in dict:
            self.wordsdic[len(i)]=self.wordsdic.get(len(i),[])+[i]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for candi in self.wordsdic.get(len(word),[]):
                countdiff=0
                for j in range(len(word)):
                    if candi[j]!=word[j]:
                        countdiff+=1
                if countdiff==1:
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MagicDictionary()
    obj.buildDict(["hello", "hallo", "leetcode"])
    print(obj.search("hello"))
    print(obj.search("hhllo"))
    print(obj.search("hell"))
    print(obj.search("leetcoded"))