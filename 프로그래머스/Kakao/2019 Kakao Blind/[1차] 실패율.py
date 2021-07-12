import collections


def solution(N, stages):
    answer = []

    total_user = len(stages)
    fail_percent = {}

    count = collections.Counter(stages)
    # print(count)

    for i in range(N):
        if count[i+1] != 0:
            fail_percent[i+1] = (count[i+1]/total_user)
            # print(f'{count[i+1]}/{total_user}')
            total_user -= count[i+1]
        else:
            fail_percent[i+1] = 0

    # answer = [i[0] for i in sorted(fail_percent.items(), key=lambda x: x[1], reverse=True)]
    answer = sorted(fail_percent, key=lambda x: fail_percent[x], reverse=True)
    return answer


if __name__ == "__main__":
    # N = 5
    # stages = [2, 1, 2, 6, 2, 4, 3, 3]
    # result = [3,4,2,1,5]

    N = 4
    stages = [4, 4, 4, 4, 4]
    result = [4, 1, 2, 3]

    print(solution(N, stages))
