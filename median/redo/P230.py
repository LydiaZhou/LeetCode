# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def helper(self, root):
        if not root:
            return
        if root.left:
            self.helper(root.left)
        self.count -= 1
        if self.count == 0:
            self.pos = root.val
            return
        if root.right:
            self.helper(root.right)


    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = k
        self.pos = None
        self.helper(root)
        return self.pos




if __name__ == '__main__':
    a = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(a.kthSmallest(root, 3))