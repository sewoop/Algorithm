# 2750.py

n = int(input())
lt = [int(input()) for i in range(n)]
lt.sort()

for i in range(len(lt)):
    print(lt[i])
