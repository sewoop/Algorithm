import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

# Prim
def prim():
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