import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def bf(start):
    # 시작 노드에 대해 초기화
    dist[start] = 0

    # 전체 n번의 라운드(round)를 반복
    for i in range(n):
        # 매 반복마다 모든 간선을 확인
        for j in range(m):
            curr, next_node, cost = edges[j]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[curr] != INF and dist[next_node] > dist[curr] + cost:
                dist[next_node] = dist[curr] + cost

                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1:
                    return True

    return False

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []

# 최단거리 테이블을 모두 무한으로 초기화
dist = [INF] * (n + 1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 간는 비용이 c라는 의미
    edges.append((a, b, c))

# 벨만 포드 알고리즘을 수행
cycle = bf(1) # 1번 노드가 시작 노드

if cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단거리 출력
    for i in range(2, n + 1):
        # 도달할 수 없는 경우, -1 출력
        if dist[i] == INF:
            print("-1")
        # 도달할 수 있는 경우 거리를 출력
    print(dist[1:])
'''
5 10
1 2 6
1 4 7
2 3 5
2 5 -4
2 4 8
3 2 -2
4 3 -3
4 5 9
5 3 7
5 1 2
'''