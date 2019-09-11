class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        # calculate the distance in between every pair
        allDis = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                allDis.append((self.disCal(worker, bike), i, j))

        # get result from the distance set
        resultList = [-1] * len(workers)
        takenBike = set()
        allDis.sort()
        for dis, i, j in allDis:
            if resultList[i] == -1 and j not in takenBike:
                takenBike.add(j)
                resultList[i] = j
        return resultList

    def disCal(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    obj = Solution()
    print(obj.assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]))

    print(obj.assignBikes([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]], \
    [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999], [5, 999], [6, 999], [7, 999], [8, 999]]))
