import sys
from collections import Counter
input = sys.stdin.readline

n = input()
arr = list(map(int, input().split()))
m = input()
comp = list(map(int, input().split()))

count = Counter(arr)

print(' '.join(str(count[x]) if x in count else '0' for x in comp))
