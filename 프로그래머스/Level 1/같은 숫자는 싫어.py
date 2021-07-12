# 같은 숫자는 싫어
def solution(arr):
    lists, p, i = [], None, 0
    for i in arr:
        if p != i:
            lists.append(i)
        p = i
    answer = lists
    return answer
