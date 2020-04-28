# -*- coding: UTF-8 -*-
from io import StringIO
from io import BytesIO

'''
StringIO
很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO顾名思义就是在内存中读写str。

要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

'''

f = StringIO()
f.write('hello')
f.write(' ')
f.write('carey')
str = f.getvalue()
print(str)

f2 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())

'''
BytesIO
StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
'''
f3 = BytesIO()
f3.write('中国'.encode('utf-8'))
print(f3.getvalue())

f4 = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(f4.read())
