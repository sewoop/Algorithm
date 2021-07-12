# 11650 좌표 정렬하기

def locationSort(data):
    data.sort(key=lambda x: (x[0], x[1]))
    return data


n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split(' '))
    data.append((x, y))

for i in locationSort(data):
    print(f'{i[0]} {i[1]}')
