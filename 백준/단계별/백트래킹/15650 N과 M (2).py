n, m = map(int, input().split())

data = [0] * m
used = [0] * (n + 1)

def backtrack(index):
    if index == m:
        for i in range(m):
            print(data[i], end=' ')
        print()
        return
    
    for i in range(1, n + 1):
        if not used[i]:
            data[index] = i
            for j in range(i + 1):
                used[j] = 1
            backtrack(index + 1)
            for j in range(i + 1):
                used[j] = 0

backtrack(0)

'''
N, M = map(int, input().split())

data = [0] * (N + 1)
check = [0] * (N + 1)

def backTracking(index):
    if index == M:
        for i in range(M):
            print(data[i], end=' ')
        print()
        return

    for i in range(1, N + 1):   # 1 2 3 4
        if check[i] == 1:       # 이전에 사용했다면
            continue            # 계속 진행
        data[index] = i         # 넣은 위치에 넣어줌

        for j in range(i + 1):
            check[j] = 1        # 들어간 숫자보다 작은 숫자 다 체크
        backTracking(index + 1)
        for j in range(1, N + 1):
            check[j] = 0        # 다음 수로 넘어가기 전에 전부 초기화 시킴

backTracking(0)
'''