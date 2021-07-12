def solution(n, computers):
    answer = 0

    graph = {}
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                if i not in graph.keys():
                    graph[i] = [j]
                else:
                    graph[i].append(j)

    # Union-Find를 사용하여 각 네트워크를 구분
    union_find = [i for i in range(n)]  # [0, 1, 2]
    for i in range(n):
        if union_find[i] == i:
            stack = [i]
            visit = []
            while stack:
                node = stack.pop()
                if node not in visit:
                    visit.append(node)
                    union_find[node] = i
                    stack.extend(graph[node])

            answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
