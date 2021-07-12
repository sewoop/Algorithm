while True:
    x, y, z = map(int, input().split())

    if x == 0 and y == 0 and z == 0:
        break

    data = sorted([x, y, z])

    if data[2]**2 == data[0]**2 + data[1] ** 2:
        print("right")
    else:
        print("wrong")
