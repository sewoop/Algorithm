# 10996.py

n = int(input())
print((("* "*((n+1)//2))+"\n"+(" *"*(n//2))+'\n')*n)

# n = int(input())
# for i in range(1, n+1):
#     print('* '*((n+1)//2))
#     print(' *'*((n)//2))

# import math
# n = int(input())
# num = 2*n if n!=1 else n

# for i in range(num):
#     if i%2==0:
#         print(math.ceil(0.5*n)*'* ')
#     else :
#         print(math.ceil(0.5*(n-1))*' *')
