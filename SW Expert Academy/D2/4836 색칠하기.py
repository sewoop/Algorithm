import collections

Ts = int(input())

for T in range(1, Ts+1):
    # 칠한 영역 개수 N
    N = int(input())

    # 전체 영역
    panel = [[0 for _ in range(10)] for _ in range(10)]
    # print(panel)

    # 영역 추출
    for _ in range(N):
        temp = list(map(int, input().split()))
        
        for row in range(temp[0], temp[2] + 1):
            for col in range(temp[1], temp[3] + 1):
                if panel[row][col] == 1 and temp[-1] == 2:
                    panel[row][col] += temp[-1]
                elif panel[row][col] == 2 and temp[-1] == 1:
                    panel[row][col] += temp[-1]
                else:
                    panel[row][col] = temp[-1]
        
    count = collections.Counter(sum(panel,[]))
    print(f'#{T} {count[3]}')

