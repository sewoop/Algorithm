ts = int(input())

def Tree(n):
    global count
    
    if n <= N:
        Tree(n*2)
        tree[n] = count
        count += 1
        Tree(n*2 + 1)

for t in range(1, ts + 1):
    N = int(input())

    tree = [0]*(N+1)
    count = 1
    Tree(1)

    print(tree)
    print(f'#{t} {tree[1]} {tree[N//2]}')
