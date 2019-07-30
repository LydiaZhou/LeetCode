# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, ptr):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if ptr == None:
            return self.inorder
        self.inorderTraversal(ptr.left)
        self.inorder.append(ptr.val)
        self.inorderTraversal(ptr.right)
        return self.inorder

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    obj = Solution()
    print(obj.inorderTraversal(root))
