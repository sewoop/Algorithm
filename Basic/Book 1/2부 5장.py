# Python (PEP 8) : D-13 (전기기사)

## 리스트 (List) : 순서대로 저장하는 시퀀스이자 변경 가능한 목록 Mutable List이다. (내부적으로는 동적 배열로 구현되어 있다.)
# 리스트의 시간 복잡도
'''
    O(1):
        len(a)
        a[i]
        a.append(element)
        a.pop()
    
    O(k):
        a[i:j]
    
    O(n):
        element in a
        a.count(element)
        a.index(element)
        a.pop(0)
        del a[i]
        min(a), max(a)
        a.reverse()
    
    O(nlogn):
        a.sort() : Timsort
'''

# IndexError 처리
try:
    print(a[9])
except IndexError:
    print('존재하지 않는 인덱스')

# remove()를 사용하면 특정 값의 요소를 지울 수 있다.


## 딕셔너리 (Dict) : 3.7+에서는 입력 순서가 유지된다.
# 딕셔너리 시간 복잡도
'''
    O(1):
        len(a)
        a[key]
        a[key] = value
        key in a
'''
# 3.6이하는 입력 순서가 유지되지 않으므로 다음과 같은 별도의 자료형을 사용한다.
from collections import OrderedDict, Counter, defaultdict

# KeyError 처리
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

# 딕셔너리 삭제 방법
del a['key1']


## 딕셔너리 모듈
# defaultdict 객체
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4

a['C'] += 1  # 해당 키 값이 없으면 0을 디폴트로 하여 생성 후 1을 더해서 자동 생성한다.

# Counter 객체
a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)
b  # Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})

# Counter 객체에서 가장 빈도 수가 높은 요소를 추출하는 방법 :
b.most_common(2)  # 가장 빈도 수가 높은 요소 2가지를 보여준다.

# OrderDict 객체 : 3.7+ 에서는 입력 순서가 유지되므로 사용하지 않지만, 3.6이하에서는 사용하였다.
