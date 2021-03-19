def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    return str(int(''.join(numbers)))

# 문자열 정렬을 이용한 알고리즘
'''
    문자열을 정렬할 때, 맨 앞의 요소의 아스키코드 값을 이용하여 값을 비교하기 때문에 가능한 방법이다.
    문자에 lambda x: x*3을 적용하면 각 문자를 3번 반복 곱하여라이며, 이는 'S' * 3 = 'SSS'이 된다. 
    
    왜, 3번을 곱하는 가? 왜냐하면, 주어진 조건에서 numbers의 각 숫자는 1000이하이기 때문이다.
'''


# solution([6, 10, 2])
solution([3, 30, 34, 5, 9])