from bisect import bisect_left

class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # first line represent odd jump, second line represent even
        dpList = [[0] * len(A) for x in range(2)]
        dpList[0][-1] = 1
        dpList[1][-1] = 1
        sortedTail = [[A[-1], len(A) - 1]]

        def helper(startIndex):
            curVal = A[startIndex]
            insertIndex = bisect_left(sortedTail, [curVal, startIndex])
            # odd case
            if insertIndex == len(sortedTail):
                dpList[0][startIndex] = -1
            else:
                dpList[0][startIndex] = dpList[1][sortedTail[insertIndex][1]]
            # new even case
            if insertIndex < len(sortedTail) and sortedTail[insertIndex][0] == curVal:
                dpList[1][startIndex] = dpList[0][sortedTail[insertIndex][1]]
            elif insertIndex == 0:
                dpList[1][startIndex] = -1
            else:
                pre = sortedTail[insertIndex - 1][0]
                j = insertIndex - 2
                while j >= 0:
                    if sortedTail[j][0] != pre:
                        break
                    j -= 1
                dpList[1][startIndex] = dpList[0][sortedTail[j + 1][1]]
            sortedTail.insert(insertIndex, [curVal, startIndex])

        for i in range(len(A)-2, -1, -1):
            helper(i)
        return dpList[0].count(1)


if __name__ == '__main__':
    obj = Solution()
    print(obj.oddEvenJumps([5, 1, 3, 4, 2]))
    print(obj.oddEvenJumps([10, 13, 12, 14, 15]))
    print(obj.oddEvenJumps([2, 3, 1, 1, 4]))
    print(obj.oddEvenJumps([1, 2, 3, 2, 1, 4, 4, 5]))

    # HINT
    # a = [7, 1, 3, 4, 2, 1, 4]
    # next_higher = [0] * 7
    # stack = []
    # for a, i in sorted([a, i] for i, a in enumerate(a)):
    #     while stack and stack[-1] < i:
    #         next_higher[stack.pop()] = i
    #     stack.append(i)


