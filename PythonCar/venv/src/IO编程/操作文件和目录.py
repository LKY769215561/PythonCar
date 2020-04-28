# -*- coding: UTF-8 -*-
import os

'''
如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。

如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。

打开Python交互式命令行，我们来看看如何使用os模块的基本功能：

'''
print(os.name)

'''
要获取详细的系统信息，可以调用uname()函数：
'''
print(os.uname())

'''
注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

环境变量
在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
'''
print(os.environ)

'''
要获取某个环境变量的值，可以调用os.environ.get('key')：
'''
print(os.environ.get('PATH'))

'''
操作文件和目录
操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
'''

path = '/Users/qzj/Desktop/测试'
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
newpath = os.path.join(path,'testdir')
print(newpath)
# 然后创建一个目录:
os.mkdir(newpath)
# 删掉一个目录:
os.rmdir(newpath)

'''
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

'''
print(os.path.split('/Users/michael/testdir/file.txt'))
print(os.path.splitext('/path/to/file.txt'))

'''
这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
'''


