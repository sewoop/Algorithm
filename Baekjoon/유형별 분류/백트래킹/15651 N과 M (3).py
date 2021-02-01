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