# 2292.py

n = int(input())
a,b,cnt = 1,6,1

while n>a:
    cnt+=1
    a+=b
    b+=6
print(cnt)
