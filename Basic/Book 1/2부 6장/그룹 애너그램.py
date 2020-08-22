
'''
    애너그램 이란,
    문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
'''

from typing import List
from collections import defaultdict

## 풀이 1. 정렬하여 딕셔너리에 추가
def groupAnagrams(self, strs: List[str]) -> List[str]:
    anagrams = defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()