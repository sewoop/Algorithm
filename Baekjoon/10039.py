# 10039.py

lt = []
for i in range(5):
    lt.append(int(input()))

for i,v in enumerate(lt):
    if v<40 :
        lt[i]=40

print(round(sum(lt)/len(lt)))