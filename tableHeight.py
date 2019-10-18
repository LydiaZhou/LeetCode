def maxHeight2(tablePositions, tableHeights):
    if len(tableHeights) == 0 or len(tableHeights) != len(tablePositions):
        return 0
    tableTuple = sorted([(tablePositions[i], tableHeights[i]) for i in range(len(tablePositions))])
    prePos, preHeight = tableTuple[0]
    maxHeight = 0
    for i in range(1, len(tableTuple)):
        curPos, curHeight = tableTuple[i]
        smallHeight = min(curHeight, preHeight)
        if curPos == prePos + 1:
            continue
        posDiff = curPos - prePos - 1
        heightDiff = abs(curHeight - preHeight)
        if posDiff <= heightDiff:
            curMaxHeight = smallHeight + posDiff
        else:
            curMaxHeight = max(preHeight, curHeight) + (posDiff - heightDiff + 1)//2
        if curMaxHeight > maxHeight:
            maxHeight = curMaxHeight
        prePos, preHeight = curPos, curHeight
    return maxHeight

def maxHeight(tablePositions, tableHeights):
    result = 0

    def calculate(height1, height2, dis):
        if dis == 0:
            return 0
        if height1 == height2:
            return height1 + (dis + 1)//2
        heightDiff = height2 - height1
        if heightDiff < dis:
            dis -= heightDiff
            height1 += heightDiff
            return height1 + (dis + 1)//2
        return height1 + dis
    for i in range(1, len(tablePositions)):
        val = calculate(min(tableHeights[i-1], tableHeights[i]), max(tableHeights[i-1],
                                                    tableHeights[i]), tablePositions[i] - tablePositions[i - 1] -1)
        result = max(result, val)
    return result



if __name__ == '__main__':
    print(maxHeight([5, 10], [5, 1])) # 5
    print(maxHeight([5, 10], [100, 1]))  # 5
    print(maxHeight([5, 10], [2, 2]))  # 4

    print(maxHeight([13, 10], [2, 2]))  # 3
    print(maxHeight([13, 10], [10, 2]))  # 4
    print(maxHeight([7, 10], [2, 2]))  # 3

