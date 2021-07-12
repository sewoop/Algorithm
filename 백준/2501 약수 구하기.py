# 2501.py

a, b = map(int, input().split())

lt = []
for i in range(a):
    if a % (i+1) == 0:
        lt.append(i+1)

print(0 if len(lt) < b else lt[b-1])
