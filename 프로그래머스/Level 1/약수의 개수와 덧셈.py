'''
def solution(left, right):
    def nod(x):
        res = []
        for i in range(1, x + 1):
            if x % i == 0:
                res.append(i)
        return len(res)

    answer = 0
    for i in range(left, right + 1):
        if nod(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
'''

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer


solution(13, 17)