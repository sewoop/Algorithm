import sys

n = int(sys.stdin.readline())

queue = []
for _ in range(n):
    control = sys.stdin.readline()

    if "push" in control:
        _, num = control.split()
        queue.append(int(num))

    elif "front" in control:
        print(queue[0]) if queue else print(-1)
    elif "back" in control:
        print(queue[-1]) if queue else print(-1)
    elif "size" in control:
        print(len(queue))
    elif "empty" in control:
        print(0) if queue else print(1)
    elif "pop" in control:
        print(queue.pop(0)) if queue else print(-1)