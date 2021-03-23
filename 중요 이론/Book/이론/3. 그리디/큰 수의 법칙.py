# 내 풀이
def my_solution(): # [2, 4, 5, 4, 6]
    N, M, K = map(int, input().split())
    numbers = [int(i) for i in input().split()]

    numbers.sort()

    maximum = numbers[N - 1]
    next_maximum = numbers[N - 2]

    total = 0
    for i in range(1, M + 1):
        if i % K == 0:
            total += next_maximum
        else:
            total += maximum
    
    return total


# 책 풀이 1.
def book_solution_1():
    # N, M, K를 공백으로 구분하여 입력 받기
    n, m, k = map(int, input().split())

    # N개의 수를 공백으로 구분하여 입력 받기
    data = list(map(int, input().split()))

    data.sort() # 입력 받은 수를 정렬
    first = data[n - 1] # 가장 큰수
    second = data[n - 2] # 두 번째로 큰수

    result = 0
    
    while True:
        for i in range(k): # 가장 큰 수를 K번 더하기
            if m == 0: # m이 0이라면 반복 탈출
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1
    
    return result

# 책 풀이 2
def book_solution_2():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort()

    first = data[n - 1]
    second = data[n - 2]

    count = int(m / (k + 1)) * k # 가장 큰 수가 등장하는 갯수
    count += m % (k + 1)
    
    result = 0 
    result += (count) * first
    result += (m - count) * second

    return result


if __name__ == '__main__':
    print(my_solution())
    print(book_solution_1())
    print(book_solution_2())


'''
5 8 3
2 4 5 4 6
'''