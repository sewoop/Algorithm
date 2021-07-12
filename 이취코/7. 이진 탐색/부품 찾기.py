n = int(input())  # 재고 부품 개수
parts = list(map(int, input().split()))  # 재고 부품 종류

m = int(input())  # 주문 부품 개수
orders = list(map(int, input().split()))  # 주문 부품 종류

parts.sort()  # 이진 탐색을 위해 오름차순 정렬


def binary_search(target, parts):
    left, right = 0, len(parts) - 1  # left, right 생성 (배열의 양쪽)

    while left <= right:  # left와 right가 교차하지 않는 범위내에서 진행
        mid = (left + right) // 2  # 중간 값을 갱신

        if parts[mid] == target:  # 부품의 중간값과 타겟이 같으면 True을 리턴
            return True
        elif parts[mid] > target:  # 타겟보다 크면 중간값보다 작은 범위에서 다시 찾기 위해 조정
            right = mid - 1
        else:
            left = mid + 1  # 타겟보다 작으면 중간값보다 큰 범위에서 다시 찾기 위해 조정

    return False


result = []
for target in orders:
    if binary_search(target, parts):
        result.append('yes')
    else:
        result.append('no')

print(*result)

'''
5
8 3 7 9 2
3
5 7 9
'''
