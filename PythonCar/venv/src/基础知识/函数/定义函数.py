# -*- coding: UTF-8 -*-
import math

'''
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
我们以自定义一个求绝对值的my_abs函数为例：
'''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-10))

'''
空函数
如果想定义一个什么事也不做的空函数，可以用pass语句：
'''

def nop():
    pass

'''
返回多个值
函数可以返回多个值吗？答案是肯定的。
比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标：
原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
'''

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = move(100,100,60,math.pi/6)
print(x,y)
p = move(100,100,60,math.pi/6)
print(p)