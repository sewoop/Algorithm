n, m = map(int, input().split()) # 떡의 개수, 원하는 잘린 떡의 합
rice_cake = list(map(int, input().split()))

rice_cake.sort() # [10, 15 17 19]

result = 0 # 결과
left, right = 0, max(rice_cake) # 양쪽 끝을 나타냄
while left <= right: # left가 right 작거나 같은 상황에서
    temp = 0 # 임시 잘린 떡의 합
    mid = (left + right) // 2 # 중간 높이

    for rice in rice_cake: # 잘린 떡의 합을 계산하는 반복문
        if rice - mid > 0:
            temp += (rice - mid)

    if temp < m: # 만약, 잘린 떡의 합이 목표치보다 작으면
        right = mid - 1 # 우측 인덱스를 중간값보다 1 작은 값으로 초기화
    else:
        result = mid # 잘린 떡의 합이 목표치보다 크거나 같으면 결과치에 저장
        left = mid + 1 # 좌측 인덱스를 중간값보다 1 큰 값으로 초기화

print(result)
    
'''
4 6
19 15 10 17
'''