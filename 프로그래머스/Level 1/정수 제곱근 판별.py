import math

def solution(n):
    if math.sqrt(n).is_integer():
        answer = pow(int(math.sqrt(n)+1),2)
    else:
        answer = -1

    return answer


if __name__ == "__main__":
    n = 3
    print(solution(n))