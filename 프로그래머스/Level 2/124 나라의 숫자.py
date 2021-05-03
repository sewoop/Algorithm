''' 효율성 시간 초과 (Bottom-Up DP)
def solution(n):
    dp = ["" for _ in range(n + 1)]
    dp[0] = "4"
    if n > 0:
        dp[1] = "1"
    if n > 1:
        dp[2] = "2"
    if n > 2:
        dp[3] = "4"

    for i in range(4, n + 1):
        dp[i] = dp[(i - 1) // 3] + dp[i % 3]

    return dp[n]
'''

def solution(n):
    answer = ""
    
    char = ["4", "1", "2"]
    while n != 0:
        answer = char[n % 3] + answer
        n = (n - 1) // 3
    return answer

for i in range(1, 20):
    print(solution(i))
