# 1316.py

re=0
for i in range(int(input())):
    a=input()
    re+=list(a)==sorted(a, key=a.find)
print(re)


# words = [input() for _ in range(int(input()))]

# result=0
# for word in words:
#     flag = True
#     if len(word)==1:
#         result+=1
#     else:
#         for i in range(len(word)-1):
#             if word[i]!=word[i+1] and word.find(word[i],i+1)!=-1:
#                 flag=False
#                 break
#         if flag:
#             result+=1
# print(result)