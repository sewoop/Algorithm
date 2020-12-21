import math

# n: max 값
def is_prime(n: int) -> list:
    # n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
    prime_list = [True for _ in range(n + 1)] # 모든 수를 True로 초기화

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인
        if prime_list[i] == True # i가 소수인 경우
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                prime_list[i * j] = False
                j += 1

    return prime_list
