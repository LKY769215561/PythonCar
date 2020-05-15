# -*- coding: UTF-8 -*-


'''
在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样就隐藏了内部的复杂逻辑，但是，从前面Student类的定义来看，
外部代码还是可以自由地修改一个实例的name score属性
'''


class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score



s1 = Student(name="carey",score=99)
print(s1.score)
s1.score = 60
print(s1.score)

'''
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__,在python中，实例的变量名如果以__开头，就变成了一个私有变量（privite），只有内部可以
访问，外部不能访问，所以，我们把Student类改一改：
'''
class Student2(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

s2 = Student2(name="carey",score=100)
s2.__score = 70
print(s2.__score)


'''
请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
'''

class Student3(object):


    def get_gender(self):
        return  self.__gender
    def set_gender(self,gender):
        self.__gender = gender

s3 = Student3()
s3.set_gender(True)
print(s3.get_gender())