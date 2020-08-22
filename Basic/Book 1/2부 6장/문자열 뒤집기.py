from typing import List

## 풀이 1. 투 포인터를 이용한 스왑
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

## 풀이 2. 파이썬 방식
def reverseStringPython(self, s: List[str]) -> None:
    s.reverse()