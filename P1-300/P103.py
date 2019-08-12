# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        count = 0
        layer = 1
        stack = [root]
        result = []
        curLine = []
        while stack:
            cur = stack.pop(0)
            curLine.append(cur.val)
            count += 1
            if pow(2, layer) - 1 == count:
                if layer%2 == 1:
                    result.append(curLine)
                else:
                    curLine.reverse()
                    result.append(curLine)
                curLine = []
                layer += 1
            if cur.right:
                stack.append(cur.left)
            if cur.left:
                stack.append(cur.right)
        if layer % 2 == 1:
            result.append(curLine)
        else:
            curLine.reverse()
            result.append(curLine)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(3)
    root.right.right = TreeNode(5)
    root.right.left = TreeNode(4)
    obj = Solution()
    print(obj.zigzagLevelOrder(root))