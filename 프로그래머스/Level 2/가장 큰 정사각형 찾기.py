''' 
# 1.실패
def solution1(board):
	def boardCheck(x, y, h_end, w_end):
		for i in range(x, h_end + 1):
			for j in range(y, w_end + 1):
				if board[i][j] != 1:
					return False
		return True
		
	def check(num, board):
		for x in range(len(board)):
			for y in range(len(board[0])):		
				# check start to last idx
				w_end = num + y - 1
				h_end = num + x - 1
				
				# check max_x, max_y
				if w_end >= len(board[0]) or h_end >= len(board):
					return False
					
				if board[x][y] == 0 or board[h_end][w_end] == 0:
					continue
				
				# check it can be correct right
				if boardCheck(x, y, h_end, w_end):
					return True
	
	num = 1
	while num <= len(board[0]):
		if not check(num, board):
			num -= 1
			break
		num += 1
	
	return num ** 2

# 2.실패
def solution2(board):
	def isRect(x, y, x_end, y_end):
		for i in range(x, x_end + 1):
				for j in range(y, y_end + 1):
					if board[i][j] == 0: return False
		return True
			
	def check(x, y, board):
		num = 1
		prev_x, prev_y = x, y
		while True:
			x_end = num + x - 1
			y_end = num + y - 1
			
			if y_end >= len(board[0]) or x_end >= len(board): return num - 1
			if isRect(prev_x, prev_y, x_end, y_end):
				prev_x, prev_y = x_end, y_end
				num += 1
			else:
				return num - 1
		
	answer = 1
	for x in range(len(board)):
		for y in range(len(board[0])):
			if board[x][y] == 0: continue
			
			res = check(x, y, board)
			if res > answer:
				answer = res
	return answer ** 2
'''

# 3.성공 (DP)


def solution(board):
    dp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    maximum = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                continue
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
            if dp[i][j] > maximum:
                maximum = dp[i][j]
    return maximum ** 2


# board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
# board = [[0,0,1,1],[1,1,1,1]]
# board = [[0, 0, 0, 0],[1, 0, 0, 0],[1, 0, 0, 0],[0, 0, 0, 0]]
# board = [[0, 1, 1, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
# board = [[1,0],[0,0]]
print(solution(board))
