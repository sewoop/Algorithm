# 오름차순 정렬
# data = [5, 4, 3, 2, 1]

# 선택정렬
# 맨 앞자리의 수를 기준
# 오른쪽 수 중 가장 작은 것과 자리를 변경 ( 반복 )

def selectionSort(data):
    for i in range(len(data) - 1):
        minValue = data[i]
        index = i

        for j in range(i, len(data)):
            if data[j] < minValue:
                minValue = data[j]
                index = j

        data[i], data[index] = data[index], data[i]

    return data


if __name__ == "__main__":
    n = int(input())
    data = []

    for _ in range(n):
        data.append(int(input()))

    for i in selectionSort(data):
        print(i)
