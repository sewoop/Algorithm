# 1427 소트인사이드

# 72ms
def sortInside(data):
    data = list(data)
    data.sort(reverse=True)
    return ''.join(data)

# 68ms
def mergeSort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])

    i, j, k = 0, 0, 0

    # descending
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

def sortInsideHandmadeSort(data):
    data = [int(i) for i in list(data)]
    data = mergeSort(data)
    data = [str(i) for i in data]
    return ''.join(data)


data = input()
# print(sortInside(data))
print(sortInsideHandmadeSort(data))