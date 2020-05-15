# -*- coding: UTF-8 -*-

'''
MySQL是Web世界中使用最广泛的数据库服务器。SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。

此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。

安装MySQL
可以直接从MySQL官方网站下载最新的Community Server 5.6.x版本。MySQL是跨平台的，选择对应的平台下载安装文件，安装即可。

安装时，MySQL会提示输入root用户的口令，请务必记清楚。如果怕记不住，就把口令设置为password。

在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。

在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：

'''


# 导入MySQL驱动:
import mysql.connector
import pymysql

# 注意把password设为你的root口令:
#conn = mysql.connector.connect(user='root',password='password',database='test')
db_host = "localhost"
db_username = "root"
db_password = "password"
db_name = "test"
conn = pymysql.connect(
    host=db_host,
    user=db_username,
    passwd=db_password,
    database=db_name,
)


cursor = conn.cursor()

# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'carey'])
print(cursor.rowcount)

# 提交事务:
conn.commit()
conn.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()