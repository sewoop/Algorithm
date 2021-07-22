n, k = map(int, input().split())

def f(n):
    if n == 0: return 1
    if n == 1: return 1
    return n * f(n - 1)
print(f(n) // (f(n - k) * f(k)))