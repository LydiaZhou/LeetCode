import time

def iteration(arr):
    for i in range(500):
        a = arr[i]

def recursion(arr, i):
    if i >= 500:
        return
    a = arr[i]
    recursion(arr, i+1)

if __name__ == '__main__':
    arr = []
    for i in range(500):
        arr.append(i)
    t1 = time.time()
    iteration(arr)
    print(time.time() - t1)
    t1 = time.time()
    recursion(arr, 0)
    print(time.time() - t1)

