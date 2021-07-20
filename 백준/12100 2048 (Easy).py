import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().strip().split())) for _ in range(n)]
answer = 0

def move(direct):
    if direct == 0:
        for j in range(n):
            nx = 0
            for i in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[nx][j] == 0:
                        board[nx][j] = temp
                    elif board[nx][j] == temp:
                        board[nx][j] = temp * 2
                        nx += 1
                    else:
                        nx += 1
                        board[nx][j] = temp
        
    elif direct == 1:
        for j in range(n):
            nx = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[nx][j] == 0:
                        board[nx][j] = temp
                    elif board[nx][j] == temp:
                        board[nx][j] = temp * 2
                        nx -= 1
                    else:
                        nx -= 1
                        board[nx][j] = temp

    elif direct == 2:
        for j in range(n):
            ny = 0
            for i in range(1, n):
                if board[j][i]:
                    temp = board[j][i]
                    board[j][i] = 0
                    if board[j][ny] == 0:
                        board[j][ny] = temp
                    elif board[j][ny] == temp:
                        board[j][ny] = temp * 2
                        ny += 1
                    else:
                        ny += 1
                        board[j][ny] = temp

    else:
        for j in range(n):
            ny = n - 1
            for i in range(n - 2, -1, -1):
                if board[j][i]:
                    temp = board[j][i]
                    board[j][i] = 0
                    if board[j][ny] == 0:
                        board[j][ny] = temp
                    elif board[j][ny] == temp:
                        board[j][ny] = temp * 2
                        ny -= 1
                    else:
                        ny -= 1
                        board[j][ny] = temp

def solution(count):
    global board, answer

    if count == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return

    origin = [i[:] for i in board]

    for i in range(4):
        move(i)
        solution(count + 1)
        board = [i[:] for i in origin]

solution(0)
print(answer)
