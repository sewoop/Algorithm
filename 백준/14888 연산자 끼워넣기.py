import math
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

result = []
total = 0


def backtrack(index):
    global total, result

    if index == n:
        result.append(total)
        return

    if index == 0:
        total += numbers[index]
        backtrack(index + 1)
        return

    for i in range(4):  # 0, 1, 2, 3
        if operators[i] != 0:
            operators[i] -= 1
            temp = total
            if i == 0:
                total = temp + numbers[index]
                backtrack(index + 1)
            elif i == 1:
                total = temp - numbers[index]
                backtrack(index + 1)
            elif i == 2:
                total = temp * numbers[index]
                backtrack(index + 1)
            else:
                total = math.trunc(temp / numbers[index])
                backtrack(index + 1)
            total = temp
            operators[i] += 1


backtrack(0)

print(max(result))
print(min(result))
