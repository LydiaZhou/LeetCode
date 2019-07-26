import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        reverseOrder = {i: set() for i in range(numCourses)}
        order = {i: set() for i in range(numCourses)}
        for i, j in prerequisites:
            reverseOrder[i].add(j)
            order[j].add(i)
        stack = []
        for i in range(numCourses):
            if len(reverseOrder[i]) == 0:
                stack.append(i)

        #BFS
        path = []
        while len(stack) != 0:
            current = stack.pop(0)
            path.append(current)
            # find the next stop, double check, if yes, remove current from the reverseOrder(prereq)
            for next in order[current]:
                reverseOrder[next].remove(current)
                if len(reverseOrder[next]) == 0:
                    stack.append(next)
        return path if len(path) == numCourses else []

if __name__ == '__main__':
    a = Solution()
    print(a.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))