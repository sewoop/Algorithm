# 내 풀이
def solution():
    n = int(input())
    routes = input().split()

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    curr_x, curr_y = 1, 1

    for route in routes:
        if route == 'R':
            if (curr_x + dx[3] >= 1 and curr_x + dx[3] <= n) and (curr_y + dy[3] >= 1 and curr_y + dy[3] <= n):
                curr_x += dx[3]
                curr_y += dy[3]
        elif route == 'D':
            if (curr_x + dx[1] >= 1 and curr_x + dx[1] <= n) and (curr_y + dy[1] >= 1 and curr_y + dy[1] <= n):
                curr_x += dx[1]
                curr_y += dy[1]
        elif route == 'L':
            if (curr_x + dx[2] >= 1 and curr_x + dx[2] <= n) and (curr_y + dy[2] >= 1 and curr_y + dy[2] <= n):
                curr_x += dx[2]
                curr_y += dy[2]
        else:
            if (curr_x + dx[0] >= 1 and curr_x + dx[0] <= n) and (curr_y + dy[0] >= 1 and curr_y + dy[0] <= n):
                curr_x += dx[0]
                curr_y += dy[0]

    print(curr_x, curr_y)

# 책 풀이
def book_solution():
    n = int(input())
    plans = input().split()

    x, y = 1, 1

    # L, R, U, D: 좌우상하
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)): # 코드를 줄일 수 있는 방법
            if plan == move_types[i]:
                next_x = x + dx[i]
                next_y = y + dy[i]

        # 범위를 벗어나는 지를 체크
        if next_x < 1 or next_y < 1 or next_x > n or next_y > n:
            continue

        # 이동 수행
        x, y = next_x, next_y

    print(x, y)

solution()
book_solution()
'''
5
R R R U D D
'''