class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        order = []
        for char in s:
            if char == '(':
                order.append(")")
            elif char == '{':
                order.append("}")
            elif char == '[':
                order.append("]")
            else:
                if len(order) == 0:
                    return False
                if char == order[-1]:
                    order.pop(-1)
                else:
                    return False
        return len(order) == 0

if __name__ == '__main__':
    obj = Solution()
    print(obj.isValid("([)]"))