# 2581.py
import math

min_ = int(input())
max_ = int(input())
lt = []

if (min_>0 and min_<=10000) and (max_>0 and max_<= 10000) :
    if min_ > max_ :
        min_,max_ = max_,min_

    def ssosu(num):
        for i in range(2, num):
            if num%i == 0:
                return False
        return True

    for i in range(int(min_), int(max_)+1):
        if i!=1 and ssosu(i):
            lt.append(i)

    if len(lt) != 0 :
        print(sum(lt),min(lt), sep='\n')

    else :
        print('-1')