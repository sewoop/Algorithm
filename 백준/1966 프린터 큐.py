import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    queue = deque([(i, int(v))
                  for i, v in enumerate(sys.stdin.readline().split())])

    res = []
    while queue:
        maximum = max(queue, key=lambda x: x[1])[1]
        if queue[0][1] < maximum:
            queue.rotate(-1)
        else:
            res.append(queue.popleft())

    for i, v in enumerate(res):
        if v[0] == m:
            print(i + 1)
            break
