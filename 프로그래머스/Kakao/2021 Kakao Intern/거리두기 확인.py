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

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not oob(nx, ny) and visit[nx][ny] == 0:
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
                if place[i][j] != "P":
                    continue
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
