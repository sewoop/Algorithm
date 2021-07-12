import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    funcs = input().strip().replace('RR', '')
    n = int(input())
    arr = input().strip()
    
    if funcs.count('D') > n:
        print('error')
        continue
    elif n == 0:
        arr = []
    else:
        arr = arr.lstrip('[').rstrip(']')
        arr = list(arr.split(','))

    left, right = 0, len(arr) - 1
    rev = False
    for func in funcs:
        if func == "R":
            rev = not rev
        elif func == "D":
            if rev:
                right -= 1
            else:
                left += 1

    if rev:
        print('['+','.join([arr[i] for i in range(right, left - 1, -1)])+']')
    else:
        print('['+','.join([arr[i] for i in range(left, right + 1)])+']')