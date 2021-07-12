# sol1
def solution():
    n, m = map(int, input().split())

    tile = [list(input()) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    # Top Bottom Left Right
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    count = 1
    for i in range(n):
        for j in range(m):
            # if "-"
            if tile[i][j] == "-" and visited[i][j] == 0:

                # BFS
                queue = [(i, j)]
                visited[i][j] = count

                while queue:
                    x, y = queue.pop(0)

                    # Only LR
                    for k in range(2, 4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < m and tile[nx][ny] == "-" and visited[nx][ny] == 0:
                            visited[nx][ny] = count
                            queue.append((nx, ny))
                count += 1

            # if "|"
            elif tile[i][j] == "|" and visited[i][j] == 0:

                # BFS
                queue = [(i, j)]
                visited[i][j] = count

                while queue:
                    x, y = queue.pop(0)

                    # Only TB
                    for k in range(2):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < m and tile[nx][ny] == "|" and visited[nx][ny] == 0:
                            visited[nx][ny] = count
                            queue.append((nx, ny))

                count += 1

    print(count - 1)


solution()

# sol2


def solution():
    n, m = map(int, input().split())

    tile = [list(input()) for _ in range(n)]
    visit = [[0] * m for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(m):
            if not visit[i][j]:
                count += 1

                if tile[i][j] == "-":
                    k = j
                    while k < m and tile[i][k] == "-":
                        visit[i][k] = 1
                        k += 1
                else:
                    k = i
                    while k < n and tile[k][j] == "|":
                        visit[k][j] = 1
                        k += 1
    print(count)


solution()
