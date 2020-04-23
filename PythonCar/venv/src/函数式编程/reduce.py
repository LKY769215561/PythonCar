# -*- coding: UTF-8 -*-
from  functools import  reduce

def add(x,y):
    return x + y

r = reduce(add,[1,3,4,5,6])
print(r)


'''
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''

arr = [3,4,5,6,7]
def prod(L):
    return reduce(add,L)

print(prod(arr))
