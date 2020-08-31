from collections import deque
from typing import List

def isValid(temp: str, string: str) -> bool:
    if temp == '{' and string == '}':
        return True
    elif temp == '(' and string == ')':
        return True
    else:
        return False

Ts = int(input())

for T in range(1, Ts + 1):
    strings = list(str(input()))
    #print(strings)

    stack = deque()

    container = ['{', '}','(', ')']
    for string in strings:
        if string in container:
            if len(stack) == 0:
                stack.append(string)
                continue
            else:
                temp = stack[-1]
                if isValid(temp, string):
                    stack.pop()
                else: 
                    stack.append(string)

    if len(stack) != 0:
        print(f'#{T} 0')
    else:
        print(f'#{T} 1')
