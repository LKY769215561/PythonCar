# -*- coding: UTF-8 -*-

'''
看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

__str__
我们先定义一个Student类，打印一个实例：

'''
class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    def ___repr__(self):
        return 'Student object (name: %s)' % self.name

print(Student(name='carey'))

'''
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

'''

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b # 计算下一个值
        if self.a > 10000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)

'''
__getitem__
Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

'''

class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib2()
print(f[5])
print(list(range(100))[5:10])
'''
对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
'''
#print(f[0:5])

class Fib2(object):
    def __getitem__(self, item):
        if isinstance(item,int):
            a,b = 1,1
            for x in range(item):
                a,b = b,a+b
            return a

        if isinstance(item,slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                 L.append(a)
                 a, b = b, a + b
            return L
f1 = Fib2()
print(f1[0:5])


class Student2(object):

    def __init__(self):
        self.name = 'carey'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr =='age':
            return  lambda :25
        return AttributeError('没有\'%s\'属性啊，烙铁' %attr)


s5 = Student2()
print(s5.name)
'''
调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
'''
print(s5.score)
'''
返回函数也是完全可以的：
'''
print(s5.age())
print(s5.height)
'''
这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。

这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

举个例子：

现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

http://api.server/user/friends
http://api.server/user/timeline/list
如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

利用完全动态的__getattr__，我们可以写出一个链式调用：
'''

class Chain(object):
    def __init__(self,path='http://api/carey'):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' %(self._path,path))
    def __str__(self):
        return self._path
    __repr =__str__

api1 = Chain().status.user.timeline.list
print(api1)

'''
一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。

任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
'''

class Student3(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('my name is %s' % self.name)
s31 = Student3(name='carey')
print(s31())

'''
__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
'''
print(callable(Student3))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))