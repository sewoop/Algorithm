# 에라토스테네스의 체를 사용하여 구하기
def solution(n):
    num = set(range(2, n+1))
    # print(num)
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
            # print(f'{num} {set(range(2*i,n+1,i))}')
    return len(num)


if __name__ == "__main__":
    n = 10
    print(solution(n))


'''
에라토스테네스의 체를 가장 잘 나타낸 코드

# 2 ~ n 
num = set(range(2,n+1))

for i in range(2,n+1):
    if i in num:
        num-=set(range(2*i, n+1, i))

return len(num)
'''
