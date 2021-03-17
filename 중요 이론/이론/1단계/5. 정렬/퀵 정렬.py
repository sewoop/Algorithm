def quickSort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left, center, right = [], [], []

    for arr in array:
        if arr < pivot:
            left.append(arr)
        elif arr > pivot:
            right.append(arr)
        else:
            center.append(arr)

    return quickSort(left) + center + quickSort(right)


array = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(quickSort(array))