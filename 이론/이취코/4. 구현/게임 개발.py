# 내 풀이, 풀이 후 책 풀이 참고하여 수정

# 배열 프린트 시각적 표현을 위해
def pprint(gmap):
    for i in range(len(gmap)):
        print(gmap[i])
    print()

# 좌측으로 도는 함수


def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


def solution():
    n, m = map(int, input().split())  # N x M 크기의 맵
    x, y, direction = map(int, input().split())  # 캐릭터 위치 및 방향 설정

    # 맵 방문 표시
    visit = [[0] * m for i in range(n)]
    visit[x][y] = 1  # 초기 위치 방문 설정

    # 맵 생성 과정
    gmap = []
    for _ in range(n):
        gmap.append(list(map(int, input().split())))

    # 반시계 방향으로 회전 상우하좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 시뮬레이션
    count, turn = 1, 0
    while True:
        # 왼쪽으로 회전
        direction = turn_left(direction)

        next_x = x + dx[direction]  # x : row
        next_y = y + dy[direction]  # y : col

        # 칸을 벗어나는 지 확인
        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
            # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
            if visit[next_x][next_y] == 0 and gmap[next_x][next_y] == 0:
                visit[next_x][next_y] = 1
                x, y = next_x, next_y
                count += 1
                turn = 0
                continue

            # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
            else:
                turn += 1

            # 네 방향 모두 갈 수 없는 경우
            if turn == 4:
                next_x = x - dx[direction]
                next_y = y - dy[direction]

                # 칸을 벗어나는 지 확인
                if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
                    # 뒤로 갈 수 있으면 이동
                    if gmap[next_x][next_y] == 0:
                        x, y = next_x, next_y

                # 뒤에 막혀있는 경우
                else:
                    break
                turn = 0

    return count


print(solution())

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

4 4
0 0 0
0 1 1 1
0 0 0 1
1 1 0 0
1 1 1 0

3 3
1 1 0
1 1 1
1 0 0
1 1 0
'''
