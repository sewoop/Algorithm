# 땅따먹기
def solution(land):
    for i in range(1,len(land)):
        temp = land[i-1][:]
        for j in range(len(land[0])):
            land[i][j] += max(temp[:j] + temp[j+1:])

    return max(land[-1])