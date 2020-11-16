# -*- coding: UTF-8 -*-
from collections.abc import Iterable


'''

如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称之为迭代
在python中，迭代是通过for in 来完成的，而很多语言比如c语言，迭代list是通过下标完成的，比如java 代码
for (i=0; i<list.length; i++) {
    n = list[i];
}
可以看出，python 的for循环抽象程度是要高于c的for循环，因为python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上
list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

'''

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)


'''
所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。

那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
'''
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

'''
请使用迭代查找一个list中最小和最大值，并返回一个tuple
'''


def findMinAndMax(L):
    min = 0
    max = 0
    for index, value in enumerate(L):
        if index == 0:
            min = value
            max = value
        else:
            if value > max:
                max = value
            else:
                min = value
    return (min, max)
list = [1, 2, 3, 4, 5, 6, 7, 8]
print(findMinAndMax(list))