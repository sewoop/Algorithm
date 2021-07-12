'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# self 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 노드 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=' ')   
    print()
'''

## 복습
# > Floyd Warshall is a kind of Dynamic Programming.

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# self initialize
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# node initialize
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# Floyd Warshall
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # i -> j is min(i -> j cost, i -> k -> j cost)

# Print
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=' ')
    print()