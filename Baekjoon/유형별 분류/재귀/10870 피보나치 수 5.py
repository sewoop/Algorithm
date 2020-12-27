# 10870 피보나치 수 5

memo = {} # memoization
def fibo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 0
        return 0
    if n == 1:
        memo[1] = 1
        return 1
    if n == 2:
        memo[2] = 1
        return 1

    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

n = int(input())

print(fibo(n))