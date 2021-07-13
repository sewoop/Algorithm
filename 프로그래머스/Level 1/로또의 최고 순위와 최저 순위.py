def solution(lottos: list, win_nums: list):
    rank=[6, 6, 5, 4, 3, 2, 1]

    unknown, known = lottos.count(0), 0
    for i in lottos:
        if i in win_nums: known += 1
    
    return [rank[unknown + known], rank[known]]


lottos, win_nums = [44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))