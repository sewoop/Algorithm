# 힙 정렬
def heapify(unsorted, index, heapSize):
    largest = index
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2

    if leftIndex < heapSize and unsorted[leftIndex] > unsorted[largest]:
        largest = leftIndex
    
    if rightIndex < heapSize and unsorted[rightIndex] > unsorted[largest]:
        largest = rightIndex

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heapSize)

def heapSort(unsorted):
    n = len(unsorted)
    # build max heap
    # 배열의 중간부터 시작하면 이진트리 성질에 의해 모든 요소 값을 서로 한번씩 비교할 수 있개 됨 : O(n)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
        
    # recurrent
    # O(nlogn)
    # max heap 이므로 맨 꼭대기를 뒤로 보내 차곡차곡 쌓으면 오름차순이 됨

    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)

    return unsorted


if __name__ == "__main__":
    data = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print(heapSort(data))