def solution(n):
    answer = ''
    base = '수박'

    for i in range(n):
        answer += base[i % 2]
    return answer


if __name__ == "__main__":
    n = 4

    print(solution(n))
