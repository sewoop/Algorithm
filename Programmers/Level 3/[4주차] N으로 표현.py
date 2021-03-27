def operation(lhs, rhs, ope):
    if ope == 0:
        res = lhs + rhs
    elif ope == 1:
        res = lhs // rhs
    else:
        res = int(f'{lhs}{rhs}')
    return res

# 작은 단위부터 시작
dp = [5] * 11
def solution(N, number):
    pass

if __name__ == '__main__':
    N, number = 5, 12
    
    print(solution(N, number))
