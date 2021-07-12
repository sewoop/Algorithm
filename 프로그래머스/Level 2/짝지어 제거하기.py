def solution(s):
    stack = []
    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
            continue
        if stack[-1] == i:
            stack.pop()
    return 0 if stack else 1


s = "baabaa"
s = "cdcd"
s = "c"
s = ""
print(solution(s))
