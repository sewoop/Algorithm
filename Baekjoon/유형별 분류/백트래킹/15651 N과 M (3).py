n, m = map(int, input().split())

data = [0] * m
used = [0] * (n + 1)

def backtrack(index):
    if index == m:
        for i in range(m):
            print(data[i], end=' ')
        print()
        return
    
    for i in range(1, n + 1):
        if not used[i]:
            data[index] = i
            for j in range(i):
                used[j] = 1
            backtrack(index + 1)
            for j in range(i):
                used[j] = 0

backtrack(0)


'''
N, M = map(int, input().split())

data = [0] * (N + 1)
isUsed = [0] * (N + 1)

def backTracking(index):
    if index == M:
        for i in range(M):
            print(data[i], end=' ')
        print()
        return

    for i in range(1, N + 1):
        data[index] = i

        isUsed[i] = 1
        backTracking(index + 1)
        isUsed[i] = 0

backTracking(0)
'''