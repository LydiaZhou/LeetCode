# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        curIndex = inorder.index(val)
        root.left = self.buildTree(preorder, inorder[:curIndex])
        root.right = self.buildTree(preorder, inorder[curIndex+1:])
        return root

if __name__ == '__main__':
    obj = Solution()
    b = obj.buildTree([3,9,20,15,7], [9,3,15,20,7])
