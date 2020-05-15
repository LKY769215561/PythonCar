# -*- coding: UTF-8 -*-


'''

Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。

我们以内建的sys模块为例，编写一个使用模块的模块：

'''

'a test module'

__author__ = 'carey'

import sys
#import random
from random import randint,choice

#num = random.randint(1,10)
#print('num:',num)

num2 = randint(3,9)
print(num2)
num3 = choice(1,2,3,4)
print(num3)

def test():
    args = sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('hello,%s!' %args[1])
    else:
        print('too many arguments')

if __name__ =='__main__':
    test()

'''
第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。

后面开始就是真正的代码部分。

你可能注意到了，使用sys模块的第一步，就是导入该模块：

import sys

'''
