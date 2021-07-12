def solution(numbers, hand):
    answer = ''

    position = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (
        1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    left = position['*']
    right = position['#']

    for number in numbers:
        if number in [1, 4, 7]:
            left = position[number]
            answer += 'L'
        elif number in [3, 6, 9]:
            right = position[number]
            answer += 'R'
        else:
            answer += diff(position, number, left, right, hand)
            if answer[-1] == 'L':
                left = position[number]
            else:
                right = position[number]

    return answer


def diff(position, number, left, right, hand):
    left_diff = abs(position[number][0]-left[0]) + \
        abs(position[number][1]-left[1])
    right_diff = abs(position[number][0]-right[0]) + \
        abs(position[number][1]-right[1])

    if left_diff == right_diff:
        return 'L' if hand == 'left' else 'R'
    return 'R' if left_diff > right_diff else 'L'


if __name__ == "__main__":
    # numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    # hand = "right"

    # numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    # hand = "left"

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = "right"

    print(solution(numbers, hand))
