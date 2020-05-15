# -*- coding: UTF-8 -*-


'''
函数作为返回值
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
'''

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f1 = lazy_sum([1,3,4])
f2 = lazy_sum([1,3,4])
print(f1)
print(f2)


'''
注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
'''

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

'''
在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。

你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
'''
print(f1())
print(f2())
print(f3())


def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f4, f5, f6 = count2()

print(f4())
print(f5())
print(f6())


'''
利用闭包返回一个计数器函数，每次调用它返回递增整数：
'''