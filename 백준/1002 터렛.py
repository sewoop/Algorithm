T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    R = [r1, r2, r]
    m = max(R)
    R.remove(m)

    if r == 0 and r1 == r2:  # 두 원이 일치하는 경우
        print("-1")
    elif r == r1 + r2 or m == sum(R):  # 두 원이 한 점에서 만나는 경우 : 외접, 내접
        print("1")
    elif m > sum(R):  # 두 점이 안 만나는 경우
        print("0")
    else:
        print("2")  # 두점에서 만나는 경우
