# 5543.py

lt = []
dt = []
for i in range(5):
    if i < 3:
        lt.append(int(input()))
    else:
        dt.append(int(input()))

print(min(lt)+min(dt)-50)
