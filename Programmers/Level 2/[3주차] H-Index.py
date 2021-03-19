def solution(citations):
    citations.sort(reverse=True)
    
    answer = 0
    for n, h in zip(citations, range(1, len(citations) + 1)):
        # print(n, h)
        if n == h:
            answer = h
            break
        elif n < h:
            answer = h - 1
            break
        else:
            if len(citations) == h:
                answer = h
                break
    return answer

# H-Index
'''
    인용 수    논문 수
        47    1
        42    2
        32    3
        28    4
        24    5
        22    6
        17    7
        15    8
        10    9
        10    10 <- 같아지거나, 인용수가 논문 수보다 작아지는 지점이 H이다.
        8     11
'''


# print(solution([3, 0, 6, 1, 5]))
# print(solution([47, 42, 32, 28, 24, 22, 17, 15, 12, 11, 8]))