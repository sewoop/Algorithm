# 2523.py

n = int(input())

for i in range(2*n-1):
    if i < ((2*n-1)//2)+1:
        print((i+1)*'*')
    else:
        print(((2*n-1)-i)*'*')
