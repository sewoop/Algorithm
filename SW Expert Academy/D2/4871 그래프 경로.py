from collections import defaultdict, deque

Ts = int(input())

for T in range(1, Ts + 1):
    V, E = map(int, input().split())

    # 방문 체크, 스택, 간선
    visited = list()
    stack = deque()
    edge = defaultdict(list)

    # 그래프 생성
    for _ in range(E):
        v1, v2 = map(int, input().split())
        edge[v1].append(v2)

    # print(edge)
    
    # 출발 노드, 도착 노드
    start_node, end_node = map(int, input().split())

    stack.append(start_node)
    while stack:
        # print(stack)
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(edge[n])
    
    if end_node in visited:
        print(f'#{T} 1')
    else:
        print(f'#{T} 0')