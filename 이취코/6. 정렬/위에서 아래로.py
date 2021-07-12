def solution():
    n = int(input())

    data = []
    for _ in range(n):
        data.append(int(input()))

    data.sort(reverse=True)

    return data


print(*solution())

'''
3
15 
27
12
'''
