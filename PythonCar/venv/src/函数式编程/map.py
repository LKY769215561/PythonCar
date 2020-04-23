# -*- coding: UTF-8 -*-


'''
如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。

我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：

'''


def f(x):
    return x * x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))


'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''

arr = ['adam', 'LISA', 'barT']

def f2(x):
    return x.capitalize()

r = map(f2,arr)
print(list(r))
