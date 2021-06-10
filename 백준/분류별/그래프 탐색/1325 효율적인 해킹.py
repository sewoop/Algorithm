import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, network, num):
	visit, cnt = [0] * (n + 1), 0
	
	queue = deque()
	queue.append(num)
	
	visit[num] = 1
	while	queue:
		node = queue.popleft()
		cnt += 1
		
		for nx in network[node]:
			if not visit[nx]:
				visit[nx] = 1
				queue.append(nx)
				
	return cnt
	
def solution():
	n, m = map(int, input().split())
	
	# Set graph
	network = [[] for _ in range(n + 1)]
	
	for _ in range(m):
		a, b = map(int, input().split())
		network[b].append(a)
	
	# Find
	max_value = 0
	result = []
	for i in range(1, n + 1):
		if network[i]:
			connect = bfs(n, network, i)
			
			if connect >= max_value:
				if connect > max_value:
					result = []
				max_value = connect
				result.append(i)
				
	print(*result)
				
solution()
