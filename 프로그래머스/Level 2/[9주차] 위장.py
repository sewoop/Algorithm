def solution(clothes):
    kinds_clothes = {}

    for _, kind in clothes:
        if kind in kinds_clothes:
            kinds_clothes[kind] += 1
        else:
            kinds_clothes[kind] = 1

    count = 1
    for i in kinds_clothes.values():
        count *= (i + 1)  # 해당 종류의 의상의 수  + 1(해당 의상이 없는 경우)

    return count - 1  # 의상 모두를 입지 않는 경우의 수를 빼준다.

# 다른 사람 풀이


def solution_(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    print(cnt.values())
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

print(solution_(clothes))
