# 4673.py

def d(n):
    sum_ = n
    while n>0:
        sum_ += n%10
        n = n//10
    return sum_

lt = []
for i in range(1,10001):
    k = d(i)
    lt.append(k)

for i in range(1, 10001):
    if i not in lt:
        print(i)

# r=range(9999);print(*sorted({*r}-{ n+sum(map(int, str(n))) for n in r}))