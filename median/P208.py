class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self
        while len(word) != 0:
            start = word[0]
            if start in root.dict:
                root = root.dict[start]
            else:
                root.dict[start] = Trie()
                root = root.dict[start]
            word = word[1:]
        root.dict["end"] = Trie()
        return

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self
        while len(word) != 0:
            start = word[0]
            if start in root.dict:
                root = root.dict[start]
            else:
                return False
            word = word[1:]
        if "end" in root.dict:
            return True
        else:
            return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self
        while len(prefix) != 0:
            start = prefix[0]
            if start in root.dict:
                root = root.dict[start]
            else:
                return False
            prefix = prefix[1:]
        return True

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))