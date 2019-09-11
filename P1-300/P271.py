class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for string in strs:
            result += "{" + str(len(string)) + "}" + string
        return result

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        i = 1
        strs = []
        while i < len(s):
            endBracket = s.find("}", i)
            lengthCount = int(s[i:endBracket])
            strs.append(s[endBracket + 1: endBracket + 1 + lengthCount])
            i = endBracket + 2 + lengthCount
        return strs

if __name__ == '__main__':
    strs = ["abcabc", "ddddd", "33333333333"]
    codec = Codec()
    print(codec.decode(codec.encode(strs)))