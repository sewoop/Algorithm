# 삽입 정렬
def insertionSort(data):
    for i in range(1, len(data)):
        index = i - 1
        keyValue = data[i]
        
        while data[index] > keyValue and index>=0:
            data[index + 1] = data[index]
            index -= 1
        
        data[index + 1] = keyValue
        
    return data

if __name__ == "__main__":
    data = [5,8,2,6,1,4,3,7]

    print(insertionSort(data))