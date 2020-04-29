# -*- coding: UTF-8 -*-
import re
from  datetime import datetime,timedelta,timezone


'''

datetime是Python处理日期和时间的标准库。

获取当前日期和时间
我们先看如何获取当前日期和时间：
'''
now = datetime.now()
print(now)
print(type(now))

'''
注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。

如果仅导入import datetime，则必须引用全名datetime.datetime。

datetime.now()返回当前日期和时间，其类型是datetime。

获取指定日期和时间
要指定某个日期和时间，我们直接用参数构造一个datetime：
'''
dt = datetime(1991,5,12,12,20)
print(dt)

'''
在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。

你可以认
'''
print(dt.timestamp())

'''
timestamp转换为datetime
要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：
2015-04-19 12:20:00
实际上就是UTC+8:00时区的时间：
2015-04-19 12:20:00 UTC+8:00
而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：
2015-04-19 04:20:00 UTC+0:00
'''
t = 674022000.0
print(datetime.fromtimestamp(t))#本地时间
print(datetime.utcfromtimestamp(t))# UTC时间

'''
str转换为datetime
很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
'''
carey = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(carey)

'''
如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
'''
print(now.strftime('%a, %b, %d, %H:%M'))

'''
datetime加减
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
'''
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2,hours=12))


'''
本地时间转换为UTC时间
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。

一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
'''
tz_utc_8 = timezone(timedelta(hours=8))
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

'''
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
'''

def to_timestamp(dt_str,tz_str):

     tzRegex = re.compile(r'UTC(.*):')
     tZone = int(tzRegex.match(tz_str).group(1))
     localDate = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
     dt = localDate - timedelta(hours=tZone)
     return dt.timestamp()

t3 = to_timestamp('2015-1-21 9:01:30', 'UTC+5:00')
print(t3)