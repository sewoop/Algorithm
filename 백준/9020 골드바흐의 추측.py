def Prime(end):
    prime_list = [0] * (end + 1)
    m = int(end ** 0.5)
    for i in range(2, m + 1):
        if prime_list[i] == 0:
            j = 2
            while i * j <= end:
                prime_list[i * j] = 1
                j += 1

    # # Method 2
    # prime_list = [0 for i in range(10001)]
    # prime_list[1] = 1
    # for i in range(2, 98):
    #     for j in range(i * 2, 10001, i):
    #         prime_list[j] = 1

    return prime_list


def GoldbaPrime(data, num):
    b = num // 2
    for j in range(b, 1, -1):
        if data[num - j] == 0 and data[j] == 0:
            print(j, num - j)
            break


T = int(input())

data = Prime(10001)  # 큰 데이터는 여러번 생성하지 않도록 따로 빼놓을 것
for _ in range(T):
    num = int(input())
    GoldbaPrime(data, num)
