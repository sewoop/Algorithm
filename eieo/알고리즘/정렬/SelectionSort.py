# 선택 정렬
def selectionSort(data):
    for i in range(len(data)-1): # O(n)
        index = i
        for j in range(i+1, len(data)):
            if data[j] < data[index]:
                index = j

        if index != i:
            data[i], data[index] = data[index], data[i]
    return data

def shortSelectionSort(data):
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[j] < data[i]:
                data[i], data[j] = data[j], data[i]
    return data

if __name__ == "__main__":
    data = [5,8,2,6,1,4,3,7]
    # data = [5,5,4,1,1,2,2,3]

    # print(selectionSort(data))
    print(shortSelectionSort(data))