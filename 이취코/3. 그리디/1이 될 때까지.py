# 내 풀이
def my_solution():
    n, k = map(int, input().split())

    count = 0
    while True:
        if n == 1:
            break
        if n % k == 0:
            n //= k
        else:
            n -= 1
        count += 1

    return count

# 책 풀이 1


def book_solution_1():
    n, k = map(int, input().split())

    result = 0
    while n >= k:
        while n % k != 0:
            n -= 1
            result += 1
        n //= k
        result += 1
    while n > 1:
        n -= 1
        result += 1

    return result

# 책 풀이 2


def book_solution_2():
    n, k = map(int, input().split())

    result = 0
    while True:
        target = (n // k) * k  # N이 K로 나누어 떨어지는 수를 찾고 그 수를 타겟으로 한다.
        result += (n - target)  # N에 타겟만큼을 뺀 값의 값이 1을 뺄 횟수가 되는 것이다.

        n = target
        if n < k:
            break

        result += 1  # N을 K로 나누고 횟수 추가
        n //= k

    return result - 1  # 남은 수에 대해 1을 뺀다.


if __name__ == '__main__':
    print(my_solution())
    print(book_solution_1())
    print(book_solution_2())
