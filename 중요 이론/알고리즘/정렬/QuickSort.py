# 퀵 정렬
def quickSortSimple(lst):
    if len(lst) <= 1: return lst
    pivot = lst[len(lst) // 2]
    lessArr, equalArr, bigArr = [], [], []

    for i in lst:
        if i < pivot: lessArr.append(i)
        elif i > pivot: bigArr.append(i)
        else: equalArr.append(i)

    return quickSortSimple(lessArr) + equalArr + quickSortSimple(bigArr)


# L은 pivot보다 큰 수가 발견되어야지 멈춘다. 즉, 0번 인덱스에서 멈출 수 없기 때문에 좀떠 빨리 하기 위해 1부터 시작
# L는 오른쪽, R는 왼쪽으로 값을 찾는다.
# 교차하지 않으면 위치한 원소값만을 교환한다.
# 교차하면 R의 값과 pivot의 값을 교환한다.

def partitionAscend(data, start, end):
    pivot = data[start]
    L, R = start, end

    while True:
        while L <= len(data)-1 and data[L] <= pivot:
            L += 1
        while R >= 0 and data[R] > pivot:
            R -= 1
        if R <= L:
            data[start], data[R] = data[R], data[start]
            break
        else:
            data[L], data[R] = data[R], data[L]

    return R

def partitionDescend(data, start, end):
    pivot = data[start]
    L, R = start, end

    while True:
        while L <= len(data)-1 and data[L] >= pivot:
            L += 1
        while R >= 0 and data[R] < pivot:
            R -= 1
        if R <= L:
            data[start], data[R] = data[R], data[start]
            break
        else:
            data[L], data[R] = data[R], data[L]

    return R

def quickSortAscend(data, start, end):
    if start < end:
        pivot = partitionAscend(data, start, end)
        quickSortAscend(data, start, pivot - 1)
        quickSortAscend(data, pivot + 1, end)

    return data

def quickSortDescend(data, start, end):
    if start < end:
        pivot = partitionDescend(data, start, end)
        quickSortDescend(data, start, pivot - 1)
        quickSortDescend(data, pivot + 1, end)

    return data

# 퀵소트 복습
# L R -> 찾음 
# 교차하면 R과 pivot을 변경
# 반복

def partitionReview(data, start, end):
    pivot, L, R = data[start], start, end

    while True:
        while L <= len(data)-1 and data[L] <= pivot:
            L += 1
        
        while R >= 0 and data[R] > pivot:
            R -= 1
        
        if R <= L:
            data[start], data[R] = data[R], data[start]
            break
        else:
            data[L], data[R] = data[R], data[L]
    return R

def quickSortReview(data, start, end):
    if start < end:
        pivot = partitionReview(data, start, end)
        quickSortReview(data, start, pivot - 1)
        quickSortReview(data, pivot + 1, end)

    return data


if __name__ == "__main__":
    data = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    print(len(data))
    # print(quickSortAscend(data, 0, len(data) - 1))
    # print(quickSortDescend(data, 0, len(data) - 1))
    print(quickSortReview(data, 0, len(data) - 1))
    