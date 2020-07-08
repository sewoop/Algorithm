# 1065.py

n = int(input())
cnt = 0
for i in range(1,n+1):
    if i>99:
        lt = []
        n = i
        while n>0:
            lt.append(n%10)
            n = n//10
        # print(f'{i} : {lt}, cnt:{cnt}')
        len_ = len(lt)-1
        if lt[len_]-lt[len_-1]==lt[len_-1]-lt[len_-2]:
            cnt+=1
    else : 
        cnt+=1
print(cnt)
