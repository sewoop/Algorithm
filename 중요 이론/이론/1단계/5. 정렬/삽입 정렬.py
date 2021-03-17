def insertionSort(array):
    for i in range(1, len(array)):
        index = i - 1
        key = array[i] # key값을 고름 

        while key < array[index] and index >= 0: # 조건을 만족하는. 즉, key보다 큰 값을 가지는 앞의 값을 뒤로 보내는 과정
            array[index + 1] = array[index]
            index -= 1

        array[index + 1] = key # 뒤로 더이상 보낼 수 없을 때, key 삽입 

    return array

array = [8, 5, 6, 2, 4]
print(insertionSort(array))