# 1181 단어 정렬

import sys

def wordSort(data):
    data = list(set(data))
    data.sort(key=lambda x: (x[1], x[0]))
    data = [i.replace('\n','') for i, v in data]
    return data

n = int(input())
data = []

for _ in range(n):
    temp = sys.stdin.readline()
    data.append((temp, len(temp)))

for i in wordSort(data):
    print(i)