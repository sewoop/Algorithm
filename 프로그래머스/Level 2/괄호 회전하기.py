def solution(s):
    def isCorrect(string):
        match = {")": "(", "}": "{", "]": "["}
        stack = []
        for s in string:
            if not stack or s not in match:
                stack.append(s)
            elif match[s] == stack[-1]:
                stack.pop()
        return not(stack)

    string = list(s)
    answer = 0
    for _ in range(len(string)):
        if isCorrect(string): answer += 1
        string = string[1: len(string)] + [string[0]]
    return answer

s = "[](){}"
# s = "}]()[{"
# s = "[)(]"
# s = "}}}"
print(solution(s))