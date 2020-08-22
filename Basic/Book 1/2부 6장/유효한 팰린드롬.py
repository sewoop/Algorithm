s = input()

## 풀이 1. 리스트로 변환
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        # isalnum() : 영문자, 숫자 여부를 판별
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


## 풀이 2. Deque 자료형을 이용한 최적화
from collections import deque

def isPalindromeDeque(self, s: str) -> bool:
    # 자료형 Deque 선언
    strs: deque = deque()

    for char in s:
        # isalnum() : 영문자, 숫자 여부를 판별
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


## 풀이 3. 슬라이싱 사용
import re  # 정규 표현식

def isPalindromeSlice(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]  # 슬라이싱