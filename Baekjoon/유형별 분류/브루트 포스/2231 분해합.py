# 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합
# ex) 256 = 245 + 2 + 4 + 5 -> 245는 256의 생성자
# 없으면 0 출력

N = int(input())
answer = 0

# def partitionSum(num): # 245
#     part = []

#     while num != 0:
#         part.append(num % 10) # 2
#         num = num // 10

#     return sum(part)

for i in range(N // 2, N + 1): # N // 2 + N // 4 부터 시작할 시 8을 넣으면 4 + 1이 되어 4+4 = 8의 경우를 못 발견함
    temp = sum(map(int, str(i)))

    if temp + i == N:
        answer = i
        break

print(answer)
