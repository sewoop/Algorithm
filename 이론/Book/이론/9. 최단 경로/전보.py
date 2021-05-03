import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

# 그래프 초기화 (단방향)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

def dijkstra(start):
    distance = [INF] * (n + 1) # 최단 거리

    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)

        if distance[node] < dist:
            continue
            
        for nextNode in graph[node]:
            cost = dist + nextNode[0]

            if cost < distance[nextNode[1]]:
                heapq.heappush(heap, (cost, nextNode[1]))
                distance[nextNode[1]] = cost
    return distance

dist = dijkstra(start)

result = []
for d in dist:
    if d == INF or d == 0:
        continue
    result.append(d)

print(len(result), max(result))

'''
3 2 1
1 2 4
1 3 2
'''