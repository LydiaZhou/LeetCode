class Solution(object):
    def totalFruit(self, trees):
        """
        :type tree: List[int]
        :rtype: int
        """
        brackets = {}
        maxFruit = -1
        pre = None
        for i, tree in enumerate(trees):
            if tree in brackets:
                brackets[tree][1] = i
            elif len(brackets) == 1 or len(brackets) == 0:
                brackets[tree] = [i, i]
            else:
                # find the fruit need to be replaced
                minEnd = float('inf')
                minStart = float('inf')
                minKey = None
                for key, val in brackets.items():
                    if val[1] < minEnd:
                        minEnd = val[1]
                        minKey = key
                    if val[0] < minStart:
                        minStart = val[0]
                # update the maxFruit
                maxFruit = max(maxFruit, i - minStart)
                # update the brackets
                brackets[pre][0] = brackets[minKey][1] + 1
                brackets.pop(minKey)
                brackets[tree] = [i, i]
            pre = tree
        # find the fruit need to be replaced
        minVal = float('inf')
        minKey = None
        for key, val in brackets.items():
            if val[0] < minVal:
                minVal = val[0]
        # update the maxFruit
        maxFruit = max(maxFruit, len(trees) - minVal)
        return maxFruit

if __name__ == '__main__':
    obj = Solution()
    print(obj.totalFruit([1,1,6,5,6,6,1,1,1,1]))
    # print(obj.totalFruit([1, 2, 1, 3, 3, 3, 3, 1]))
    # print(obj.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
