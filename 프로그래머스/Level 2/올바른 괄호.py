def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif stack and stack[-1] == "(":
            stack.pop()
        else:
            return False
    return not(stack)

s = "()()"
s = ")()("
print(solution(s))