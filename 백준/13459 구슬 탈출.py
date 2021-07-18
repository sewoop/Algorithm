import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# 4차원 배열
visit = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 시계방향
queue = deque()

# 공의 위치 초기화
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] in "#.O": continue
        if board[i][j] == "R": rx, ry = i, j
        elif board[i][j] == "B": bx, by = i, j

queue.append((rx, ry, bx, by, 0))
visit[rx][ry][bx][by] = True

def move(x, y, dx, dy, count):
    while board[x + dx][y + dy] != "#" and board[x][y] != "O":
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    while queue:
        _rx, _ry, _bx, _by, cnt = queue.popleft()

        if cnt >= 10: break

        for i in range(4):
            nrx, nry, rc = move(_rx, _ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(_bx, _by, dx[i], dy[i], 0)

            if board[nbx][nby] == "O": continue
            if board[nrx][nry] == "O": return 1

            if nrx == nbx and nry == nby:
                if rc > bc: nrx, nry = nrx - dx[i], nry - dy[i]
                else: nbx, nby = nbx - dx[i], nby - dy[i]
            
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, cnt + 1))
    return 0

print(bfs())
