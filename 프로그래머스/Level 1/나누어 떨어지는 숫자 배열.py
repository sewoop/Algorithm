# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    if len(arr) >=1:
        for i in arr:
            if i%divisor == 0 :
                answer.append(i)
        if not answer:
            answer.append(-1)
        answer = sorted(answer)
        return answer