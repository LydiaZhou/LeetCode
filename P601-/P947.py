import collections

class Solution(object):
    def removeStones2(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        islandCount = 0
        visited = set()
        tupleStones = [(i, j) for i, j in stones]
        nexts = {tupleStones[0]}
        while tupleStones:
            cur = nexts.pop()
            tupleStones.remove(cur)
            visited.add(cur)
            for i, stone in enumerate(tupleStones):
                if stone not in visited:
                    if stone[0] == cur[0] or stone[1] == cur[1]:
                        nexts.add(stone)
            if not nexts:
                islandCount += 1
                if tupleStones:
                    nexts.add(tupleStones[0])
        return len(stones) - islandCount

    # Better solution, storing the stones in grid(use two dicts to represent)
    def removeStones(self, stones):
        islandCount = 0
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        for stone in stones:
            rows[stone[0]].append(stone[1])
            cols[stone[1]].append(stone[0])
        tupleStones = {(i, j) for i, j in stones}

        def dfs(cur):
            tupleStones.discard(cur)
            for ele in rows[cur[0]]:
                if (cur[0], ele) in tupleStones:
                    dfs((cur[0], ele))
            for ele in cols[cur[1]]:
                if (ele, cur[1]) in tupleStones:
                    dfs((ele, cur[1]))

        for stone in stones:
            if (stone[0], stone[1]) in tupleStones:
                dfs((stone[0], stone[1]) )
                islandCount += 1
        return len(stones) - islandCount

if __name__ == '__main__':
    obj = Solution()
    print(obj.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))