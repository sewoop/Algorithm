import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = set()
b = set()

for _ in range(n):
    a.add(input().strip())

for _ in range(m):
    b.add(input().strip())

c = sorted(b.intersection(a))

print(len(c))
print(*c, sep="\n")