import sys
k = int(sys.stdin.readline())

stack = []
for _ in range(k):
    temp = int(sys.stdin.readline())
    if temp:
        stack.append(temp)
    else:
        stack.pop()
print(sum(stack))
