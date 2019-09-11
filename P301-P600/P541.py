class Solution:
    def reverseStr2(self, s: str, k: int) -> str:
        kCount = k
        resultStr = ""
        waitForReverse = ""
        for i in range(len(s)):
            kCount -= 1
            waitForReverse += s[i]
            if kCount == 0:
                resultStr += self.reverse(waitForReverse)
                waitForReverse = ""
            if kCount == -k:
                kCount = k
                resultStr += waitForReverse
                waitForReverse = ""
        # remaining part not reach length k
        if kCount >= 0:
            resultStr += self.reverse(waitForReverse)
        else:
            resultStr += waitForReverse
        return resultStr

    def reverse(self, s: str) -> str:
        returnVal = ""
        for i in range(len(s)-1, -1, -1):
            returnVal += s[i]
        return returnVal

    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)


if __name__ == '__main__':
    obj = Solution()
    print(obj.reverseStr("abcdefg", 2))
