"""
# Topology Sort
from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int, input().split())

# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능

    # 진입 차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    queue = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 원소 꺼내기
        node = queue.popleft()
        result.append(node)

        # 해당 원소와 연결된 노드들의 진입 차수에서 -1하기
        for i in graph[node]:
            indegree[i] -= 1

            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                queue.append(i)

    # 위상 정렬 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()

'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''
"""

# 위상 정렬 복습
from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

    # 진입 차수 증가
    indegree[b] += 1

def topology_sort():
    result = []
    queue = deque()

    # 진입 차수가 0인 노드 찾아 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        result.append(node)

        # 인접 노드들의 진입 차수 낮추기
        for i in graph[node]:
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=" ")

topology_sort()

'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''