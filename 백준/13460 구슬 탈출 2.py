import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visit = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
queue = deque()

rx, ry, bx, by = 0, 0, 0, 0

# board 초기화
for i in range(n):
    for j in range(m):
        if board[i][j] in "#.O": continue
        if board[i][j] == "R": rx, ry = i, j
        elif board[i][j] == "B": bx, by = i, j

queue.append((rx, ry, bx, by, 1))
visit[rx][ry][bx][by] = 1

def move(x, y, dx, dy, dist):
    while board[x + dx][y + dy] != "#" and board[x][y] != "O":
        x += dx
        y += dy
        dist += 1
    return x, y, dist

def bfs():
    while queue:
        crx, cry, cbx, cby, count = queue.popleft()

        if count > 10: break

        for i in range(4):
            nrx, nry, rdist = move(crx, cry, dx[i], dy[i], 0)
            nbx, nby, bdist = move(cbx, cby, dx[i], dy[i], 0)

            if board[nbx][nby] == "O": continue
            if board[nrx][nry] == "O": return count

            if (nrx, nry) == (nbx, nby):
                if rdist > bdist:
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]

            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, count + 1))
    return -1

print(bfs())
            