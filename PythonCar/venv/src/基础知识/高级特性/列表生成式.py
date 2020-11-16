# -*- coding: UTF-8 -*-
import os

'''
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
'''

print(list(range(1, 11)))


'''
但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
'''
Y = [x * x for x in range(1, 11)]
K = [x * x for x in range(1, 11) if x % 2 == 0]
print(Y)
print(K)

'''
还可以使用两层循环，可以生成全排列：
'''
arr = [m + n for m in 'ABC' for n in 'XY']
print(arr)

'''
例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
'''
arr1 = [d for d in os.listdir('.')]
print(arr1)


'''
for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
'''
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

'''
因此，列表生成式也可以使用两个变量来生成list：
'''
arr2 = [k + '=' + v for k, v in d.items()]
print(arr2)

'''
最后把一个list中所有的字符串变成小写：
'''
arr3 = ['Hello', 'World', 'IBM', 'Apple']
arr4 = [s.lower() for s in arr3]
print(arr4)


'''
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
'''
arr5 = ['Hello', 'World', 18, 'Apple', None]
arr6 = [s.lower() for s in arr5 if isinstance(s, str)]
print(arr6)
