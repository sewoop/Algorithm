import sys

n = int(sys.stdin.readline().strip())

answer = [int(sys.stdin.readline().strip()) for _ in range(n)]

stack = []
result = []
ope = []
num, idx = 1, 0
while num <= n:
    if num != answer[idx]:
        stack.append(num) # push
        ope.append('+')
    else:
        stack.append(num) # push
        ope.append('+')
        while stack and stack[-1] == answer[idx]:
            result.append(stack.pop()) # pop
            ope.append('-')
            idx += 1
    num += 1

if result == answer:
    for i in ope:
        print(i)
else:
    print('NO')