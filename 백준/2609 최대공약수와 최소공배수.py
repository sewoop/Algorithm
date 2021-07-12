m, n = map(int, input().split())
# m, n = 24, 18

# 유클리드 호제법 이용
# 최대공약수


def gcd(m: int, n: int) -> int:
    '''
        123, 12 -> 123%12 = 3
        12, 3 -> 12%3 == 0
        3, 0 --> return 3
    '''
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

# 최소공배수


def lcm(m: int, n: int) -> int:
    '''
       ( m * n ) / gcd(m, n) 
    '''
    return round(m*n/gcd(m, n))


print(gcd(m, n))
print(lcm(m, n))
