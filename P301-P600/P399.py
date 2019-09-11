class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # reading
        dicts = {}
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            if a in dicts:
                dicts[a].append((b, val))
            else:
                dicts[a] = [(b, val)]
            if b in dicts:
                dicts[b].append((a, 1/val))
            else:
                dicts[b] = [(a, 1/val)]

        # bfs searching
        returnVal = []
        for query in queries:
            start, end = query
            if start == end:
                if start not in dicts:
                    returnVal.append(-1.0)
                else:
                    returnVal.append(1.0)
            else:
                num = self.bfs(start, end, dicts, set())
                if num != 0:
                    returnVal.append(self.bfs(start, end, dicts, set()))
                else:
                    returnVal.append(-1.0)
        return returnVal


    def bfs(self, current, target, dict, visited):
        visited.add(current)
        if current == target:
            return 1
        if current in dict:
            for (next, distance) in dict[current]:
                if next not in visited:
                    newV = visited.copy()
                    num = self.bfs(next, target, dict, newV)*distance
                    if num != 0:
                        return num
        return 0

if __name__ == '__main__':
    obj = Solution()
    print(obj.calcEquation([["a","b"],["b","c"]],
[2.0,3.0],
[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))