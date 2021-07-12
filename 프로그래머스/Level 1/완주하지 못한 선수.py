# 효율성 문제 발생
import collections


def solution(participant, completion):
    for comp in completion:
        index = participant.index(comp)
        participant.pop(index)

    return ''.join(participant)


# Collections 사용


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


if __name__ == "__main__":
    # participant = ['leo', 'kiki', 'eden']
    # completion = ['eden', 'kiki']

    # participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
    # completion = ['josipa', 'filipa', 'marina', 'nikola']

    participant = ['mislav', 'stanko', 'mislav', 'ana']
    completion = ['stanko', 'ana', 'mislav']
    print(solution(participant, completion))
