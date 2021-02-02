import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

t = int(input())

for _ in range(t):
    function = input().replace("RR", "")
    n = int(input())
    queue = deque(eval(input()))

    rev, flag = False, True
    for func in function:
        if func == "R":
            rev = not rev
        elif func == "D":
            if queue:
                if rev:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                flag = False
                break

    if flag:
        if rev:
            print(str([int(i) for i in list(queue)[::-1]]).replace(' ', ''))
        else:
            print(str([int(i) for i in list(queue)]).replace(' ', ''))
    else:
        print('error')