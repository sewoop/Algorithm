import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

data = [0] * m
used = [0] * (n + 1)


def backtrack(index):
    if index == m:
        for i in range(m):
            print(data[i], end=' ')
        print()
        return

    for i in range(1, n + 1):
        data[index] = numbers[i - 1]
        used[i] = 1
        backtrack(index + 1)
        used[i] = 0


backtrack(0)
