# x kg, y cm => (x, y)
# A, B = (x, y), (p, q)

N = int(input())
rank = []
answer = []

for _ in range(N):
    m, n = map(int, input().split())
    rank.append([m, n])

for i in range(N):
    store = 1
    for j in range(N):
        if rank[i][0] < rank[j][0] and rank[i][1] < rank[j][1]:
            store += 1

    answer.append(str(store))

print(' '.join(answer))
