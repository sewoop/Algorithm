from itertools import combinations
import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = 0

    for i in list(combinations(nums, 3)):
        if is_prime(sum(i)):
            answer += 1
    return answer

nums = [1, 2, 3, 4]
print(solution(nums=nums))