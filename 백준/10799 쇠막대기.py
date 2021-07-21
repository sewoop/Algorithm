import sys
input = sys.stdin.readline

batch = input().strip()
stack = []
answer = 0

for i in range(len(batch)):
    if batch[i] == "(":
        stack.append(batch[i])
    else:
        if batch[i - 1] == "(":
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)
