import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
INF = int(1e9)

# Dijkstra
def short_path_1():
    v, e = map(int, input().split())
    start = int(input())
    distance = [INF] * (v + 1)

    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))

    def dijkstra(start):
        heap = []
        heapq.heappush(heap, (0, start))
        distance[start] = 0

        while heap:
            dist, node = heapq.heappop(heap)

            if distance[node] < dist: # 기존 루트보다 더 작은 값이 이미 갱신이 된 상태면 continue
                continue

            for nextNode in graph[node]:
                cost = dist + nextNode[0]

                if distance[nextNode[1]] > cost:
                    heapq.heappush(heap, (cost, nextNode[1]))
                    distance[nextNode[1]] = cost
                
    dijkstra(start)

    print(*distance[1:])

            
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

# Floyd-Warshall
def short_path_2():
    v, e = map(int, input().split())
    graph = [[INF] * (v + 1) for _ in range(v + 1)] 

    for i in range(v + 1):
        for j in range(v + 1):
            if i == j:
                graph[i][j] = 0

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, v + 1):
        for j in range(1, v + 1):
            print(graph[i][j], end=' ')
        print()

    # print(graph[1][3])

'''
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''

# Bellmam-Ford
def short_path_3():
    v, e = map(int, input().split())

    dist = [INF] * (v + 1)
    edges = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    start = 1

    def bellmanFord(start):
        dist[start] = 0

        for i in range(v):
            for cost, cur, nxt in edges:
                if dist[cur] != INF and dist[nxt] > dist[cur] + cost:
                    dist[nxt] = dist[cur] + cost

                    if i == v - 1:
                        return True

        return False

    isCycle = bellmanFord(start)

    if isCycle:
        print('Cycle')
    else:
        print(*dist[1:])

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

# Union-Find
def union_find():
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    v, e = map(int, input().split())
    parent = [i for i in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    for i in range(v + 1):
        find_parent(parent, i)

    print(parent)
    
'''
6 4
1 4
2 3
2 4
5 6
'''

# Kruskal
def mst_1():
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    v, e = map(int, input().split())
    parent = [i for i in range(v + 1)]

    edges = []
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    edges.sort()

    result = []
    dist = 0
    for edge in edges:
        cost, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result.append((a, b))
            dist += cost

    print(result) # [(3, 4), (4, 7), (4, 6), (1, 2), (2, 6), (5, 6)]
    print(dist) # 159

'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''

# Prim
def mst_2():
    v, e = map(int, input().split())
    
    edges = []
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    result = []
    start = 1
    adjacent_edges = defaultdict(list)

    for cost, a, b in edges:
        adjacent_edges[a].append((cost, a, b))
        adjacent_edges[b].append((cost, b, a))

    connected_nodes = set([start])
    
    candidate_edges = adjacent_edges[start]
    heapq.heapify(candidate_edges)

    while candidate_edges:
        cost, a, b = heapq.heappop(candidate_edges)
        
        if b not in connected_nodes:
            connected_nodes.add(b)
            result.append((cost, a, b))

            for edge in adjacent_edges[b]:
                if edge[2] not in connected_nodes:
                    heapq.heappush(candidate_edges, edge)

    print(result)

'''
7 9
1 2 29
1 7 10
2 3 16
2 4 15
3 5 12
4 5 18
4 6 25
5 6 22
6 7 27
'''


if __name__ == '__main__':
    # short_path_1()
    # short_path_2()
    short_path_3()
    # union_find()
    # mst_1()
    # mst_2()