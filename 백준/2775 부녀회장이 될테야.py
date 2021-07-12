# 2775.py

'''
.   0   1   2   3   4   5 ..
4   1   6   21  56  116
3   1   5   15  35  60
2   1   4   10  20  25
1   1   3   6   10  15
0   1   2   3   4   5 ..
'''

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n + 1)]

    for _ in range(k):
        for j in range(1, n):
            people[j] = people[j] + people[j-1]

    print(people[-1])
