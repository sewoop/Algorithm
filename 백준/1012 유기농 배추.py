from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j):
    global visit

    queue = deque()
    queue.append((i, j))

    visit[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and mat[nx][ny]:
                visit[nx][ny] = 1
                queue.append((nx, ny))


t = int(input())

for _ in range(t):
    m, n, c = map(int, input().split())

    # Set matrix
    mat = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]

    # TBLR
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for _ in range(c):
        x, y = map(int, input().split())
        mat[y][x] = 1

    # Find BFS
    count = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] and not visit[i][j]:
                count += 1
                bfs(i, j)

    print(count)
