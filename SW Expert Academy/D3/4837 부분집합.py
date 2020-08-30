Ts = int(input())

for T in range(1, Ts+1):
    N, K = map(int, input().split())


    sets = set(range(1,13))
    sets_up = set(range(K+1,13))

    diff_sets = list(sets-sets_up)
    
    n = len(diff_sets)
    count = 0
    for i in range(1<<n):
        lst = []
        for j in range(n):
            t_f = i & (1 << j)
            if t_f:
                lst.append(diff_sets[j])
        # print(lst)

        if len(lst) == N and sum(lst) == K:
            count+=1

    print(f'#{T} {count}')
        


    
        