n, m = map(int, input().split()) # 4 4

data = [0] * m # [0, 0, 0, 0]
used = [0] * n # [0, 0, 0, 0]

def backtrack(index):
    if index == m:
        for i in range(m):
            print(data[i], end=" ")
        print()
        return

    for i in range(1, n + 1): # 1 2 3 4
        if not used[i - 1]:
            data[index] = i # 1
            used[i - 1] = 1
            backtrack(index + 1)
            used[i - 1] = 0

backtrack(0)

'''
N, M = map(int, input().split())

data = [0] * (N + 1)
isUsed = [0] * (N + 1)

def BackTracking(index):
    if index == M:
        for i in range(M):
            print(data[i], end=' ')
        print()
        return

    for i in range(1, N + 1):
        if not isUsed[i]:
            data[index] = i
            isUsed[i] = 1
            BackTracking(index + 1)
            isUsed[i] = 0

BackTracking(0)
'''