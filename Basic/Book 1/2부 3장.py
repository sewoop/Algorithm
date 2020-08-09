# Python (PEP 8) : D-13 (전기기사)

## 인덴트
foo = long_function_name(var_one, var_two, 
                         var_three, var_four)

def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

foo = long_function_name(
    var_one, var_two,
    var_three, var_four)


## 네이밍 컨벤션 (Naming Convention)
# 파이썬은 _로 표기하는 스네이크 케이스 Snake Case를 따른다.


## 타입 힌트
import typing
a: str = '1'
b: int = 1

def fn(a: int) -> bool:  # 파라미터 값은 int, 리턴 값은 bool값
    pass

# pip install mypy : mypy를 사용하여 타입 힌트에 오류가 없는지 자동으로 확인할 수 있다.
# mypy solution.py
'''
(base) lingo@Lingoui-MacBookPro Book 1 % mypy 2부\ 3장.py
2부 3장.py:2: error: Name 'var_one' is not defined
2부 3장.py:2: error: Name 'var_two' is not defined
2부 3장.py:3: error: Name 'var_three' is not defined
2부 3장.py:3: error: Name 'var_four' is not defined
2부 3장.py:11: error: Name 'var_one' is not defined
2부 3장.py:11: error: Name 'var_two' is not defined
2부 3장.py:12: error: Name 'var_three' is not defined
2부 3장.py:12: error: Name 'var_four' is not defined
Found 8 errors in 1 file (checked 1 source file)
'''


## 리스트 컴프리헨션 (List Comprehension)
# 파이썬은 다음과 같이 람다 표현식을 지원하지만 List Comprehension이 더 가독성이 높다.

list(map(lambda x: x + 10, [1, 2, 3]))  # [11, 12, 13]

[n * 2 for n in range(1, 10 + 1) if n % 2 == 1]   # [2, 6, 10, 14, 18]

a = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
        a.append(n * 2)

# 파이썬 2.7 이후 List뿐만 아니라 딕셔너리 등도 추가됨
a = {}
for key, value in originals.items():
    a[key] = value

a = {key: value for key, value in originals.items()}


## 제네레이터 : 루프의 반복 iteration 동작을 제어할 수 있는 루틴 형태를 말한다.
# yield 구문을 사용하면 제너레이터를 리턴할 수 있다. return과는 다르게 값을 내보내고 계속 함수를 돌린다.
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

# 만약 다음 값을 생성하려면 next()를 추출하면 된다.
g = get_natural_number()
for _ in range(0, 100):
    print(next(g))

# 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능
def generator():
    yield 1
    yield 'String'
    yield True

g = generator()
g
next(g)  # 1
next(g)  # String
next(g)  # True


## range : 제너레이터의 방식을 활용하는 함수이다.
range()  # range 클래스를 리턴하며, 내부적으로 제너레이터 next()를 호출하듯 숫자를 생성
# 제너레이터를 사용하면 예를들어 100만개가 되는 큰 숫자를 생성할 때에 메모리를 아낄 수 있다. (사용할 때 생성하므로)
a = [n for n in range(100000)]
b = range(100000)

# a 에는 이미 생성된 값이 담겨있고, b는 생성해야 한다는 조건만 존재한다. 둘을 비교하면 range 클래스를 리턴하는 b 방식이 좋다.
import sys
sys.getsizeof(a)  # 8697464
sys.getsizeof(b)  # 48


## enumerate
a = [1, 2, 3]
list(enumerate(a))  # [(0, 1), (1, 2), (2, 3)] : index를 자동으로 부여해준다.

for i, v in enumerate(a):
    print(i, v)


## 나눗셈 연산자
5 / 3  # 1.66666666...67 float
5 // 3  # 1 : int(5 / 3)과 동일
5 % 3  # 2
divmod(5, 3)  # (1, 2) : 몫과 나머지를 한 번에 구할 때


## print
print('A1', 'B2')  # A1 B2
print('A1', 'B2', sep=',')  # A1,B2 : 구분자 지정
print('A1', end=' ')
print('B2')  # A1 B2

# 리스트를 출력할 때는 join()
a = ['A', 'B']
print(' '.join(a))  # A B

idx = 1
fruit = "Apple"
print('{0}: {1}'.format(idx, fruit))
print('{}: {}'.format(idx, fruit))
print(f'{idx}: {fruit}')  # 가장 직관적이며 빠르다.


## pass : 코드의 전체 골격을 잡아 놓고 내부에서 처리할 내용을 차근차근 만들때 사용
# pass는 null 연산으로 아무것도 하지 않는 기능이다.


## locals : locals()는 로컬 심볼 테이블 딕셔너리를 가져오는 메소드이며 업데이트가 가능하다. (디버깅할 때 좋다)
import pprint
pprint.pprint(locals())  # 클래스 메소드 내부의 모든 로컬 변수를 출력해주므로 디버깅할 때 좋다.


## PLUS
def num_matching_sub_seq(self, S: str, words: List[str]) -> int:
    matched_count = 0

    for word in words:
        pos = 0
        for i in range(len(word)):
            # Find matching position for each character.
            found_pos = S[pos:].find(word[i])
            if found_pos < 0:
                matched_count -= 1
                break
            else:  # If found, take step position forward.
                pos += found_pos + 1
        matched_count += 1

    return matched_count


str1s = [
    str1[i:i + 2].lower() for i in range(len(str1) - 1)
    if re.findall('[a-z]{2}', str1[i:i + 2].lower())
]


## 구글 파이썬 스타일 가이드
# 1. 함수의 기본 값으로 가변 객체를 사용하지 않아야 한다. (기본 값으로 []나 {}를 지양해야 한다.)
def foo(a, b=[]):  # No
    pass

def foo(a, b: Mapping = {}):  # No
    pass

# 대신 불변 객체를 사용한다.
def foo(a, b=None):  # Yes
    if b is None:
        b = []

def foo(a, b: Optional[Sequence] = None):  # Yes
    if b is None:
        b = []

# 2. True, False를 판별할 때 암시적인 방법을 사용한다.
# Yes:
if not users:

if foo == 0:

if i % 10 == 0:

# No:
if len(users) == 0:

if foo is not None and not foo:

if not i % 10:

# 3. 최대 줄 길이는 80자로 한다.

