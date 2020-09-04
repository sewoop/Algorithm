def find_min(row: int) -> None:
    global sum_, min_

    # 총 합이 최소값보다 크면 종료
    if sum_ > min_:
        return
    
    # row가 최대치를 넘어감
    if row == N:
        if sum_ < min_:
            min_ = sum_
            return
    
    for col in range(N):
        if not visited[col]:
            visited[col] = True
            sum_ += lst[row][col]
            find_min(row + 1)

            sum_ -= lst[row][col]
            visited[col] = False 

Ts = int(input())

for T in range(1, Ts + 1):
    N = int(input())

    # 입력 데이터 NxN
    lst = [ list(int(i) for i in input().split()) for _ in range(N) ] 
    # print(lst)

    visited = [False]*N
    sum_, min_ = 0, N*9
    find_min(0)

    print(f'#{T} {min_}')
