# -*- coding: UTF-8 -*-
'''
了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：

浏览器发送一个HTTP请求；

服务器收到请求，生成一个HTML文档；

服务器把HTML文档作为HTTP响应的Body发送给浏览器；

浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

所以，最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。

正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。

这个接口就是WSGI：Web Server Gateway Interface。

WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”：

environ {'PATH': '/Users/qzj/venv/bin:/Users/qzj/opt/anaconda3/bin:/Users/qzj/opt/anaconda3/condabin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin',
 'CONDA_DEFAULT_ENV': 'base',
  'CONDA_EXE': '/Users/qzj/opt/anaconda3/bin/conda',
   'CONDA_PYTHON_EXE': '/Users/qzj/opt/anaconda3/bin/python',
   'PS1': '(venv) ',
   'CONDA_PREFIX': '/Users/qzj/opt/anaconda3',
   '_CE_M': '',
   'LOGNAME': 'qzj',
   'XPC_SERVICE_NAME': 'com.jetbrains.pycharm.2164',
    'PWD': '/Users/qzj/PythonCar/PythonCar/venv/src/Web开发',
    'PYCHARM_HOSTED': '1',
    'CONDA_SHLVL': '1',
    'PYCHARM_DISPLAY_PORT': '63342',
    'PYTHONPATH': '/Users/qzj/PythonCar/PythonCar:/Users/qzj/PythonCar/PythonCar/venv/src:/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend:/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display',
    'SHELL': '/bin/zsh', 'PYTHONIOENCODING': 'UTF-8', 'OLDPWD': '/Applications/PyCharm.app/Contents/bin', 'USER': 'qzj', 'TMPDIR': '/var/folders/_g/ptcy9tmj3xj64hbzjrfbhqnr0000gn/T/',
    'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.YsaZGI5HOb/Listeners',
    '_CE_CONDA': '',
    'VIRTUAL_ENV': '/Users/qzj/venv',
    'XPC_FLAGS': '0x0', 'PYTHONUNBUFFERED': '1',
     '__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34', 'CONDA_PROMPT_MODIFIER': '(base) ',
      'LC_CTYPE': 'UTF-8', 'HOME': '/Users/qzj',
      '__PYVENV_LAUNCHER__': '/Users/qzj/venv/bin/python',
      'SERVER_NAME': '1.0.0.127.in-addr.arpa',
      'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '',
      'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/carey444', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1',
      'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': 'localhost:8000', 'HTTP_CONNECTION': 'keep-alive',
       'HTTP_CACHE_CONTROL': 'max-age=0', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
       'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'HTTP_SEC_FETCH_SITE': 'none', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_USER': '?1', 'HTTP_SEC_FETCH_DEST': 'document',
       'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9',
       'HTTP_COOKIE': 'Pycharm-3a498cca=412b16ce-dc83-40b6-9611-4b4999c2a0b2', 'wsgi.input': <_io.BufferedReader name=7>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True,
     'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}
127.0.0.1 - - [05/May/2020 19:49:40] "GET /carey444 HTTP/1.1" 200 25

'''

def application(environ, start_response):
    print('environ %s' %environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


'''
上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

environ：一个包含所有HTTP请求信息的dict对象；

start_response：一个发送HTTP响应的函数。

在application()函数中，调用：
'''