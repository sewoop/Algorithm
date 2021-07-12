def shellSort(array):
    gap = len(array) // 2

    # gap이 짝수 값이면 홀수로 변경 해줌
    if gap != 0 and gap % 2 == 0:
        gap += 1
        
    while gap > 0: # gap이 0보다 클 동안 반복
        for start_pos in range(gap):
            insertion(array, start_pos, gap) # 배열, 시작 값, 간격을 넣어서 삽입 정렬을 돌림
        gap //= 2

        # gap이 짝수 값이면 홀수로 변경 해줌
        if gap != 0 and gap % 2 == 0:
            gap += 1

    return array

def insertion(array, start_pos, gap):
    for i in range(start_pos + gap, len(array), gap):
        index = i - gap
        key = array[i] # key값을 고름 

        while key < array[index] and index >= 0: # 조건을 만족하는. 즉, key보다 큰 값을 가지는 앞의 값을 뒤로 보내는 과정
            array[index + gap] = array[index]
            index -= gap

        array[index + gap] = key # 뒤로 더이상 보낼 수 없을 때, key 삽입

array = [10, 8, 6, 20, 4, 3, 22, 1, 0, 15, 16]
print(shellSort(array))