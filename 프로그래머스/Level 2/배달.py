def solution(N, road, K):
    INF = int(1e9)

    # floyd warshall
    path = [[INF for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                path[i][j] = 0

    for r in road:
        a, b, c = r
        path[a - 1][b - 1] = min(path[a - 1][b - 1], c)
        path[b - 1][a - 1] = min(path[b - 1][a - 1], c)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                path[i][j] = min(path[i][j], path[i][k] + path[k][j])

    answer = 0
    for i in range(N):
        if path[0][i] <= K:
            answer += 1
    return answer
