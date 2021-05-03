def check(yellow):
    result = []
    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            result.append((i, yellow // i))        
    return result

def solution(brown, yellow):
    answer = []
    lsts = check(yellow) # (높이, 너비)
    for h, w in lsts:
        if (h + 2) * (w + 2) - (h * w) == brown:
            answer = [(w + 2), (h + 2)]
            break

    return answer

## 다른 사람 풀이
import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]

brown, yellow = 10, 2
# brown, yellow = 8, 1
# brown, yellow = 24, 24

print(solution(brown, yellow))