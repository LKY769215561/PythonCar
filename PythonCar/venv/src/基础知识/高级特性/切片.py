# -*- coding: UTF-8 -*-


arr = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

'''
取一个list或tuple的部分元素是非常常见的操作
'''

print(arr[0:3])
print(arr[:3])
print(arr[-2:])

arr1 = list(range(100))


'''
可以通过切片轻松取出某一段数列。比如前10个数：
'''
print(arr1[:10])


'''
后10个数：
'''
print(arr1[-10:])


'''
前11-20个数：
'''
print(arr1[10:20])

'''
前10个数，每两个取一个：
'''
print(arr1[:10:2])

'''
利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
'''

def trim(s):
    s2 = s
    if s2[0] == ' ':
        s2 = s2[-(len(s2)-1):]
    if s2[-1] == ' ':
        s2 = s2[:len(s2)-1]
    return s2

def trim2(s):
    s2 = s
    if s2[0] == ' ':
        s2 = s[1:(len(s2)-1)]
    if s2[-1] == ' ':
        s2 = s2[0: (len(s2)-1)]

    return s2


print(trim(' dfdfdfdfd  '))
print(trim2(' dfdfdfdfd  '))
