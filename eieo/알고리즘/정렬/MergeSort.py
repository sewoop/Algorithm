# 병합 정렬
def mergeSortAscending(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    leftList = data[:mid]
    rightList = data[mid:]

    leftList = mergeSortAscending(leftList)
    rightList = mergeSortAscending(rightList)

    return mergeAscending(leftList, rightList)

def mergeAscending(left, right):
    result = []

    # [1,3,4,5] [2,7,8,9]
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
            
    return result
        
def mergeSortDescending(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    leftList = data[:mid]
    rightList = data[mid:]

    leftList = mergeSortDescending(leftList)
    rightList = mergeSortDescending(rightList)

    return mergeDescending(leftList, rightList)

def mergeDescending(left, right):
    result = []

    # [1,3,4,5] [2,7,8,9]
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] >= right[0]: # 이것만 변경하면 오름차순 내림차순 변경가능
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
            
    return result
if __name__ == "__main__":
    data = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

    print(mergeSortAscending(data))
    print(mergeSortDescending(data))