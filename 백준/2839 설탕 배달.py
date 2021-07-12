a = int(input())

cnt = 0
while a > 0:
    if a % 5 == 0:
        a -= 5
        cnt += 1
    elif a % 3 == 0:
        a -= 3
        cnt += 1
    elif a > 5:
        a -= 5
        cnt += 1
    else:
        cnt = -1
        break
print(cnt)
