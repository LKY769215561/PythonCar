# -*- coding: UTF-8 -*-
import math
'''
计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。
比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：
'''

age = 10
#age = 18
if age >= 18:
    print('your age is',age)
    print('adult')
elif age > 6:
    print('teenager')
else:
    print('your age is',age)
    print('kid')


s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')


'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
weight = 80.5
height = 1.75
bmi = weight / math.pow(height,2)

if bmi < 18.5:
    print('过轻')
elif 18.5< bmi < 25:
    print('正常')
elif 25< bmi < 28:
    print('过重')
elif 28< bmi < 32:
    print('肥胖') 
elif bmi > 32:
    print('严重肥胖')







