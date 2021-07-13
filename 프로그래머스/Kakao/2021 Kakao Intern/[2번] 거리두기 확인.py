# 카카오 인턴쉽 2021 - 2번 문제
def oob(x, y):
    if 0 <= x < 5 and 0 <= y < 5:
        return False
    return True


def check(place, x, y):
    visit = [[0] * 5 for _ in range(5)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = [(x, y, 0)]
    visit[x][y] = 1

    while queue:
        x, y, dist = queue.pop(0)

        # 처음 "P" 인 점에서부터 BFS를 진행하여 상하좌우를 검사, 이후에는 "O"에서 진행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not oob(nx, ny) and visit[nx][ny] == 0:
                # 만약, 상하좌우에서 "O"일 경우 "O"에서 다시 상하좌우 검색하여 만약 "P"가 있으면 False
                # 맨헤튼 거리가 2가 되는 지점에만 해당하므로 dist를 생각해준다.
                if place[nx][ny] == "O" and dist == 0:
                    visit[nx][ny] = 1
                    queue.append((nx, ny, dist + 1))
                elif place[nx][ny] == "P":
                    return False
    return True


def solution(places):
    answer = []

    for place in places:
        flag = True
        for i in range(5):
            for j in range(5):
                # "P"인 경우에만 주변을 검사한다.
                if place[i][j] != "P":
                    continue

                # 만약, False가 나타났다는 것은 해당 그룹이 거리두기를 지키지 않았다는 것이므로 바로 break
                if not check(place, i, j):
                    flag = False
                    break
            if not flag:
                break

        if not flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places=places))
