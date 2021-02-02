import sys
from collections import deque

n = int(sys.stdin.readline().strip())

queue = deque()
for _ in range(n):
    command = sys.stdin.readline().strip()

    if "push" in command:
        command = command[5:]
        queue.append(command)
    elif command == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "front":
        print(queue[0]) if queue else print(-1)
    elif command == "back":
        print(queue[-1]) if queue else print(-1)
    elif command == "empty":
        print(0) if queue else print(1)