'''
N = int(input()) # N = 4

count = 0

row = [0 for _ in range(N)] # [0, 1, 2, 3]
left = [0 for _ in range(2 * N - 1)] # [0, 1, 2, 3, 4, 5, 6]
right = [0 for _ in range(2 * N - 1)]

def nQueen(index):
    global count

    if index == N:
        count += 1
        return 
    
    for col in range(N):
        if row[col] + left[index + col] + right[N - 1 + index - col] == 0:
            row[col] = left[index + col] = right[N - 1 + index - col] = 1
            nQueen(index + 1)
            row[col] = left[index + col] = right[N - 1 + index - col] = 0

nQueen(0)
print(count)

'''


n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]
count = 0

def nQueen(x, y):
    # 같은 열에 퀸이 있는 지를 확인
    for i in range(x):
        if board[i][y] == 1:
            return 0

    # 좌 상단 대각선에 퀸이 있는 지 확인
    leftRow = x
    leftCol = y
    while leftRow >= 0 and leftCol >= 0:
        if board[leftRow][leftCol] == 1:
            return 0
        leftRow -= 1
        leftCol -= 1

    # 우 상단 대각선에 퀸이 있는 지 확인
    rightRow = x
    rightCol = y
    while rightRow >= 0 and rightCol < n:
        if board[rightRow][rightCol] == 1:
            return 0 
        rightRow -= 1
        rightCol += 1

    return 1

def nQueenDFS(x):
    if x == n:
        global count
        count += 1
        return
    
    for i in range(n):
        # 끝까지 도달하면
        if nQueen(x, i) == 1:
            board[x][i] = 1
            nQueenDFS(x + 1)
            board[x][i] = 0

nQueenDFS(0) # 0줄부터 시작
print(count)



