import sys
input = sys.stdin.readline

string = input().strip()

stack_a = []
stack_b = []
answer = 0
coeff = 1
isPaired = True

for i in range(len(string)):
    if string[i] == "(":
        stack_a.append(i)
        coeff *= 2
    elif string[i] == "[":
        stack_b.append(i)
        coeff *= 3
    elif string[i] == ")":
        if stack_a:
            if string[i - 1] == "(":
                answer += coeff
            stack_a.pop()
            coeff //= 2
        else:
            isPaired = False
            break
    else:
        if stack_b:
            if string[i - 1] == "[":
                answer += coeff
            stack_b.pop()
            coeff //= 3
        else:
            isPaired = False
            break

if not stack_a and not stack_b and isPaired:
    print(answer)
else:
    print(0)