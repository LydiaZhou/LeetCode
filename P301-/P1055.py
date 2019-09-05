class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        curIndex = 0
        output = 1
        for char in target:
            if char not in source:
                return -1
            else:
                # continue using the former source
                if char not in source[curIndex:]:
                    output += 1
                    curIndex = 0
                curIndex += source[curIndex:].find(char) + 1
        return output

if __name__ == '__main__':
    obj = Solution()
    print(obj.shortestWay("abc", "abcbc"))
    print(obj.shortestWay("abc", "acdbc"))
    print(obj.shortestWay("xyz", "xzyxz"))
