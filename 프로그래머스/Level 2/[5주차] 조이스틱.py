''' # 11번 테스트 케이스가 안됨
def find_effective(index, name, visit):
    # 우
    if index == len(name) - 1:
        next_right = 0
    else:
        next_right = index + 1

    # 좌
    if index == 0:
        next_left = len(name) - 1
    else:
        next_left = index - 1

    # 좌우 비교
    if alphabet_diff(next_left, name) == 0 and alphabet_diff(next_right, name) != 0:
        if visit[next_right] == 0:
            return next_right
        else:
            return next_left
    elif alphabet_diff(next_left, name) != 0 and alphabet_diff(next_right, name) == 0:
        if visit[next_left] == 0:
            return next_left
        else:
            return next_right
    else:
        if visit[next_left] == 0:
            return next_left
        else:
            return next_right
            
def alphabet_diff(index, name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    char_index = alphabet.index(name[index])

    if len(alphabet) // 2 < char_index:
        return len(alphabet) - char_index
    else:
        return char_index

def solution(name):
    
    name = list(name)
    string = ['A'] * len(name)
    visit = [0] * len(name)

    index = count = 0
    while True:
        # 현재 라인에서 바꾸기 실행
        count += alphabet_diff(index, name)
        string[index] = name[index]
        visit[index] = 1

        if string == name:
            break

        # 다음 인덱스
        index = find_effective(index, name, visit)
        count += 1

    return count
'''


def solution(name):
    alphabet = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]

    index = count = 0
    while True:
        # 상하로 알파벳 변경
        count += alphabet[index]
        alphabet[index] = 0

        if sum(alphabet) == 0:
            return count

        # 좌우 탐색 : 'A'를 만날 경우 계속 진행해 봄
        left_index = right_index = 1
        # 좌측
        while alphabet[index - left_index] == 0:
            left_index += 1

        # 우측
        while alphabet[index + right_index] == 0:
            right_index += 1

        # 좌/우 중에 더 적게 이동한 것이 좋은 경로
        if left_index < right_index:
            count += left_index
            index += -left_index
        else:
            count += right_index
            index += right_index
    return count


name = "JEAAAEN"
# name = "JEROEN"
# name = "JAZ"
# name = "JAN"
# name = "JAZ"

print(solution(name))
