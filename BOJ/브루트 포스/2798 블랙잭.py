
# 각 카드에는 양의 정수가 쓰여있다.
# N장을 보이고, 숫자 M을 크게 외침
# 플레이어가 3장을 고름
# 합이 M보다 작거나 같도록 만들어야함

# 입력 카드의 개수, M값
N, M = map(int, input().split())

# 카드의 종류
card = list(map(int, input().split())) # card = [5, 6, 7, 8, 9]

# 구현
total = 0
for i in range(N - 2):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            temp = card[i] + card[j] + card[k]

            if temp >= total and temp <= M:
                total = temp
            
# 출력 
print(total)