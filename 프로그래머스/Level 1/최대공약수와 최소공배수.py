# math module를 사용
import math
def solution(n, m):
    return [math.gcd(n,m), n*m//math.gcd(n,m)]

# math 없이
def solution(n, m):
    gcd = lambda a,b: b if not a%b else gcd(b, a%b)
    lcm = lambda a,b: a*b//gcd(a,b)

    return [gcd(n,m), lcm(n,m)]

if __name__ == "__main__":
    n = 12
    m = 18
    # print(solution(n,m))

    print(18%12)