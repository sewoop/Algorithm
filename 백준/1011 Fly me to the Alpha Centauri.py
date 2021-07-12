# 1011.py
'''
    0 1 2 3 4 5 6 7

    k-1 k k+1

    1 : 0 1 2
    2 : 1 2 3
    3 : 2 3 4

    0 s1 : 0 1 2
    0 s2 : 1 2 3

    0 -> 1 : 1
    0 -> 2 : 1+1
    0 -> 3 : 1+1+1
    0 -> 4 : 1+2+1
    0 -> 5 : 1+2+1+1
    0 -> 6 : 1+2+2+1
    0 -> 7 : 1+1+2+2+1


'''

T = int(input())

for _ in range(T):
    a, b = input().split()

    c = int(b) - int(a)
    num = 1
    while True:
        if num ** 2 <= c < (num + 1) ** 2:
            break
        num += 1
    if num ** 2 == c:
        print((num * 2) - 1)
    elif num ** 2 < c <= num ** 2 + num:
        print(num * 2)
    else:
        print((num * 2) + 1)
