from collections import deque
import copy

n = int(input())
indegree = [0] * (n + 1)
time = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1: -1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            result[i] = max(result[i], result[node] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()

'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''