# 11729 하노이 탑 이동 순서

n = int(input())


def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, 6-start-end)  # 1단계: n-1개를 2번째 막대로 이동
    print(start, end)  # 2단계: n번째를 3번으로 이동
    hanoi(n - 1, 6-start-end, end)  # 3단계: n-1개를 3번 막대로 이동


print(2**n - 1)
hanoi(n, 1, 3)
