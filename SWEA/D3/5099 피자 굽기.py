from collections import deque

Ts = int(input())
# Ts = 1

for T in range(1, Ts + 1):
    N, M = map(int, input().split())
    # N, M = 5, 10

    # 치즈의 양
    cheese = {i:int(v) for i, v in enumerate(input().split())}
    # print(cheese)

    # 큐 생성
    queue = deque()

    # [7 2 6 5 3]
    # 화덕에 3개를 넣고 [7 2 6], popleft할때마다 //2를 수행 후 치즈 양 확인. 만약 0이면 새로운 피자 삽입 아니면 다시 넣고 돌린다.

    # Queue 초기화
    for i in range(N):
        queue.append(i)

    idx = N-1
    complete = []
    # 반복
    while queue:
        temp = queue.popleft()  # 0
        cheese[temp] = cheese[temp] // 2

        if cheese[temp] == 0:
            complete.append(temp)
            if idx != M-1:
                idx += 1
                queue.append(idx)
        else:
            queue.append(temp)
        
    print(f'#{T} {complete[-1]+1}')