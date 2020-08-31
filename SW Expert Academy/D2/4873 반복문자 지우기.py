from collections import deque

Ts = int(input())

for T in range(1, Ts + 1):
    strings = list(input())
    # print(strings)

    # 스택 생성
    stack = deque()

    # 글자 하나씩 가져와서 
    for string in strings:
        # print(stack)

        # stack이 비어 있으면 하나 넣고 시작
        if not stack:
            stack.append(string)
        else:
            # stack의 top원소와 단어를 비교
            n = stack[-1]
            if n == string:
                stack.pop()
            else:
                stack.append(string)

    print(f'#{T} {len(stack)}')