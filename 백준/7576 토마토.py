import sys
from collections import deque
input = sys.stdin.readline


def bfs(box):
    # TBLR
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    day = -1

    while ripe:
        day += 1

        for _ in range(len(ripe)):
            x, y = ripe.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if (0 <= nx < n) and (0 <= ny < m) and (box[nx][ny] == 0):
                    box[nx][ny] = box[x][y] + 1
                    ripe.append([nx, ny])

    for b in box:
        if 0 in b:
            return -1
    return day


m, n = map(int, input().split())
box, ripe = [], deque()

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(m):
        if row[j] == 1:
            ripe.append([i, j])

    box.append(row)

print(bfs(box))
