import sys
input = sys.stdin.readline

n = int(input())
dp = [[0, 0, 0] for _ in range(n)]

price = []
for _ in range(n):
    price.append(list(map(int, input().split())))

dp[0] = [i for i in price[0]]

for i in range(n):
    for j in range(3):
        dp[i][j] = price[i][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])

print(min(dp[n - 1]))