# def Prime(end):
#     prime_list = [1] * (end + 1)
#     result = []

#     prime_list[0], prime_list[1] = 0, 0

#     for i in range(2, end + 1):
#         if prime_list[i] == 1:
#             j = 2
#             while i * j <= end:
#                 prime_list[i * j] = 0
#                 j += 1
#             result.append(i)

#     return result

# N = int(input())

# prime = Prime(N)

# for i in prime:
#     while N % i == 0:
#         print(i)
#         N //= i

N = int(input())

i = 2
while N != 1:
    if N % i == 0:
        N = N // i
        print(i)
    else:
        i += 1
