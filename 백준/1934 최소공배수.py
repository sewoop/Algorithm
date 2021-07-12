T = int(input())

# 유클리드 호제범
# 최대 공약수


def gcd(m: int, n: int) -> int:
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

# 최소 공배수


def lcm(m: int, n: int) -> int:
    return round(m*n/gcd(m, n))


for _ in range(T):
    m, n = map(int, input().split())

    print(lcm(m, n))
