# Python (PEP 8) : D-14 (전기기사)
# 1부 1장은 글이므로 생략

## Loop (반복문)
# 예시 1)
sum = 0
for i in range(1, 10+1):
    sum+=i
# 예시 2)
sum = sum(i for i in range(1, 10+1))
# 예시 3)
sum = sum(range(1, 10+1))


## Generic (제네릭 프로그래밍 : Type을 나중에 지정하는 방식 == C++의 template과 동일)
def are_equal(a, b):
    return a == b

are_equal(10, 10.0)  # 파이썬은 동적 타이핑 언어이므로 제네릭이 필요없지만, 코드의 복잡도가 증가할 시 혼란을 막기 위해 다음과 같이 사용한다.

# 파이썬 제네릭 PEP 484
from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def are_equal(a: T, b: U) -> bool:
    return a == b

are_equal(10, 10.0)


## 배열 반복
foo = ['A', 'B', 'C']
for f in foo:
    print(f)


## 구조체
# 구조체를 지원하지 않지만 구조체와 같은 형태를 정의하려면 namedtuple을 import 해야한다.
from collections import namedtuple
Struct = namedtuple("Struct", "field1 field2 field3")

m = Struct("foo", "bar", "baz")

# Python 3.7+ 의 경우 데코레이션을 사용하여 class를 이용하여 구조체 형태를 정의할 수 있다.
from dataclasses import dataclass

@dataclass
class Product:
    weight: int = None
    price: float = None

apple = Product()
apple.price = 10


## 클래스
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width * self.height

rect = Rectangle(3, 4)
print(rect.area())