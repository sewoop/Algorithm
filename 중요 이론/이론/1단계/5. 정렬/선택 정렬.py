def selectionSort(array):
    for i in range(len(array) - 1):

        # 파이썬 min 내장 함수와 index 함수를 이용한 방법
        # minimum = min(array[i + 1:])
        # index = array.index(minimum)

        # 직접 구현한 방법
        min_idx = i # 최소값의 인덱스
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]: # 비교하여 뒤가 더 작으면
                min_idx = j # 뒤의 인덱스 번호를 최소값의 인덱스로 갱신

        array[min_idx], array[i] = array[i], array[min_idx] # Swap

    return array

array = [9, 6, 7, 3, 5]
print(selectionSort(array))