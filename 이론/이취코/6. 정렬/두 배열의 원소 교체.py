n, k = map(int, input().split())

lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))

# 내 풀이
# for _ in range(k):
#     index_a = lst_a.index(min(lst_a))
#     index_b = lst_b.index(max(lst_b))
#     lst_a[index_a], lst_b[index_b] = lst_b[index_b], lst_a[index_a]

# 정렬 (문제가 원하는 방법)
lst_a.sort()
lst_b.sort(reverse=True)

for i in range(k):
    if lst_a[i] < lst_b[i]:
        lst_a[i], lst_b[i] = lst_b[i], lst_a[i]
    else:
        break

print(sum(lst_a))

'''
5 3
1 2 5 4 3
5 5 6 6 5
'''
