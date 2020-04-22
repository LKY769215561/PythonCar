# -*- coding: UTF-8 -*-

'''
调用abs函数
'''
print(abs(100))
print(abs(-20))
print(abs(12.34))

'''
调用max函数
'''
print(max(1,2))
print(max(2,3,1,-9))


'''
数据类型转换
'''
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

'''
请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
'''

n1 = 255
n2 = 10000
print(hex(n1))
print(hex(n2))