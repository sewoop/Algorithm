n = list(map(int, input().split()))
print(sum([i ** 2 for i in n]) % 10)