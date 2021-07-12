# 2447 별 찍기 - 10
def starPointer(star):
    res = []

    for i in range(3 * len(star)):
        if i // len(star) == 1:
            res.append(star[i % len(star)] + " " *
                       len(star) + star[i % len(star)])
        else:
            res.append(star[i % len(star)] * 3)

    return res


n = int(input())
star = ["***", "* *", "***"]
k = 0

while n != 3:
    n = int(n / 3)
    k += 1

# k == 2
for _ in range(k):
    star = starPointer(star)

for i in star:
    print(i)
