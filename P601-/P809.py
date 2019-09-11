class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        def check(word):
            pre = None
            count = 0
            wordIndex = 0
            for s in S:
                if not pre:
                    pre = s
                    count = 1
                    if word[wordIndex] != s:
                        return False
                    wordIndex += 1
                elif s == pre:
                    count += 1
                else:
                    # deal with count
                    oriCount = count
                    while wordIndex < len(word):
                        if word[wordIndex] == pre:
                            count -= 1
                        else:
                            break
                        wordIndex += 1
                    if oriCount < 3:
                        if count != 1:
                            return False
                    else:
                        if count < 1:
                            return False
                    # check current
                    if wordIndex >= len(word) or s != word[wordIndex]:
                        return False
                    else:
                        pre = s
                        count = 1
                        wordIndex += 1
            # deal with count
            oriCount = count
            while wordIndex < len(word):
                if word[wordIndex] == pre:
                    count -= 1
                else:
                    break
                wordIndex += 1
            if oriCount < 3:
                if count != 1:
                    return False
            else:
                if count < 1:
                    return False
            return True
        count = 0
        for word in words:
            if check(word):
                count += 1
        return count


if __name__ == '__main__':
    obj = Solution()
    # print(obj.expressiveWords("abcd", ["abc"]))
    print(obj.expressiveWords("zzzzzyyyyy", ["zzyy", "zy", "zyy"]))
    # print(obj.expressiveWords("heeellooo", ["hello", "hi", "helo"]))