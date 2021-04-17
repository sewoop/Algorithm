# 크루스칼을 사용
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

def solution(n, costs):
    answer = 0

    parent = [i for i in range(n)] # [0, 1, 2, 3]
    costs.sort(key=lambda x: x[2])
    
    for cost in costs:
        a, b, c = cost

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += c

    return answer

if __name__ == "__main__":
    n, costs = 4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(n, costs))