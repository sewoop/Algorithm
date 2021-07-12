# 10814 나이순 정렬

# def ageSort(data):
#     data.sort(key=lambda x: (x[0], x[2]))
#     return data


# n = int(input())
# data = []

# for i in range(n):
#     age, name = map(str, input().split())
#     data.append((int(age), name, i))

# for i in ageSort(data):
#     print(f'{i[0]} {i[1]}')

# --- sys
import sys
# 10814 나이순 정렬


def ageSort(data):
    data.sort(key=lambda x: (x[0], x[2]))
    return data


n = int(input())
data = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    data.append((int(age), name, i))

for i in ageSort(data):
    print(f'{i[0]} {i[1]}')
