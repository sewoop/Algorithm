# 나의 풀이
def my_solution():
    n, m = map(int, input().split())

    result = 0
    for _ in range(n):
        data = list(map(int, input().split()))

        temp_minimum = min(data)
        if result < temp_minimum:
            result = temp_minimum

    return result

# 책 풀이 1
def book_solution_1():
    n, m = map(int, input().split())

    result = 0
    for _ in range(n):
        data = list(map(int, input().split()))

        min_value = min(data)

        result = max(result, min_value)

    return result

# 책 풀이 2
def book_solution_2():
    n, m = map(int, input().split())

    result = 0

    for _ in range(n):
        data = list(map(int, input().split()))

        min_value = 10001

        for a in data:
            min_value = min(min_value, a)
        
        result = max(result, min_value)

    return result

if __name__ == '__main__':
    print(my_solution())
    print(book_solution_1())
    print(book_solution_2())

'''
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
'''