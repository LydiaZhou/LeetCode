# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = 0
        # depthtotal = self.getDepth(root)
        while root:
            left = self.getDepth(root.left)
            right = self.getDepth(root.right)
            if left > right:
                root = root.left
                total += pow(2, right)
            else:
                root = root.right
                total += pow(2, left)
        return total

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)

if __name__ == '__main__':
    obj = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(obj.countNodes(root))