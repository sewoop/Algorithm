from collections import deque

# 미로의 최단 거리는 BFS를 사용하는 것이 좋다.


def solution():
    n, m = map(int, input().split())

    visit = [[0] * m for _ in range(n)]  # 방문여부 확인

    # 미로 정보 입력
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input())))

    # 이동 방향 (상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    x, y = 0, 0
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 상하좌우 위치 탐색
            next_x, next_y = x + dx[i], y + dy[i]  # 다음 좌표

            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:  # 다음 좌표가 벽을 넘어가면 다른 방향 탐색 진행
                continue

            if maze[next_x][next_y] == 0:  # 괴물이 존재하면 다른 방향 탐색
                continue

            if maze[next_x][next_y] == 1:
                maze[next_x][next_y] = maze[x][y] + 1  # BFS
                queue.append((next_x, next_y))

    return maze[n - 1][m - 1]


print(solution())

'''
5 6
101010
111111
000001
111111
111111
'''
