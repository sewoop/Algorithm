import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

queue = deque([str(i + 1) for i in range(n)])
result = []

while queue:
    queue.rotate(len(queue) - k)
    result.append(queue.pop())

print(f'<{", ".join(result)}>')
