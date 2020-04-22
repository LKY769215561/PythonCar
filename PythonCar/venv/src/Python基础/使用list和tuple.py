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

'''
要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
'''
classmates.pop(1)
print(classmates)


'''
要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
'''
classmates[1] = 'good'
print(classmates)


'''
要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
'''
arr = ['allpe',123,True]
print(arr)

'''
list元素也可以是另一个list，比如：
'''
arr1 = ['phton','java',arr,'swift']
print(arr1)



'''
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
'''

classmates2 = ('Michael', 'Bob', 'Tracy')
print(classmates2)

'''
tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
'''
t = (1,2)
print(t)

'''
如果要定义一个空的tuple，可以写成()：
'''
t1 = ()
print(t1)


'''
但是，要定义一个只有1个元素的tuple，如果你这么定义：
定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
'''
t2 = (1)
print(t2)
t3 = (1,)
print(t3)


Y = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(Y[0][0])
# 打印Python:
print(Y[1][1])
# 打印Lisa:
print(Y[2][2])

