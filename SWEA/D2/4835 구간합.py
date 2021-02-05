# 0.14217s
Ts = int(input())

for T in range(1, Ts+1):
    N, M = map(int, input().split())
    number_lst = list(map(int, input().split()))
    
    sum_lst = []
    for i in range(N-M+1):
        sum_lst.append(sum(number_lst[i:i+M]))

    sum_lst = sorted(sum_lst)
    minimum = sum_lst[0]
    maximum = sum_lst[-1]

    # print(minimum, maximum)
    print(f'#{T} {maximum-minimum}')


# 0.15570s
# Ts = int(input())

# for T in range(1, Ts+1):
#     N, M = map(int, input().split())
#     number_lst = list(map(int, input().split()))

#     minimum = 999999999
#     maximum = 0
#     temp = 0
#     for i in range(N-M+1):
#         # max 추출
#         if maximum < sum(number_lst[i:i+M]):
#             maximum = sum(number_lst[i:i+M])

#         if minimum > sum(number_lst[i:i+M]):
#             minimum = sum(number_lst[i:i+M])

#     # print(minimum, maximum)
#     print(f'#{T} {maximum-minimum}')