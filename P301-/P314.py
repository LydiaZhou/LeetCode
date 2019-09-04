# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return []
        newDict = {}
        curPos = 0
        queue = [(root, curPos)]
        # dfs
        while queue:
            (root, curPos) = queue.pop(0)
            if curPos in newDict:
                newDict[curPos].append(root.val)
            else:
                newDict[curPos] = [root.val]
            if root.left:
                queue.append((root.left, curPos - 1))
            if root.right:
                queue.append((root.right, curPos + 1))
        return [newDict[i] for i in sorted(newDict)]

    # def verticalOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     return self.helper(root)[0]
    #
    # def helper(self, root):
    #     if not root:
    #         return ([], -1)
    #     (leftList, leftIndex) = self.helper(root.left)
    #     (rightList, rightIndex) = self.helper(root.right)
    #     rightStart = leftIndex + 1 - rightIndex + 1
    #     # conbime two lists
    #     if leftIndex != -1:
    #         newArray = leftList.copy()
    #         if leftIndex + 1 < len(newArray):
    #             newArray[leftIndex + 1].insert(0, root.val)
    #         else:
    #             newArray.append([root.val])
    #         for i in range(len(rightList)):
    #             if i + rightStart < len(newArray) and i + rightStart > 0:
    #                 newArray[i + rightStart] += rightList[i]
    #             else:
    #                 newArray.append(rightList[i])
    #     else:
    #         newArray = rightList.copy()
    #         if rightIndex - 1 < len(newArray) and rightIndex - 1 > 0:
    #             newArray[rightIndex - 1].insert(0, root.val)
    #         elif rightIndex - 1 < 0:
    #             newArray.insert(0, [root.val])
    #         else:
    #             newArray.append([root.val])
    #     return (newArray, leftIndex + 1)


if __name__ == '__main__':
    obj = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(8)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(7)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(0)
    root.left.right.right = TreeNode(2)
    root.right.left.left = TreeNode(5)
    print(obj.verticalOrder(root))

    root2 = TreeNode(1)
    root2.right = TreeNode(6)
    root2.right.left = TreeNode(5)
    root2.right.left.left = TreeNode(3)
    root2.right.left.left.left = TreeNode(2)
    root2.right.left.left.right = TreeNode(4)
    # print(obj.verticalOrder(root2))

