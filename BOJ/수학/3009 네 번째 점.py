locationX = []
locationY = []

for _ in range(3):
    x, y = map(int, input().split())
    if x in locationX:
        locationX.remove(x)
    else:
        locationX.append(x)

    if y in locationY:
        locationY.remove(y)
    else:
        locationY.append(y)

print(*locationX, *locationY)
