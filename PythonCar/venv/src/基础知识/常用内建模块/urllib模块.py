# -*- coding: UTF-8 -*-
from urllib import request,parse
import urllib

'''
urllib提供了一系列用于操作URL的功能。

Get
urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：

例如，对百度进行抓取，并返回响应：
'''
path = 'https://www.baidu.com'

def log(f):
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

with request.urlopen(path) as f:
     pass
    # log(f)




'''
如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求百度首页：
'''
# req = request.Request(path)
# header = 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
# req.add_header('User-Agent',header)
# with request.urlopen(req) as f:
#      log(f)


'''
Post
如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
'''

# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
#
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     log(f)


'''
Handler
如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
'''


proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    log(f)

'''
小结
urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。

练习
利用urllib读取JSON，然后将JSON解析为Python对象：

'''