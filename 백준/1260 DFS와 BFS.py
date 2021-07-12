from collections import defaultdict, deque
import sys


def dfs(graph, root):
    visit = []
    stack = [root]

    while stack:
        node = stack.pop()

        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


def bfs(graph, root):
    visit = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node not in visit:
            visit.append(node)
            queue.extend(list(reversed(graph[node])))

    return visit


n, m, root = map(int, sys.stdin.readline().split())

graph = defaultdict(list)

for _ in range(m):
    k, v = map(int, sys.stdin.readline().split())
    graph[k].append(v)
    graph[v].append(k)

for v in graph.values():
    v.sort(reverse=True)

print(*dfs(graph, root))
print(*bfs(graph, root))
