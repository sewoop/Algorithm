# 버블 정렬
def BubbleSort(data):
    length = len(data) - 1
    for i in range(length):
        for j in range(length-i): # -i의 이유 bubble sort는 한번 진행하면 맨 끝의 값이 최대가 되므로 더이상 해줄 필요가 없다.
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    
    return data

if __name__ == "__main__":
    data = [5,8,2,6,1,4,3,7]

    print(BubbleSort(data))