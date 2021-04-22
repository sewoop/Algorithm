# iter
data = [1, 2, 3]
it = iter(data)
# print(it)
print(next(it)) # 1
print(list(it)) # [2, 3]

# lambda
_sum = lambda a, b: a + b
print(f'lambda: {_sum(3, 4)}')

# map
# map(function, iterable)
li = [-3, -2, -1, 1, 2, 3]
result = list(map(lambda i: i ** 2, li))
print(f'list(map): {result}')

it = map(lambda i: i ** 2, li)
print(f'map_0: {next(it)}')
print(f'map_1: {next(it)}')
print(f'map_2: {next(it)}')

# filter
# filter(function, iterable)
print(f'filter: {list(filter(lambda x: x > 0, li))}')

# reduce
# python3 부터 내장 함수에서 빠짐
def __reduce(function, iterable, initializer=None): 
    it = iter(iterable) 
    if initializer is None: 
        value = next(it) 
    else: 
        value = initializer 
    for element in it: 
        value = function(value, element) 
    return value

# reduce(function, iterable, iterable, initializer(생략가능))
from functools import reduce
print(f'reduce: {reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])}') # = ((((1+2)+3)+4)+5)

## reduce를 활용하여 최대값 구하기
print(reduce(lambda a, b: a if a > b else b, li))

## Input : data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c']
## # Output : {'a': 3, 'b': 2, 'c': 3}
data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c']
print(reduce(lambda a, b: a.update({b: a.get(b, 0) + 1}) or a, data,{}))
