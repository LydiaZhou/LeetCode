class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [[1, ""]]
        bracketCount = 0
        digit = ""
        for char in s:
            if char.isdigit():
                digit += char
            elif char == '[':
                stack.append([int(digit), ""])
                digit = ""
            elif char == ']':
                num, str = stack.pop()
                stack[-1][1] += num*str
            else:
                stack[-1][1] += char
        return stack[0][1]


if __name__ == '__main__':
    obj = Solution()
    print(obj.decodeString("3[a]2[bc]"))