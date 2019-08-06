# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        if right and left :
            return root
        else:
            return right or left


    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
    #     pIndex = None
    #     qIndex = None
    #     # Find index of two nodes first
    #     for index in range(len(root)):
    #         if root[index] == p:
    #             pIndex = index
    #         elif root[index] == q:
    #             qIndex = index
    #         if qIndex != None and pIndex != None:
    #             break
    #
    #     # Finding parent till the two index are the same
    #     while pIndex != qIndex:
    #         if pIndex > qIndex:
    #             pIndex = (pIndex - 1)//2
    #         else:
    #             qIndex = (qIndex - 1) // 2
    #
    #     return pIndex