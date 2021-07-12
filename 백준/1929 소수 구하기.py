# 1929.py
import math


def isPrime(start, end):
    primeList = [True for _ in range(end + 1)]

    primeList[0] = primeList[1] = False

    for i in range(2, int(math.sqrt(end)) + 1):
        if primeList[i] == True:
            j = 2
            while i * j <= end:
                primeList[i * j] = False
                j += 1

    for i in range(start, end + 1):
        if primeList[i] == True:
            print(i)


m, n = map(int, input().split())

isPrime(m, n)
