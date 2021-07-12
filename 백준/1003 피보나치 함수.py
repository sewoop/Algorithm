t = int(input())

memo = [False] * 10001
count = [False] * 10001


def fibonacci(n):
    if memo[n]:
        return memo[n]

    if n == 0:
        count[n] = [1, 0]
        memo[n] = n
        return 0
    if n == 1:
        count[n] = [0, 1]
        memo[n] = n
        return 1

    fibo = fibonacci(n - 1) + fibonacci(n - 2)
    count[n] = [count[n - 1][0] + count[n - 2]
                [0], count[n - 1][1] + count[n - 2][1]]
    memo[n] = fibo

    return fibo


for _ in range(t):
    n = int(input())

    fibonacci(n)
    print(count[n][0], count[n][1])
