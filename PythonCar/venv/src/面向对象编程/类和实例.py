# -*- coding: UTF-8 -*-

'''
面向对象最重要的概念就是类（class）和实例（instace）,必须牢记类是抽象的模版，比如Studen类，而实例是根据类创建出来的一个个具体的对象，
每个对象都拥有相同的方法，但各自的数据可能不同。
仍以Student类为例，在python中，定义类是通过class关键字：

'''
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print(self):
        print(self.name,self.score)

    def get_grade(self):
        if self.score >= 90:
            return  'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

'''

class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：

'''
s1 = Student('carey',100)
print(s1.print())
print(s1.get_grade())