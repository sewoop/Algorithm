def solution():
    n = int(input())

    data = []
    for _ in range(n):
        name, score = input().split()
        data.append((name, int(score)))

    data.sort(key=lambda x: x[1])

    result = []
    for i in data:
        result.append(i[0])

    return result


print(*solution())

'''
2
홍길동 95
이순신 77
'''
