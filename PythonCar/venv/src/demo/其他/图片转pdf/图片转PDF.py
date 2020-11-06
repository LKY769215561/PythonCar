import os
import sys
from PIL import Image


def create_pic_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)
        print('[{}]文件夹已创建'.format(name))
    else:
        print('[{}]文件夹已存在'.format(name))


dirPath = os.getcwd() + '/图片转pdf/jpgDir'
newPath = os.getcwd() + '/newjpgDir'
dirList = os.listdir(path=dirPath)
print(dirList)
create_pic_dir('newjpgDir')
for f in dirList:
    if f.endswith('.jpg'):
        img = Image.open(dirPath + '/' + f)
        new_size = img.resize((1401,1867))
        new_size.save(newPath + '/' + f)

    else:
        print('none')
