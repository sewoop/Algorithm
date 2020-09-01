Ts = int(input())

def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def maze_tracking(x, y):
    # 우, 하, 좌, 상 
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    global isPath

    if maze[x][y] == 3:
        isPath = True
        return 

    visited.append((x, y))

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if (next_x, next_y) not in visited and (0<=next_x<N and 0<=next_y<N) and maze[next_x][next_y] != 1:
            maze_tracking(next_x, next_y)


for T in range(1, Ts + 1):
    N = int(input())
    maze = [ [int(n) for n in input()] for _ in range(N)]

    visited = []
    isPath = False
    
    start_x, start_y = find_start()
    
    try:
        maze_tracking(start_x, start_y)
    except:
        isPath = 'error'

    print(f'#{T} {1 if isPath else 0}')