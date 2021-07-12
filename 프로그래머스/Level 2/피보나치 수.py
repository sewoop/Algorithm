# def solution(n):
#     dp = [0] * (n + 1)
#     dp[1] = dp[2] = 1
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 2] + dp[i - 1]
#     return dp[n] % 1234567

def solution(n):
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a + b
    return b % 1234567


print(solution(3))
