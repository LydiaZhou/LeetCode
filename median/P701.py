# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST2(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        tmp = root
        while tmp:
            if val > tmp.val:
                if tmp.right:
                    tmp = tmp.right
                else:
                    tmp.right = TreeNode(val)
                    break
            else:
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left = TreeNode(val)
                    break
        return root


if __name__ == '__main__':
    obj = Solution()

