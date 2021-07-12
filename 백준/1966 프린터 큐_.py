import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    queue = deque([int(i) for i in sys.stdin.readline().split()])

    current = m
    prior = queue[m]
    count = 0

    while queue:
        maximum = max(queue)
        front = queue.popleft()
        if not current:
            if prior == maximum:
                count += 1
                break
            else:
                queue.append(front)
                current = len(queue) - 1
        else:
            current -= 1
            if front == maximum:
                count += 1
            else:
                queue.append(front)
    print(count)
