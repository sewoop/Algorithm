from itertools import permutations

# 내 풀이


def make_numbers(numbers):
    result = set()
    for i in range(len(numbers)):
        result |= set(map(int, map("".join, permutations(numbers, i + 1))))
    return result


def solution(numbers):
    answer = 0

    n = int('9' * len(numbers))

    prime = [1] * (n + 1)
    prime[0] = prime[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = 0

    numbers = make_numbers(numbers)

    for number in numbers:
        if prime[number]:
            answer += 1

    return answer

# 다른 사람 풀이


def solution_short(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


numbers = "17"
# numbers = "011"
print(solution(numbers))
