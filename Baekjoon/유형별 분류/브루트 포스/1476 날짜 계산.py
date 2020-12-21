# 지구 E, 태양 S, 달 M
# 1<=E<=15, 1<=S<=28, 1<=M<=19
# 1년 == 111
# 15년 == 15 15 15
# 16년 == 1 16 16

# 시간 초과
# 입력
E, S, M = map(int, input().split())
# E, S, M = 1, 1, 1 # 임시

N, init = 0, []
while init != [E, S, M]:
    init = [0, 0, 0]
    N += 1
    for i in range(N):
        init[0] += 1
        init[1] += 1
        init[2] += 1

        if init[0] == 16:
            init[0] = 1
        
        if init[1] == 29:
            init[1] = 1

        if init[2] == 20:
            init[2] = 1
print(N)

## 중국인의 나머지 정리
E,S,M=map(int,input().split())
print((6916*E+4845*S+4200*M-1)%7980+1)