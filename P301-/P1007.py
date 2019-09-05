class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtyxpe: int
        """
        flipCount = 0
        flipCountB = 0
        target = set([A[0], B[0]])
        # twoPos = [A[0], B[0]]
        for i in range(1, len(A)):
            target &= set([A[i], B[i]])
        if not target:
            return -1
        val = target.pop()
        for i in range(len(A)):
            if A[i] != val:
                flipCount += 1
            if B[i] != val:
                flipCountB += 1
        return min(flipCountB, flipCount)


if __name__ == '__main__':
    obj = Solution()
    print(obj.minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))
