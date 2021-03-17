def bubbleSort(array):
    for i in range(len(array) - 1): # 뒤로 맞춰져야하는 것이 리스트의 크기의 -1한 값이다.
        for j in range(len(array) - 1 - i): # 1회전마다 맨 끝의 값은 최댓값이 되므로 더이상 안해줘도 된다. 
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array = [7, 4, 5, 1, 3]
print(bubbleSort(array))