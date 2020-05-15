# -*- coding: UTF-8 -*-

'''
定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。
Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
'''

'''
位置参数
我们先写一个计算x的n次方的函数：n 默认值为2
'''
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
        return  s
print(power(5))
print(power(15))

'''
定义默认参数要牢记一点：默认参数必须指向不变对象！
'''
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())

'''
可变参数
在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
'''

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1,2,3]))
print(calc([1,3,5,7]))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))
print(calc())

nums = [1,2,3]
print(calc(nums[0],nums[1],nums[2]))
print(*nums)

'''
关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，
这些关键字参数在函数内部自动组装为一个dict。请看示例：
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

'''
命名关键字参数

对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。

仍以person()函数为例，我们希望检查是否有city和job参数：
'''

def person2(name,age,**kw):
    if 'city' in kw:
        #有city 参数
        pass
    if 'job' in kw:
        #有job参数
        pass
    print('name:',name,'age:',age,'otherL:',kw)

person2('jsck',24,city='shanghai',addr='hanguojie',str='5454')

'''
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
'''

def person3(name,age,*,city,job):
    print(name,age,city,job)

person3('jack',24,city='dfdfd',job='dfdfd')

'''
参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

比如定义一个函数，包含上述若干种参数：
'''
def f1(a,b,c=0,*args,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a,b,c=0,*,d,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)

'''
最神奇的是通过一个tuple和dict，你也可以调用上述函数：
'''
args = (1,2,3,4)
kw = {'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)

'''
以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x, y):
    return x * y
'''

def product(*args):
    total = 1
    for n in args:
        total = total * n
    return total
jinum = product(5,6,7,9)
print('jinum:',jinum)