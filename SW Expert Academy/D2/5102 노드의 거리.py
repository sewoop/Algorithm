import pprint

def bfs():
    queue = [[start, 0]]
    visited = [start]

    while queue:
        v, cnt = queue.pop(0)
        if v == end:
            return cnt
        
        for i in range(1, V+1):
            if i not in visited and graph[v][i] == 1:
                queue.append([i, cnt+1])
                visited.append(i)

    return 0

ts = int(input())
# ts = 1

for t in range(1, ts + 1):
    V, E = map(int, input().split())
    # V, E = 6, 5

    # 초기화
    graph = [[0]*(V+1) for _ in range(V+1)]
    # pprint.pprint(graph)

    # 세팅
    for i in range(E):
        n1, n2 = map(int, input().split())
        graph[n1][n2] = graph[n2][n1] = 1
    # pprint.pprint(graph)

    start, end = map(int, input().split())

    print(f'#{t} {bfs()}')