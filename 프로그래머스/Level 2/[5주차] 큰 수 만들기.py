# MARK: - itertools의 조합으로 풀 수도 있지만 그럴 경우 '시간 초과'가 발생한다. 따라서, 이 문제는 실행 시간을 낮추는 것이 핵심이다.
def solution(number, k):

    stack = [number[0]]  # 맨 앞의 값을 스택에 추가

    for num in number[1:]:  # 추가된 값 후의 값으로 비교

        # 앞의 값들이 현재 값(num)보다 작다면 반복해서 제거
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()

        stack.append(num)  # 삭제해야될 수(k)를 다 소진했거나, 스택의 마지막 값이 현재 값보다 크면 그냥 집어 넣음

    if k != 0:
        stack = stack[: -k]  # 999와 같이 숫자가 같은 경우를 제거하기 위함

    return ''.join(stack)


# number = "1924"
# number = "1231234"
# number = "4177252841"
number = "999"
k = 2
print(solution(number, k))
