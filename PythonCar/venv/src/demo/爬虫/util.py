# -*- coding: UTF-8 -*-
import os

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}

def fun01():
    print('测试自己制作的模块')

def create_pic_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)
        print('[{}]文件夹已创建'.format(name))
    else:
        print('[{}]文件夹已存在'.format(name))


