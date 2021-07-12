from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    visit = [0] * (n + 1)

    # 그래프 초기화 (양방향)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    start = 1
    depth = [0] * (n + 1)
    queue = deque([start])
    visit[start] = 1

    while queue:  # DP와 BFS를 활용
        # print(depth)
        node = queue.popleft()

        for nextNode in graph[node]:
            if visit[nextNode] != 1:
                visit[nextNode] = 1
                depth[nextNode] = depth[node] + 1
                queue.append(nextNode)

    max_depth = max(depth)
    answer = 0
    for i in depth:
        if i == max_depth:
            answer += 1

    return answer


if __name__ == '__main__':
    n, edge = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, edge))
