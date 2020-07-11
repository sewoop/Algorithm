# 2747.py

n,a,b = int(input()),0,1

for i in range(n):
    c = a+b
    a,b = b,c
    
print(a)
