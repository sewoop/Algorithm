'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
'''
import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split()) # 노드 수, 간선 수
INF = int(1e9)

# 시작 노드
start = int(input())

# 그래프 초기화
graph = [[] for _ in range(n + 1)] # [[0번째는 사용하지 않음], [], [], [], [], [], []]
for _ in range(m):
    a, b, c = map(int, input().split()) # 출발 -> (비용, 도착)
    graph[a].append((c, b))

# 최단 거리 기록
distance = [INF] * (n + 1) # [0, 1, 2, 3, 4, 5, 6]

def dijkstra(start):
    heap = []
    # 시작 노드를 선택, 최단 거리를 0으로 초기화
    heapq.heappush(heap, (0, start)) # (비용, 도착노드)
    distance[start] = 0

    while heap:
        dist, node = heapq.heappop(heap) # (비용, 도착노드)

        if distance[node] < dist:
            continue

        # 인접노드를 갱신
        for nextNode in graph[node]: # (비용, 도착노드)

            # cost는 현재 노드까지의 비용과 다음 노드까지 비용을 합한 값
            cost = dist + nextNode[0]

            # 만약 위에서 합산한 비용이 이전에 계산한 다음 노드까지의 거리보다 작으면 갱신
            if cost < distance[nextNode[1]]:
                heapq.heappush(heap, (cost, nextNode[1]))
                distance[nextNode[1]] = cost # 최단 거리를 초기화

# 다익스트라 수행
dijkstra(start)

# 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print('무한')
    else:
        print(distance[i])

'''

## 복습
import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)

start = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b)) # (비용, 도착노드)

distance = [INF] * (n + 1)

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)

        if distance[node] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for nextNode in graph[node]:
            cost = dist + nextNode[0]

            if cost < distance[nextNode[1]]:
                heapq.heappush(heap, (cost, nextNode[1]))
                distance[nextNode[1]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('무야호')
    else:
        print(distance[i])
                