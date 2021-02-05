from collections import deque

n, m = map(int, input().split())
extracts = deque([int(i) for i in input().split()])

queue = deque([i + 1 for i in range(n)])
count = 0

for extract in extracts:
    while queue:
        if queue[0] == extract: 
            queue.popleft()
            break
        else:
            position = queue.index(extract)
            if position < len(queue) - position:
                queue.rotate(-1)
                count += 1
            else:
                queue.rotate(1)
                count += 1
print(count)
