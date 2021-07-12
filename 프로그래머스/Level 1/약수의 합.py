def solution(n):
    answer = 0

    num = set(range(1, n+1))

    for i in range(1, n+1):
        if i in num and n % i == 0:
            answer += i

    return answer


if __name__ == "__main__":
    n = 12
    print(solution(n))
