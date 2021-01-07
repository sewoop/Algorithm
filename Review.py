''' Review 01
import time

def timeWrapper(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(f'#time: {round(end - start, 4)}s')
        return value
    return wrapper

# 에라스토텔레스의 체
@timeWrapper
def Prime(start, end):
        # 2부터 시작하여 배수를 모두 False
        # end 까지
    prime_list = [True for _ in range(end + 1)] # 0 - end까지의 True 배열

    for i in range(2, end + 1):
        if prime_list[i] == True:
            j = 2
            while i * j <= end:
                prime_list[i * j] = False
                j += 1 

    prime_list[0], prime_list[1] = False, False
    for i in range(start, end + 1):
        if prime_list[i]:
            print(i, end=' ')
    print()

@timeWrapper
def PrimeFast(start, end):
    prime_list = [True] * (end + 1) # 0 - end까지의 True 배열
    m = int(end ** 0.5)
    for i in range(2, m + 1):
        if prime_list[i] == True:
            j = 2
            while i * j <= end:
                prime_list[i * j] = False
                j += 1 

    print([i for i in range(2, end + 1) if prime_list[i] == True])


# 병합 정렬
def mergeSortAscending(data):
    # data가 들러오면 이를 좌우로 쪼갬
    # 길이가 1보다 작거나 같으면 리턴

    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = mergeSortAscending(data[:mid])
    right = mergeSortAscending(data[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

    return data

def mergeSortDescending(data):
    # data가 들러오면 이를 좌우로 쪼갬
    # 길이가 1보다 작거나 같으면 리턴

    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = mergeSortDescending(data[:mid])
    right = mergeSortDescending(data[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

    return data

# 퀵 정렬
def quickSort(data):
        # pivot을 기준으로 좌우를 나눔
        # pivot은 좌큰 찾, 우 작 찾 교차하면 R을 pivot으로 만들고 나눔

    # pivot을 찾고 partitioning
    def partition(data, start, end):
        pivot = data[start]
        L = start
        R = end





    return data

# 힙 정렬
def heapSort(data):
    return


# 피보나치
## 기본 (재귀)
def fiboRecursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fiboRecursive(n - 1) + fiboRecursive(n - 2)

## DP - Memorization
def fiboMemorization(n):
    if n in memo:
        return memo[n]

    if n == 0:
        memo[n] = 0
        return 0
    if n == 1:
        memo[n] = 1
        return 1

    memo[n] = fiboMemorization(n - 1) + fiboMemorization(n - 2)
    return memo[n]
    
## 행렬
def matrixMul(matA, matB):
    matrix = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                # matrix[i][k] += (matA[i][j] * matB[j][k]) % 1000000007
                matrix[i][k] += (matA[i][j] * matB[j][k])
    return matrix

def fiboMatrix(x):
    base = [[1, 1], [1, 0]]
    matrix = [[1, 1], [1, 0]]

    for _ in range(x): # n이 0, 1이면 실행 안함
        matrix = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    # matrix[i][k] += (base[i][j] * base[j][k]) % 1000000007
                    matrix[i][k] += (base[i][j] * base[j][k])
        base = matrix

    return matrix


if __name__ == "__main__":
    Prime(1, 101)   #time: 0.0001s
    PrimeFast(1, 101)   #time: 0.0s
    print(mergeSortAscending([1,3,4,7,2,5,9,6,8,10]))
    print(mergeSortDescending([1,3,4,7,2,5,9,6,8,10]))


    n = 900
    # start = time.time()
    # print(fiboRecursive(n)) # (n == 40): 38.4931s
    # print(f'{round(time.time() - start, 4)}s')
    
    memo = {}
    start = time.time()
    print(fiboMemorization(n)) # (n == 40): 0.0s
    print(f'{round(time.time() - start, 4)}s')

    
    n = bin(n)[2:] # 0b000.. 의 형태이므로 2열부터
    result = [[1, 0], [0, 1]]

    start = time.time()
    for i in range(len(n)):
        if n[-i-1] == '1':
            result = matrixMul(result, fiboMatrix(i))
    # print(result[0][1] % 1000000007)
    print(result[0][1])
    print(f'{round(time.time() - start, 4)}s')

'''

# Review 02 : 백트래킹

def BackTrackingProblem1():

    N, M = map(int, input().split())

    data = [0] * (N + 1)
    isUsed = [0] * (N + 1)

    def BackTracking(index):
        if index == M:
            for i in range(M):
                print(data[i], end=' ')
            print()
            return
        
        for i in range(1, N + 1):
            if isUsed[i] == 1:
                continue

            data[index] = i
            isUsed[i] = 1
            BackTracking(index + 1)
            isUsed[i] = 0

    BackTracking(0)

def BackTrackingProblem2():
    N, M = map(int, input().split())

    data = [0] * (N + 1)
    isUsed = [0] * (N + 1)

    def backTracking(index):
        if index == M:
            for i in range(M):
                print(data[i], end=' ')

            print()
            return

        for i in range(1, N + 1):
            if isUsed[i] == 1:
                continue    
            data[index] = i

            for j in range(i + 1):
                isUsed[j] = 1
            backTracking(index + 1)
            for j in range(1, N + 1):
                isUsed[j] = 0

    backTracking(0)


# BackTrackingProblem1()
BackTrackingProblem2()
