n = int(input())
answer = list(input())
for _ in range(n - 1):
    for i, (a, b) in enumerate(zip(answer, input())):
        if a != b: answer[i] = "?"
print(''.join(answer))