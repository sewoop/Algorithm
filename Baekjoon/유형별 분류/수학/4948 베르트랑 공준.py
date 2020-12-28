# 1929.py
import math

def isPrime(inputs):
    counts = []
    for inp in inputs:
        start = inp
        end = start * 2
        count = 0

        primeList = [True for _ in range(end + 1)]

        primeList[0] = primeList[1] = False

        for i in range(2, int(math.sqrt(end)) + 1):
            if primeList[i] == True:
                j = 2
                while i * j <= end:
                    primeList[i * j] = False
                    j += 1

        for i in range(start + 1, end + 1):
            if primeList[i] == True:
                count += 1

        counts.append(count)

    return counts


inputs = []

n = int(input())
inputs.append(n)
while n != 0 :
    n = int(input())
    if n != 0:
        inputs.append(n)

for i in isPrime(inputs):
    print(i)
