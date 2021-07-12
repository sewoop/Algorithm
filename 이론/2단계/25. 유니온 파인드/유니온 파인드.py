# 특정 원소가 속한 집합을 찾기
"""
'''
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
'''

# find 최적화 (경로 압축)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 : union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력 : find_parent를 한번 더 돌려서 조상을 찾아서 갱신해줌
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

'''
6 4
1 4
2 3
2 4
5 6
'''
"""

# 유니온 파인드 복습
# find
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

v, e = map(int, input().split())

# parent 초기화
parent = [i for i in range(v + 1)]

# 그래프 생성 및 초기화
graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 조상 부모 최종 갱신
for i in range(1, v + 1):
    find_parent(parent, i)

print(*parent[1:])

'''
6 4
1 4
2 3
2 4
5 6
'''