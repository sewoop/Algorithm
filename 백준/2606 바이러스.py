def solution():
    n = int(input())
    m = int(input())

    # matrix
    network = [[] for _ in range(n + 1)]
    visit = [0] * (n + 1)

    # connection
    for _ in range(m):
        a, b = map(int, input().split())

        network[a].append(b)
        network[b].append(a)

    # BFS
    queue = [1]
    visit[1] = 1

    count = 0
    while queue:
        node = queue.pop(0)

        for i in network[node]:
            if visit[i] == 0:
                count += 1
                visit[i] = 1
                queue.append(i)

    print(count)


solution()
