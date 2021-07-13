from itertools import combinations

'''
def solution(numbers):
    answer = []

    for i in list(combinations(numbers, 2)):
        answer.append(i[0] + i[1])

    answer = list(set(answer))
    answer.sort()

    return answer
'''

def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return sorted(list(set(answer)))