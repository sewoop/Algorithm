# 유클리드 호제법 이용
# 최소공배수
def lcm(m: int, n: int) -> int:
    # 최대 공약수
    def gcd(m: int, n: int) -> int:
        if m < n: # 두번째 수를 첫번째 수보다 작도록 배치
            m, n = n, m
        if n == 0: # n이 0이면 m이 최대공약수이다.
            return m
        if m % n == 0: # m이 n으로 나누어 떨어지면 n을 반환
            return n
        else:
            return gcd(n, m%n)

    return (m * n)//gcd(m, n) # 최소공배수 = 두수의 곱 / 최대공약수

print(lcm(24, 18))

