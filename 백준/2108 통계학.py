# 2108 통계학
import sys
import collections

# 산술 평균


def mean(data):
    return round(sum(data) / len(data))

# 중앙 값


def median(data):
    data.sort()
    return data[len(data) // 2]

# 최빈 값


def many(data):
    dic = collections.Counter(data)
    dic_common = dic.most_common()

    if len(data) > 1:
        if dic_common[0][1] == dic_common[1][1]:
            many_value = dic_common[1][0]
        else:
            many_value = dic_common[0][0]
    else:
        many_value = dic_common[0][0]

    return many_value

# 범위


def scope(data):
    return max(data) - min(data)


# N : 홀수
n = int(sys.stdin.readline())

data = []

for _ in range(n):
    data.append(int(sys.stdin.readline()))

print(mean(data))
print(median(data))
print(many(data))
print(scope(data))
