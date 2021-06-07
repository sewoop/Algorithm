def solution():
	n = int(input())
	
	apart = [list(input()) for _ in range(n)]
	visit = [[0] * n for _ in range(n)]
	
	# 상하좌우
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	
	group, dan = 1, []
	
	for i in range(n):
		for j in range(n):
			if apart[i][j] == '1' and visit[i][j] == 0:
				
				# group, count initialize
				visit[i][j], count = group, 1 
				
				# BFS
				queue = [(i, j)]
				
				while queue:
					x, y = queue.pop(0)
					
					for k in range(4):
						nx = x + dx[k]
						ny = y + dy[k]
						
						if 0 <= nx < n and 0 <= ny < n and apart[nx][ny] == '1' and visit[nx][ny] == 0:
							count += 1
							visit[nx][ny] = group
							queue.append((nx, ny))
				
				dan.append(count)
				group += 1
				
	# Output
	print(group - 1)
	for i in sorted(dan):
		print(i)
	
solution()
