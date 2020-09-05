from collections import deque
from typing import List

def find_start(N: int) -> List:
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def maze_tracking(x: int, y: int):
    global isPath, count, queue

    # 우 하 좌 상 (수정)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    if maze[x][y] == 3:
        isPath = True
        count = len(queue)-1
        return

    visited.append((x, y))

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if (next_x, next_y) not in visited and (0<=next_x<N and 0<=next_y<N) and maze[next_x][next_y] != 1:
            queue.append((next_x, next_y))
            maze_tracking(next_x, next_y)

    queue.pop()  # 수정


Ts = int(input())
# Ts = 1

for T in range(1, Ts + 1):
    N = int(input())
    # N = 5

    maze = [[int(i) for i in list(input())] for _ in range(N)]
    # maze = [
    #     [1, 3, 1, 0, 1],
    #     [1, 0, 1, 0, 1],
    #     [1, 0, 1, 0, 1],
    #     [1, 0, 1, 0, 1],
    #     [1, 0, 0, 2, 1]
    # ]
    # print(maze)

    # 시작점 찾기
    start_x, start_y = find_start(N)
    visited = []

    queue = deque()
    isPath = False
    count = 0

    # 찾기
    try:
        maze_tracking(start_x, start_y)
    except IndexError:
        pass

    print(f'#{T} {count if isPath else 0}')
