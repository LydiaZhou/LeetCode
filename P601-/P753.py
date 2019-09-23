class Solution(object):
    def crackSafe(self, n, k):
        if n == 1:
            return ''.join([str(i) for i in range(k)])
        result = "0"*n
        visited = set()
        visited.add(result)
        for x in range(k**n):
            prefix = result[len(result) - n + 1:]
            for i in range(k-1, -1, -1):
                # print(prefix + str(i) not in visited)
                if (prefix + str(i)) not in visited:
                    result += str(i)
                    visited.add(prefix + str(i))
                    break
        return result



if __name__ == '__main__':
    obj = Solution()
    print(obj.crackSafe(3, 2))
    print(obj.crackSafe(1, 2))
    print(obj.crackSafe(2, 2))



# class Solution(object):
#     # Time limit exceed
#     def __init__(self):
#         global result
#
#     def crackSafe(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: str
#         """
#         # write out every number with length n-1
#         nList = []
#
#         def generateList(prefix, n):
#             if n == 0:
#                 nList.append(prefix)
#                 return
#             for i in range(k):
#                 generateList(prefix + str(i), n-1)
#
#         generateList("", n)
#         print(nList)
#
#         if n == 1:
#             return ''.join(nList)
#
#         self.result = ''.join(nList)
#         # dfs to find path, after finding a path, end
#         def dfs(prefix, current, visited):
#             visited.add(current)
#             current = nList[current]
#             for i, num in enumerate(nList):
#                 if i not in visited:
#                     for j in range(1, n):
#                         if current[j:] == nList[i][:n-j]:
#                             visitedCopy = visited.copy()
#                             dfs(prefix + nList[i][n-j:], i, visitedCopy)
#             if len(visited) == len(nList) and len(prefix) < len(self.result):
#                 self.result = prefix
#             return
#
#         tmp = dfs(str(nList[0]), 0, set())
#         return self.result