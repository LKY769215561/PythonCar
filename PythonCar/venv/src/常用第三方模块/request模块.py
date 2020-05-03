# -*- coding: UTF-8 -*-
import requests

'''
使用requests
要通过GET访问一个页面，只需要几行代码：
'''
path = 'https://www.baidu.com/'
#r = requests.get(path)
'''
对于带参数的URL，传入一个dict作为params参数：
'''
#r = requests.get(path, params={'q': 'python', 'cat': '1001'})

'''
需要传入HTTP Header时，我们传入一个dict作为headers参数：
'''
#r = requests.get(path, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

'''
要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
'''



#r = requests.post(path+'login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

'''
requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
'''
params = {'key':'value'}
#r = requests.post(path,json=params)

'''
类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
'''
upload_files = {'file':open('444.xml','rb')}
r = requests.post(path,files=upload_files)
'''
在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。

把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：
'''


print(r.status_code)
print(r.text)