import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

# 스택 활용

result = [-1 for _ in range(n)]
stack = [0]
i = 1

while stack and i < n:
    while stack and numbers[stack[-1]] < numbers[i]:
        result[stack[-1]] = numbers[i]
        stack.pop()
    stack.append(i)
    i += 1

for i in range(n):
    print(result[i], end=" ")
