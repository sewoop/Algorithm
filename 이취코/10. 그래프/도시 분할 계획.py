def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

distance = []
for _ in range(m):
    a, b, c = map(int, input().split())
    distance.append((c, a, b))

distance.sort()

last = total = 0
for dist in distance:
    cost, a, b = dist

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += cost
        last = cost

total -= last
print(total)


'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
