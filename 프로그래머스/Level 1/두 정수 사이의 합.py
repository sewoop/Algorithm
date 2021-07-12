# 두 정수 사이의 합
def solution(a, b):
    sum = 0
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        sum += i
    answer = sum
    return answer
