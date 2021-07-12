# 2941.py

cro_str = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str_ = input()

for cro_ in cro_str:
    str_ = str_.replace(cro_, '*')

print(len(str_))
