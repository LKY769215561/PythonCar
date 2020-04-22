# -*- coding: UTF-8 -*-

'''
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
比如，列出班里所有同学的名字，就可以用一个list表示：
'''
classmates = ['carey','wqq','bob','tom']
print(classmates)
length = len(classmates)
str1 = '长度:%d' %len(classmates)
print(str1)
print(classmates[0])
print(classmates[1])
print(classmates[-1])

'''
list是一个可变的有序表，所以，可以往list中追加元素到末尾：
'''
classmates.append('gp')
print(classmates)


'''
也可以把元素插入到指定的位置，比如索引号为1的位置：
'''
classmates.insert(1,'lhy')
print(classmates)


'''
要删除list末尾的元素，用pop()方法：
'''

classmates.pop()
print(classmates)