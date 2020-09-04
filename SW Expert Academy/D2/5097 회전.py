from collections import deque

Ts = int(input())

for T in range(1, Ts + 1):

    N, M = map(int, input().split())
    # N, M = 5, 12

    queue = deque()

    for i in input().split():
        queue.append(int(i))
    # for i in [18140, 14618, 18641, 22536, 23097]:
    #     queue.append(int(i))

    cnt = 0
    while cnt != M:
        cnt += 1
        queue.append(queue.popleft())


    print(f'#{T} {queue[0]}')