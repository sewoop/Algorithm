import heapq
import sys

# 내 풀이 : 다익스트라 2번해서 구함


def solution():
    input = sys.stdin.readline
    INF = int(1e9)

    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]  # [[], [] ... []]

    # 그래프 초기화
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append((1, b))
        graph[b].append((1, a))

    x, k = map(int, input().split())

    # 시작 노드
    start = 1

    def dijkstra(start):
        distance = [INF] * (n + 1)  # 최단 거리

        heap = []
        heapq.heappush(heap, (0, start))
        distance[start] = 0

        while heap:
            dist, node = heapq.heappop(heap)

            if distance[node] < dist:
                continue

            for nextNode in graph[node]:
                cost = dist + nextNode[0]  # 경유해서 가는 경로

                if cost < distance[nextNode[1]]:  # 경유해서 간 것이 기존보다 비용이 덜 들면
                    heapq.heappush(heap, (cost, nextNode[1]))  # 바꿔줌
                    distance[nextNode[1]] = cost

        return distance

    # 1에서 찾아가는 노드 + k에서 찾아가는 노드
    result = dijkstra(start)[k] + dijkstra(k)[x]

    if result >= INF:
        print(-1)
    else:
        print(result)

# 책 풀이 : 플로이드 워셜 사용 (n의 크기가 작기 때문에 사용 가능)


def book_solution():
    INF = int(1e9)

    n, m = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 2차원 배열

    # self 제거
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    x, k = map(int, input().split())

    # 플로이드 워셜 점화식
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 수행 결과 출력
    distance = graph[1][k] + graph[k][x]

    if distance >= INF:
        print(-1)
    else:
        print(distance)


if __name__ == '__main__':
    solution()
    book_solution()

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4
'''
