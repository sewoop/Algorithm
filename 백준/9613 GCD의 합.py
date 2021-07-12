T = int(input())

# 유클리드 호제법 이용
# 최대공약수


def gcd(m: int, n: int) -> int:
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
    return round(m*n/gcd(m, n))


for _ in range(T):
    lst = list(map(int, input().split()))

    sum_gcd = 0
    for i in range(1, lst[0]):  # 1,2,3
        for j in range(i+1, lst[0]+1):  # 2, 3, 4
            sum_gcd += gcd(lst[i], lst[j])

    print(sum_gcd)
