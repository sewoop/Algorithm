def solution(s):
    result = list(map(int, s.split()))
    return f'{min(result)} {max(result)}'

s = "1 2 3 4"
print(solution(s))