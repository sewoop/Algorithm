# 내 풀이
def solution():
    def pprint(visit):
        for i in range(len(visit)):
            print(visit[i])
        print()

    n, m = map(int, input().split()) # N, M을 입력 받음
    # n, m = 4, 5

    # 방문 확인용
    visit = [[0] * m for i in range(n)]

    # 얼음 틀을 입력 받음
    board = []
    for _ in range(n):
        board.append(list(map(int, input())))

    # board = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
    
    # DFS 구현 
    # 우하좌상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    count = 0 # 아이스크림 개수
    # 좌표 전체를 훝는다.
    for row in range(n):
        for col in range(m):
            # pprint(visit)

            x, y = row, col # 초기 위치

            if visit[x][y] == 0 and board[x][y] == 0: # 만약 현재 위치에서 얼음 틀의 구멍이 뚫려있고, 방문하지 않았으면
                count += 1 # 아이스크림 개수 + 1

                if board[x][y] == 0:
                    visit[x][y] = 1 # 방문 처리
                stack = [(x, y)] # 방문 기록을 담을 스택

                while stack:
                    x, y = stack.pop()

                    # 우하좌상으로 돌아가며 탐색
                    for i in range(4):
                        next_x, next_y = x + dx[i], y + dy[i] # 다음 좌표

                        # 틀을 넘어가면 안됨
                        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
                            if visit[next_x][next_y] == 0 and board[next_x][next_y] == 0: # 두 조건을 만족하면
                                stack.append((next_x, next_y)) # 방문 기록에 추가하고
                                visit[next_x][next_y] = 1
                                x, y = next_x, next_y # 갱신

    return count

print(solution())

# 책 풀이
def book_solution():
    # n,m을 공백으로 구분하여 입력 받기
    n, m = map(int, input().split())

    # 2차원 리스트의 맵 정보 입력받기
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    def dfs(x, y):
        # 주어진 범위를 벗어나는 경우에는 즉시 종료
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        
        # 현재 녿드를 아직 방문하지 않았다면
        if graph[x][y] == 0:
            # 해당 노드 방문 처리
            graph[x][y] = 1

            # 상하좌우의 위치도 모두 재귀적으로 호출
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    # 모든 노드(위치)에 대하여 음료수 채우기
    result = 0 
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 DFS 수행
            if dfs(i, j) == True:
                result += 1

    return result

print(book_solution())

'''
4 5
00110
00011
11111
00000
'''