from typing import List

## 풀이 1. 람다와 + 연산자를 이용
# 숫자 여부를 판별하기 위한 isdigit() 사용
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits