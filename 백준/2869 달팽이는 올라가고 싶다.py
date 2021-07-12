# 2869.py

a, b, h = map(int, input().split(' '))
day = (h-b)/(a-b)

print(int(day) if day == int(day) else int(day)+1)
