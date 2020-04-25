# -*- coding: UTF-8 -*-

'''
在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
'''

class Student(object):
    pass

s = Student()
s.score = 9999

'''
这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
'''

class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not  isinstance(value,int):
            raise  ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise  ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return '1991-%s' %self._birth

s2 = Student2()
s2.score = 55
s2.birth = '05-12'
print(s2.age)


'''
@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
'''

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return '%f--%f' %(self.width,self.height)

scr = Screen()
scr.width = 100.6
scr.height = 200.9
print(scr.resolution)