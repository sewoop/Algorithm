# 2446.py

n = int(input())
total = 2*n-1
for i in range(0, n-1):
    print(i*' ' + (total-2*i)*'*')
for i in range(n-1, -1, -1):
    print(i*' ' + (total-2*i)*'*')
