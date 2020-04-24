# -*- coding: UTF-8 -*-

'''
由于Python是动态语言，根据类创建的实例可以任意绑定属性。

给实例绑定属性的方法是通过实例变量，或者通过self变量：
'''

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

'''
但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
'''

class Student2(object):
    name = 'Student'

s2 = Student2()
print(s2.name)
print(Student2.name)
s2.name = 'Michael'
print(s2.name)
del s2.name
print(s2.name)

'''
从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
'''

'''
为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
'''

class Student3(object):
    count = 10086
    def __init__(self):
        Student3.count = Student3.count + 1
        pass

st1 = Student3()
print(st1.count)
st2 = Student3()
print(st2.count)

'''
实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''