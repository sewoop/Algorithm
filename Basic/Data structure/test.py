data = 1
max_ = 0
answer = []
visit = []

def find(x: int, y: int, n: int):
    global data, max_, answer, visit

    # 하 우 대좌
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    count = 0

    if data > max_:
        return

    visit[x][y] = 1
    answer[x][y] = data

    # print(answer)
    for i in range(3):
        if visit[n-1][n-1] == 0 and visit[1][1] == 0:
            next_x = x + dx[i]
            next_y = y + dy[i]
        elif visit[n-1][n-1] != 0 and visit[1][1] == 0:
            next_x = x - 1
            next_y = y - 1
        else:
            next_x = x + dx[i]
            next_y = y + dy[i]
                
        if (0<=next_x<n) and (0<=next_y<n) and visit[next_x][next_y] != 1:
            data += 1 
            find(next_x, next_y, n)

def solution(n):
    global data, max_, answer, visit

    visit = [[1]*n for _ in range(n)]
    answer = [[-1]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1):
            visit[i][j] = answer[i][j] = 0
            

    max_ = (n**2+n)//2
    find(0, 0, n)

    result = []
    for i in range(n):
        for j in range(n):
            if answer[i][j] != -1:
                result.append(answer[i][j])

    return result

print(solution(100))