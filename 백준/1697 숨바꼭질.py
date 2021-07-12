from collections import deque

MAX = int(10 ** 5)
n, k = map(int, input().split())
dist = [0] * (MAX + 1)


def bfs():
    queue = deque([n])

    while queue:
        x = queue.popleft()

        if x == k:
            return dist[x]

        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)


print(bfs())
