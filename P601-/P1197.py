class Solution(object):
    def minKnightMoves(self, x, y):
        x = abs(x)
        y = abs(y)
        dpList = [[-1]*(max(min(x, y) + 1, 3)) for i in range(max(x,y)+1)]
        dpList[0][0] = 0

        def dp(x, y):
            if x < y:
                swapVal = x
                x = y
                y = swapVal
            if dpList[x][y] != -1:
                return dpList[x][y]
            if x + y == 2:
                dpList[x][y] = 2
                return 2
            val = min(dp(abs(x-2), abs(y-1)), dp(abs(x-1), abs(y-2))) + 1
            dpList[x][y] = val
            return val

        return dp(x, y)

if __name__ == '__main__':
    obj = Solution()
    print(obj.minKnightMoves(300, 0))
    # print(obj.minKnightMoves(16, 2))

# # BFS solution
# class Solution(object):
#     def minKnightMoves(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         x = abs(x)
#         y = abs(y)
#         current = [0, 0, 0]
#         visited = set()
#         stack = [current]
#
#         # better why to do this, sort all the possible next steps and work towards the firection with maxMovement towards destination
#         while stack:
#             current = stack.pop(0)
#             visited.add((current[0], current[1]))
#             if current[:2] == [x, y]:
#                 return current[2]
#             if current[0] - current[1] > 4:
#                 list = [(2,1), (2, -1)]
#             elif current[1] - current[0] > 4:
#                 list = [(1,2), (-1, 2)]
#             else:
#                 list = [(1, 2), (-1, 2), (2,1), (2, -1)]
#             for (i, j) in list:
#                 if (abs(current[0] + i), abs(current[1] + j)) not in visited:
#                     stack.append([abs(current[0] + i), abs(current[1] + j), current[2]+1])