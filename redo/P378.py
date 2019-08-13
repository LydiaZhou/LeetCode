from collections import OrderedDict

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        queue = OrderedDict()
        # queue.put((0,0), matrix[0][0])
        queue['a'] = 1
        queue['b'] = 2
        # while k != 0:
        print(queue)
        queue.popitem()
        print(queue)

if __name__ == '__main__':
    obj = Solution()
    print(obj.kthSmallest([], 0))