# 14681.py

x_axis = int(input())
y_axis = int(input())

if x_axis>0 and y_axis>0:
    print('1')
elif x_axis>0 and y_axis<0:
    print('4')
elif x_axis<0 and y_axis>0:
    print('2')
else :
    print('3')
