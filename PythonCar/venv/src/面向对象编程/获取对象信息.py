# -*- coding: UTF-8 -*-
import types

'''
首先，我们来判断对象类型，使用type()函数：

基本类型都可以用type()判断：
'''

print(type(123))
print(type('str'))
print(type(None))

'''
如果一个变量指向函数或者类，也可以用type()判断：
'''
print(type(abs))

print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))

'''
判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
'''

def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

'''
使用isinstance()
对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

我们回顾上次的例子，如果继承关系是：
object -> Animal -> Dog -> Husky
那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：
'''

class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h,Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Dog) and isinstance(d, Animal))
print(isinstance(d, Husky))


'''
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
'''
print(dir('ABC'))

'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
'''
print(len('ABC'))
print('ABC'.__len__())

'''
我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
'''
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))

'''
仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
'''
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj,'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))

'''
可以传入一个default参数，如果属性不存在，就返回默认值：
'''
print(getattr(obj, 'wqq', 521))

'''
也可以获得对象的方法：
'''
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))