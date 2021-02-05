from collections import deque
import re

Ts = int(input())

for T in range(1, Ts + 1):
    postfix = list(input().split())
    # print(postfix)
    
    # 스택 생성
    stack = deque()
    
    try:
        for p in postfix:
            print(stack)
            if p.isdecimal():
                stack.append(int(p))
            elif p == '.':
                if len(stack) == 1:
                    print(f'#{T} {stack.pop()}')
                else:
                    raise IndexError  # 연산자 수가 부족해서 stack에 숫자가 남은 경우
            else:
                nop = [stack.pop(), stack.pop()]
                if p == '+':
                    temp = nop[1] + nop[0]
                elif p == '-':
                    temp = nop[1] - nop[0]
                elif p == '*':
                    temp = nop[1] * nop[0]
                elif p == '/':
                    temp = nop[1] // nop[0]
                stack.append(temp)
    except IndexError:
        print(f'#{T} error')