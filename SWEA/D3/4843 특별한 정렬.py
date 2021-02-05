from collections import deque
import re

Ts = int(input())

for T in range(1, Ts + 1):
    N = int(input())

    Deque = deque(sorted(list(map(int, input().split()))))

    lst = []
    for _ in range(N//2):
        lst.append(Deque.pop())
        lst.append(Deque.popleft())

    if len(lst) > 10 :
        lst = lst[0:10]

    # lst = str(lst).replace('[','').replace(']','').replace(',','')
    lst = re.sub(r"[\[\],]","",str(lst))
    print(f'#{T} {lst}')