# -*- coding: UTF-8 -*-
import requests,os

'''
读写文件是最长江的IO操作，Python内置了读写文件的函数，用法和C是兼容的
读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
'''

path = '/Users/qzj/Desktop/测试/打包签名.txt'

'''
要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标识符：
'''
f = open(path,'r')

'''
标示符'r'表示读，这样，我们就成功地打开了一个文件。
'''

'''
如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
'''
str = f.read()
print(str)

'''
最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
'''

f.close()

'''
Python引入了with语句来自动帮我们调用close()方法：
'''

with open(path,'r') as f2:
    print(f2.read())
    pass

'''
和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
'''


f3 = open(path,'r') 

for line in f3.readlines():
    print(line.strip())

'''
file-like Object
像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。'''

'''
二进制文件
前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：'''

f4 = open(path,'rb')
f4.read()



'''
写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
可以传入'a'以追加（append）模式写入。

'''
f5 = open(path,'a')
f5.write('hello carey 666')
f5.close()

'''
你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

'''


downloadPath = 'download/'
pic_link = 'http://pic.topmeizi.com/wp-content/uploads/2016a/04/08/01.jpg'
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

def creatDir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print('[{}]文件夹已创建'.format(path))
    else:
        print('[{}]文件夹已存在'.format(path))


if __name__ == '__main__':
    #创建文件存放路径
    creatDir(downloadPath)
    #下载图片
    res = requests.get(pic_link,header)
    imageName = pic_link.split('/')[-1]
    imagePath = downloadPath + imageName
    print('下载完成')
    #写入目录文件 w:写文件 wb:写二进制文件 a:追加
    with open(imagePath,'wb') as f:
        f.write(res.content)

