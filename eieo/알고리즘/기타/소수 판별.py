import math

def isPrime(x: int) -> bool:
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어지면
        if x % i == 0:
            return False
    return True