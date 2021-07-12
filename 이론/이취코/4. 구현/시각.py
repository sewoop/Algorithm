# 내 풀이
def solution():
    n = int(input())

    count = 0
    time_h, time_m, time_s = 0, 0, 0
    while time_h != n or time_m != 59 or time_s != 60:
        if time_s == 60:
            time_m += 1
            time_s %= 60
        elif time_m == 60:
            time_h += 1
            time_m %= 60

        if '3' in f'{time_h}{time_m}{time_s}':
            count += 1

        time_s += 1

    print(count)

# 책 풀이


def book_solution():
    h = int(input())

    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if '3' in f'{i}{j}{k}':
                    count += 1

    print(count)


solution()
book_solution()
