from collections import Counter

Ts = int(input())

for T in range(1, Ts + 1):
    find = list(input())
    find_in = list(input())
    
    count_in = Counter([i for i in find_in if i in find])

    count = sorted(count_in.values(), key=lambda x: x, reverse=True)
    print(f'#{T} {count[0]}')