# 내 풀이
def solution():
    inp = input()  # a1
    x_index, y_index = int(inp[1]), "abcdefgh".index(inp[0]) + 1

    # 우(상, 하),하(좌, 우), 좌(상, 하), 상(좌, 우)
    dy = [2, 2, -1, 1, -2, -2, -1, 1]
    dx = [-1, 1, 2, 2, -1, 1, -2, -2]

    count = 0
    for i in range(8):
        next_x, next_y = x_index + dx[i], y_index + dy[i]
        if next_x >= 1 and next_x <= 8 and next_y >= 1 and next_y <= 8:
            count += 1

    return count


print(solution())

# 책 풀이


def book_solution():
    # 현재 나이트의 위치 입력 받기
    input_data = input()
    row = int(input_data[1])
    column = int(ord(input_data[0])) - int(ord('a')) + 1

    # 나이트가 이동할 수 있는 8가지 방향 정의
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]

    # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
    result = 0
    for step in steps:
        # 이동하고자 하는 위치 확인
        next_row = row + step[0]
        next_column = column + step[1]

        # 해당 위치로 이동이 가능하다면 카운트 증가
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            result += 1

    return result


print(book_solution())
