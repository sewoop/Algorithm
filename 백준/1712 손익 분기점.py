# 1712.py

a, b, c = map(int, input().split(' '))

if b < c:
    print(int(a/(c-b))+1)
else:
    print('-1')
