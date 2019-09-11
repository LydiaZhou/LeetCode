# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(plants, capacity):
    # write your code in Python 3.6
    steps = 0
    waterLevel = capacity
    for i, plant in enumerate(plants):
        if plant > waterLevel:
            waterLevel = capacity
            steps += 2*i
        waterLevel -= plant
        steps += 1
    return steps


if __name__ == '__main__':
    print(solution([2, 4, 5, 1, 2], 6))
    print(solution([2], 6))