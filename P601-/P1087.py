class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        words = []
        beginning = ""
        for i in range(len(S)):
            if S[i] == "{":
                endIndex = S[i + 1:].index("}")
                options = sorted(S[i + 1: i + 1 + endIndex].split(","))
                tails = self.expand(S[i + 1 + endIndex + 1:])
                for i in range(len(options)):
                    for j in range(len(tails)):
                        words.append(beginning + options[i] + tails[j])
                return words
            else:
                beginning += S[i]
        return [beginning]

if __name__ == '__main__':
    obj = Solution()
    print(obj.expand("{a,b}c{d,e}f"))
    print(obj.expand("{a,b}{z,x,y}"))
