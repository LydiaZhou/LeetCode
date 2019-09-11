class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtyxpe: int
        """
        target = set([A[0], B[0]])
        # twoPos = [A[0], B[0]]
        for i in range(1, len(A)):
            target &= set([A[i], B[i]])
            if not target:
                return -1
        val = target.pop()
        return min(len(A) - A.count(val), len(B)- B.count(val))


if __name__ == '__main__':
    obj = Solution()
    print(obj.minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))
