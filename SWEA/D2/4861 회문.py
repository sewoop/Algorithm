Ts = int(input())

for T in range(1, Ts + 1):
    N, M = map(int, input().split())

    lst = [list(input()) for _ in range(N)]
    find = ''
    
    # 가로 검색
    # for i in range(N):
    #     for j in range(N-M+1):
    #         temp = lst[i][j:j+M]
    #         # print(temp)

    #         if temp == temp[::-1]:
    #             find = ''.join(temp)

    # # 세로 검색
    # for i in range(N):
    #     for j in range(N-M+1):
    #         temp = [lst[k][i] for k in range(j, j+M)]
    #         # print(temp)

    #         if temp == temp[::-1]:
    #             find = ''.join(temp)


    for i in range(N):
        for j in range(N-M+1):
            temp_row = lst[i][j:j+M]
            temp_col = [lst[k][i] for k in range(j, j+M)]
            
            if temp_row == temp_row[::-1] and temp_col != temp_col[::-1]:
                find = ''.join(temp_row)
            elif temp_col == temp_col[::-1] and temp_row != temp_row[::-1]:
                find = ''.join(temp_col)

    print(f'#{T} {find}')