import sys

n = int(sys.stdin.readline())

deque = []
for _ in range(n):
    control = sys.stdin.readline()

    if "push_front" in control:
        _, num = control.split()
        deque.insert(0, int(num))
    elif "push_back" in control:
        _, num = control.split()
        deque.append(int(num))
    elif "pop_front" in control:
        print(deque.pop(0)) if deque else print(-1)
    elif "pop_back" in control:
        print(deque.pop()) if deque else print(-1)
    elif "size" in control:
        print(len(deque))
    elif "empty" in control:
        print(0) if deque else print(1)
    elif "front" in control:
        print(deque[0]) if deque else print(-1)
    elif "back" in control:
        print(deque[-1]) if deque else print(-1)
