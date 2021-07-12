# 2530.py

H, M, S = map(int, input().split())
D = int(input())

S += D
M += S//60
H += M//60
S = S % 60
M = M % 60
H = H % 24

print(H, M, S)
