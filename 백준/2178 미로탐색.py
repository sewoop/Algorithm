def solution():
    n, m = map(int, input().split())

    maze = [list(input()) for _ in range(n)]
    visit = [[0] * m for _ in range(n)]

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS
    queue = [(0, 0)]
    visit[0][0] = 1

    while queue:
        x, y = queue.pop(0)

        if x == n - 1 and y == m - 1:
            print(visit[x][y])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '1' and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))


solution()
