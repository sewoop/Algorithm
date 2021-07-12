import sys

t = int(sys.stdin.readline())

for _ in range(t):
    gaulho = list(sys.stdin.readline().strip())

    stack = []
    try:
        for i in gaulho:
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
        print('NO') if stack else print('YES')
    except:
        print('NO')
