# -*- coding: UTF-8 -*-


'''
要计算1+2+3，我们可以直接写表达式：
'''
print(1+2+3)

'''
要计算1+2+3+...+10，勉强也能写出来。

但是，要计算1+2+3+...+10000，直接写表达式就不可能了。

为了让计算机能计算成千上万次的重复运算，我们就需要循环语句。

Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：

'''
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

'''
再比如我们想计算1-100的整数之和，可以用一个sum变量做累加：
如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
'''
sum = 0
list = range(101)
for x in list:
    sum = sum + x
print(sum)

'''
请自行运行上述代码，看看结果是不是当年高斯同学心算出的5050。
第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
'''
sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n -2
print(sum2)


'''
请利用循环依次对list中的每个名字打印出Hello, xxx!：
'''

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello,' + name)


