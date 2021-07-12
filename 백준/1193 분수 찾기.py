# 1193.py
# (1)
# n = int(input())
# a,b,cnt = 1,1,1
# p_a,p_b,p_cnt = 1,1,1

# while n>=a:
#     p_a,p_b,p_cnt = a,b,cnt
#     a+=b
#     b+=1
#     cnt+=1

# if p_cnt%2!=0:
#     print(str(p_cnt-(n-p_a))+'/'+str(1+(0 if n==p_a else n-p_a)))
# else :
#     print(str(1+(0 if n==p_a else n-p_a))+'/'+str(p_cnt-(n-p_a)))
    
# (2)
n,a,b=int(input()),1,1
while n>=a:a+=b;b+=1
k=[a-b+1,b-1]; print(f'{1 if n==k[0] else n-k[0]+1}/{k[1]-n+k[0]}') if b%2 else print(f'{k[1]-n+k[0]}/{1 if n==k[0] else n-k[0]+1}')