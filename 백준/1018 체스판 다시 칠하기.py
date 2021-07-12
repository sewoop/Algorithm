N, M = map(int, input().split())

board = [input() for i in range(N)]
answer = []

for i in range(N - 7):
    for j in range(M - 7):
        count_x = 0
        count_y = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'W':
                        count_x += 1  # [0, 0] = 'B'로 시작하는 경우
                    if board[x][y] != 'B':
                        count_y += 1  # [0, 0] = 'W'로 시작하는 경우
                else:
                    if board[x][y] != 'B':
                        count_x += 1  # [0, 0] = 'B'로 시작하는 경우
                    if board[x][y] != 'W':
                        count_y += 1  # [0, 0] = 'W'로 시작하는 경우

        answer.append(count_x)
        answer.append(count_y)

print(min(answer))
