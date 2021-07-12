N, M = map(int, input().split())

data = [0] * M  # [0, 0, 0] (M == 3)
isUsed = [False] * (N + 1)  # [0, 1, 2, 3, 4] (N == 4)


def backTracking(index):
    if index == M:
        for i in range(M):
            print(data[i], end=' ')
        print()
        return

    for i in range(1, N + 1):
        if index != 0 and i < data[index - 1]:
            continue

        data[index] = i

        isUsed[i] = True
        backTracking(index + 1)
        isUsed[i] = False


backTracking(0)
