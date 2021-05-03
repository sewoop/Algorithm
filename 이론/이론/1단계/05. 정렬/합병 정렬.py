def mergeSort(data):
    # 분할
    if len(data) <= 1:
        return data

    # 중심을 기점으로 좌/우로 분할한다.
    mid = len(data) // 2
    leftList = mergeSort(data[:mid])
    rightList = mergeSort(data[mid:])

    # 정복 (결합)
    result = merge(leftList, rightList) # 반환 받은 정렬된 리스트를 합친다.

    return result

def merge(left, right):
    result = [] # 빈 리스트를 생성하고

    while len(left) > 0 or len(right) > 0: # 좌/우 리스트가 한개 이상 존재하는 상황일 때,
        if len(left) > 0 and len(right) > 0: # 만약, 둘다 존재하면
            if left[0] < right[0]: # 좌/우를 비교해서 더 작은 값을
                result.append(left[0]) # 빈 리스트에 넣어주고 갱신한다.
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:] 
        elif len(left) > 0: # 만약, 좌만 존재할 경우
            result.append(left[0])
            left = left[1:]

        elif len(right) > 0: # 만약, 우만 존재할 경우
            result.append(right[0])
            right = right[1:]
    return result # 정렬 후 결합된 결과 리스트를 반환한다.

data = [21, 10, 12, 20, 25, 13, 15, 22]
print(mergeSort(data))