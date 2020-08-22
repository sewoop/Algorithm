from typing import List
from collections import Counter
import re

## 풀이 1. List comprehension, Counter 객체 사용
# 정규식에서 \w 는 단어 문자를 뜻하며, ^은 not을 의미한다.
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]','', paragraph).lower().split() if word not in banned]

    counts = Counter(words)
    # 가장 흔하게 등장하는 단어의 첫번째 인덱스 리턴
    return counts.most_common(1)[0][0]
