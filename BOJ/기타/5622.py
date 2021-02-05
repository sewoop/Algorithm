# 5622.py

dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
S = input()

num = [idx for i in S for idx, temp in enumerate(dial) if i in temp]

print(sum(num) + 3*len(S))


'''
dial = str(input())
dial_str = {
            '1':[], '2':['A','B','C'], '3':['D','E','F'],\
            '4':['G','H','I'], '5':['J','K','L'], '6':['M','N','O'],\
            '7':['P','Q','R','S'], '8':['T','U','V'], '9':['W','X','Y','Z'],'0':[]
            }

def dial_to_sum(dial):
    lt = []
    for k in range(len(dial)):
        for i,v in dial_str.items():
            if dial[k] in v:
                lt.append(int(i)+1)
    return sum(lt)

print(dial_to_sum(dial))
'''