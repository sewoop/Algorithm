import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

# 시간 초과

length = len(numbers)
result = [-1 for _ in range(n)]
for standard in range(n):
    compare = standard + 1

    while compare < length and numbers[standard] >= numbers[compare]:
        compare += 1

    if compare != length:
        result[standard] = numbers[compare]
    standard += 1

for i in range(n):
    print(result[i], end=' ')
