def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]


def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)

    if a < b:
        team[b] = a
    else:
        team[a] = b


n, m = map(int, input().split())

team = [i for i in range(n + 1)]

for _ in range(m):
    op, a, b = map(int, input().split())

    if op:
        if find_team(team, a) == find_team(team, b):
            print('YES')
        else:
            print('NO')
    else:
        union_team(team, a, b)

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''
