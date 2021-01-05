N, M = map(int, input().split())

# W = 1, B =0
pattern = [170, 85] * 4
board = []

for _ in range(N):
    board.append(input().replace('W', '1').replace('B', '0'))

def matchPatternWithCountNotMatch(pattern, board):
    global N, M

    count = 99999999

    for i in range(N - 8 + 1): # 0, 1, 2
        tempCount = 0
        for j in range(M - 8 + 1): # 0, 1, 2, 3, 4, 5
            for k in range(i, i + 8):
                temp = int(board[k][j: j + 8], 2)
                temp = bin(pattern[k - i] ^ temp)[2:]
                
                for x in temp:
                    if x == '1':
                        tempCount += 1
            if tempCount < count:
                count = tempCount
    print(count)
    return count

matchPatternWithCountNotMatch(pattern, board)