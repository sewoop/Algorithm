import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

data = [0] * m
used = [0] * (n + 1)

result = []

def backtrack(index):
    if index == m:    
        result.append(tuple(data[:m]))
        return
    
    for i in range(1, n + 1):
        if not used[i]:
            data[index] = numbers[i - 1]
            for j in range(i):
                used[j] = 1
            backtrack(index + 1)
            for j in range(i):
                used[j] = 0

backtrack(0)

for number in sorted(set(result)):
    for num in number:
        print(num, end=' ')
    print()