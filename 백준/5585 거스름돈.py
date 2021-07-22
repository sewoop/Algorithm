n = 1000 - int(input())

# print(n // 500 + n // 100 % 5 + n // 50 % 2 + n // 10 % 5 + n // 5 % 2 + n % 5)

count = 0
m = [500, 100, 50, 10, 5, 1]
for i in range(6):
    count += n // m[i]
    n %= m[i]
print(count)
