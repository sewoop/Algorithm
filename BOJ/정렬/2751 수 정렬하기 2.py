# 오름차순 정렬
# 병합 정렬
def mergeSort(data):
    if len(data) <= 1: # 원소가 하나, 없으면 반환
        return data

    mid = len(data) // 2 # 중간 값 mid
    # mid를 중점으로 자름
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])

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

if __name__ == "__main__":
    data = [5, 4, 3, 2, 1]
    print(mergeSort(data))

    # n = int(input())
    # data = []
    # for _ in range(n):
    #     data.append(int(input()))
    
    # for i in mergeSort(data):
    #     print(i)