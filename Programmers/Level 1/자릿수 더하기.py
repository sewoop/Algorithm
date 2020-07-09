def solution(n):
    answer,k = 0, str(n)
    for i in range(len(k)) :
        answer+=int(k[i])

    return answer