Ts = int(input())

for T in range(1, Ts + 1):
    find = str(input())
    find_in = str(input())

    print(f'#{T} {1 if find in find_in else 0}')