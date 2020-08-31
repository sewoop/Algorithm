def paper(x):
    if x == N:
        return 1
    if x > N:
        return 0
    return paper(x + 10) + paper(x + 20) * 2  
    

Ts = int(input())

for T in range(1, Ts + 1):
    N = int(input())

    print(f'#{T} {paper(0)}')

    

