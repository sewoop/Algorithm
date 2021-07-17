# 카카오 인턴쉽 2021 - 4번 문제 : 풀이 중

''' 정확성: 41/100
import heapq
from collections import defaultdict

INF = int(1e9)

def swap(n, path, now):
    for i in range(1, n + 1):
        path[now][i], path[i][now] = path[i][now], path[now][i]
    return path


def dijkstra(n, path, trap, distance, start, end, visit):
    heap = []
    
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    visit[start] = 1

    while True:
        dist, now = heapq.heappop(heap)

        if now == end: break

        if distance[now] < dist:
            continue

        if now in trap.keys():
            visit[now] = 0
            path = swap(n, path, now)

        for i in [nxt for nxt in range(1, n + 1) if path[now][nxt] != INF and not visit[nxt]]:
            cost = dist + path[now][i]

            visit[i] = 1
            distance[i] = cost
            heapq.heappush(heap, (cost, i))


def solution(n, start, end, roads, traps):
    path = [[INF] * (n + 1) for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    trap = dict(zip(traps, [False] * len(traps)))
    visit = [0] * (n + 1)
    
    # 경로 초기화
    for road in roads:
        a, b, cost = road
        path[a][b] = cost

    # 다익스트라 최단 경로
    dijkstra(n, path, trap, distance, start, end, visit)

    return distance[end]
'''

'''
# 인접 리스트로 해결해보기 (43.6/100)
from heapq import heappush, heappop
from collections import defaultdict

INF = int(1e9)

def solution(n, start, end, roads, traps):
    path = defaultdict(list)
    trap = dict(zip(traps, [False] * len(traps)))

    # 경로 초기화
    for road in roads:
        a, b, cost = road
        path[a].append((cost, b))

    # 다익스트라 경로 탐색
    heap = []
    heappush(heap, (0, start))

    while True:
        dist, now = heappop(heap)

        # print(now, end=" -> ")

        if now == end: 
            return dist # end 지점에 도착하면 종료

        if now in traps and not trap[now]:
            trap[now] = not trap[now]

            for i in path.keys():
                for j in path[i]:
                    if j[1] == now:
                        cost = dist + j[0]
                        heappush(heap, (cost, i))
        elif now in traps and trap[now]:
            trap[now] = not trap[now]
            for i in path[now]:
                cost = dist + i[0]
                heappush(heap, (cost, i[1]))
        else:
            for i in path[now]:
                cost = dist + i[0]
                heappush(heap, (cost, i[1]))
'''

'''
## 56.4 / 100.0
from heapq import heappop, heappush
from collections import defaultdict

INF = int(1e9)

def solution(n, start, end, roads, traps):
    paths = defaultdict(list)
    distance = [INF] * (n + 1)
    trap = defaultdict(bool)

    # 경로 초기화
    for road in roads:
        a, b, c = road
        paths[a].append([c, b, False])  # 순반향
        paths[b].append([c, a, True])  # 역방향

    # 다익스트라
    heap = []
    heappush(heap, (0, -start))
    distance[start] = 0

    while heap:
        dist, curr = heappop(heap)
        curr = -curr

        if curr == end: break
        
        # if distance[curr] < dist: continue

        if curr in traps:
            trap[curr] = not trap[curr]

        for path in paths[curr]:
            cost = dist + path[0]
    
            if path[2] == (trap[curr] ^ trap[path[1]]):
                if distance[path[1]] > cost:
                    distance[path[1]] = cost
                heappush(heap, (cost, -path[1]))

    return distance[end]
'''

## 정확성: 92.3/100 (3,5,6번: 실패)
from heapq import heappop, heappush

INF = int(1e9)

def trap(n, paths, curr):
    for i in range(1, n + 1):
        paths[curr][i], paths[i][curr] = paths[i][curr], paths[curr][i]
    return paths

def solution(n, start, end, roads, traps):
    paths = [[INF] * (n + 1) for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    # 경로 초기화
    for road in roads:
        a, b, c = road
        if paths[a][b] > c:
            paths[a][b] = c
    
    # 다익스트라
    heap = []
    heappush(heap, (0, -start))
    distance[start] = 0

    status = False
    while heap:
        dist, curr = heappop(heap)
        curr = -curr
        
        if curr == end: break

        if distance[curr] < dist: continue

        if curr in traps:
            paths = trap(n, paths, curr)
            status = True
        else:
            status = False

        for j in [i for i in range(1, n + 1) if paths[curr][i] != INF]:
            cost = dist + paths[curr][j]
            
            if status:
                distance[j] = cost
                heappush(heap, (cost, -j))
            else:
                if distance[j] > cost:
                    distance[j] = cost
                    heappush(heap, (cost, -j))

    return distance[end]

n, start, end, roads, traps = 3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]
# n, start, end, roads, traps = 4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]
# n, start, end, roads, traps = 4, 1, 4, [[1, 2, 2], [2, 3, 2], [1, 3, 1], [3, 4, 3]], [2, 3]
# n, start, end, roads, traps = 2, 1, 2, [[1, 2, 30]], [2]
print(solution(n, start, end, roads, traps))