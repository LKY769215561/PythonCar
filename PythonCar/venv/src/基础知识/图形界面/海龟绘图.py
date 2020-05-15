# -*- coding: UTF-8 -*-
from turtle import *

'''

在1966年，Seymour Papert和Wally Feurzig发明了一种专门给儿童学习编程的语言——LOGO语言，它的特色就是通过编程指挥一个小海龟（turtle）在屏幕上绘图。

海龟绘图（Turtle Graphics）后来被移植到各种高级语言中，Python内置了turtle库，基本上100%复制了原始的Turtle Graphics的所有功能。

我们来看一个指挥小海龟绘制一个长方形的简单代码：
'''

# 设置笔刷宽度:
width(4)

# 前进:
forward(200)
# 右转90度:
right(90)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()

'''
从程序代码可以看出，海龟绘图就是指挥海龟前进、转向，海龟移动的轨迹就是绘制的线条。要绘制一个长方形，只需要让海龟前进、右转90度，反复4次。

调用width()函数可以设置笔刷宽度，调用pencolor()函数可以设置颜色。更多操作请参考turtle库的说明。

绘图完成后，记得调用done()函数，让窗口进入消息循环，等待被关闭。否则，由于Python进程会立刻结束，将导致窗口被立刻关闭。

turtle包本身只是一个绘图库，但是配合Python代码，就可以绘制各种复杂的图形。例如，通过循环绘制5个五角星：
'''