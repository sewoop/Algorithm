'''
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
        data[index] = numbers[i - 1]
        used[i] = 1
        backtrack(index + 1)
        used[i] = 0

backtrack(0)

for number in sorted(set(result)):
    for num in number:
        print(num, end=' ')
    print()
'''

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = sorted(set(map(int, input().split())))
ans = []

def backtrack(index):
    if index == m:
        print(*ans)
        return

    for i,num in enumerate(nums):
        ans.append(num)
        backtrack(index+1)
        ans.pop()

backtrack(0)