# itertools
# import sys
# from itertools import permutations
# input = sys.stdin.readline

# n, m = map(int, input().split())
# numbers = sorted(map(int, input().split()))

# result = []

# for number in list(permutations(numbers, m)):
#     result.append(number)

# result = sorted(list(set(result)))

# for number in result:
#     for num in number:
#         print(num, end=' ')
#     print()

# direct
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
            used[i] = 1
            backtrack(index + 1)
            used[i] = 0


backtrack(0)

for number in sorted(set(result)):
    for num in number:
        print(num, end=' ')
    print()
