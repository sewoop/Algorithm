from collections import deque

# graph = {
#     0: [1, 2, 4],
#     1: [0, 2],
#     2: [0, 1, 3, 4],
#     3: [2, 4],
#     4: [0, 2, 3]
# }

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}


root = 'A'

def bfs(graph, root):
    visited = []
    queue = deque([root])
    
    while queue:
        print(queue)
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited

print(bfs(graph, root))