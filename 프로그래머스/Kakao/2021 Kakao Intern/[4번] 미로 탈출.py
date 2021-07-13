# 카카오 인턴쉽 2021 - 4번 문제 : 풀이 중
import heapq
from collections import deque

INF = int(1e9)

def swap(path):
    # a -> b 의 단방향 그래프를 b -> a 로 변경
    return list(zip(*path))

def dijkstra(n, trap, traps, path, distance, start):
    origin_path = path

    heap = []
    
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        if now in traps:
            if trap[now]:
                trap[now] = False
                path = origin_path
            else:
                trap[now] = True
                path = swap(path)

        for i in list(filter(lambda x: path[now][x] != INF, range(1, n + 1))):
            cost = dist + path[now][i]

            if cost < distance[i]:
                if i not in traps:
                    distance[i] = cost
                heapq.heappush(heap, (cost, i))


def solution(n, start, end, roads, traps):
    path = [[INF] * (n + 1) for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    trap = dict(zip(traps, [False] * len(traps)))
    
    # 경로 초기화
    for road in roads:
        a, b, cost = road
        # if path[a][b] > cost:
        path[a][b] = cost

    # Dijkstra
    dijkstra(n, trap, traps, path, distance, start)

    return distance[end]


# n, start, end, roads, traps = 3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]
n, start, end, roads, traps = 4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]
print(solution(n, start, end, roads, traps))