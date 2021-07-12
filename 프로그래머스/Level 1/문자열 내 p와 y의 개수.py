# 문자열 내 p와 y의 개수
def solution(s):
    s = s.upper()
    p = s.count('P')
    y = s.count('Y')

    if p == y:
        answer = True
    else:
        answer = False
    return answer
