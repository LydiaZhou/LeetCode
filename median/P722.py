class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        paragraphComment = False
        lineComment = False
        result = ""
        char = 0
        source = "\n".join(source)
        # endWell = False
        while char < len(source) - 1:
            if paragraphComment:
                if source[char:char+2] == "*/":
                    char += 1
                    paragraphComment = False
            elif lineComment:
                if source[char] == "\n":
                    lineComment = False
            else:
                if source[char:char+2] == "/*":
                    char += 1
                    paragraphComment = True
                elif source[char:char+2] == "//":
                    result += "\n"
                    char += 1
                    lineComment = True
                else:
                    result += source[char]
            char += 1
        if not lineComment and not paragraphComment and source[-2:] != "*/":
            result += source[-1]
        return list(filter(None, result.split("\n")))

if __name__ == '__main__':
    obj = Solution()
    # print(obj.removeComments(["main() { ", "  int a = 1; /* Its comments here ", "", "  ", "  */ return 0;", "} "]))
    # print(obj.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
    print(obj.removeComments(["a//*b//*c","blank","d//*e/*/f"]))