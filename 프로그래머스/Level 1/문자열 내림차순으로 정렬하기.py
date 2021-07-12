def solution(s):
    answer = ''
    return answer.join(sorted(s, reverse=True))


if __name__ == "__main__":
    # s = "Zbcdefg"
    s = "AbCdEfg"
    print(solution(s))
