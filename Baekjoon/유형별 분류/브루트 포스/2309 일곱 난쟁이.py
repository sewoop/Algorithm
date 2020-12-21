from itertools import combinations

# 일곱 난쟁이의 키의 합이 100

# 난쟁이 리스트 초기화
seven = []
for _ in range(9):
    seven.append(int(input()))

# seven = [20, 7, 23, 19, 10, 15, 25, 8, 13] # 임시

combs = combinations(seven, 7) # 조합

for comb in list(combs):
    if sum(comb) == 100:
        seven = sorted(comb)
        break
    
for i in seven:
    print(i)


## 다른 풀이
seven = []
for _ in range(9):
    seven.append(int(input()))

sum_seven = sum(seven) # 9개의 수의 총합
one, two = 0, 0

for i in range(8):
    for j in range(i + 1, 9):
        if sum_seven - (seven[i] + seven[j]) == 100: # 총합에서 2개의 합을 빼서
            one, two = seven[i], seven[j] # 뺀 총합이 100인 원소 2개를 찾아서

seven.remove(one) # 리스트에서 제거
seven.remove(two)
seven.sort() # 정렬

for i in seven:
    print(i) # 출력