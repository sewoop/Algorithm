from collections import defaultdict

def dfs(root):
    global count
    count += 1

    for i in tree[root]:
        dfs(i)

ts = int(input())

for t in range(1, ts + 1):
    E, N = map(int, input().split())

    # Tree 구조 생성
    temp = [int(i) for i in input().split()]
    tree = defaultdict(list)

    for i in range(0, E*2, 2):
        tree[temp[i]].append(temp[i+1])
    
    # dfs
    count = 0
    dfs(N)

    print(f'#{t} {count}')

