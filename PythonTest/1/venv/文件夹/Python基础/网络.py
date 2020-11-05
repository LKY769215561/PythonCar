from urllib import request

# with request.urlopen('http://www.baidu.com') as f:
#      data = f.read()
#      print('Status:',f.status,f.reason)
#      for k,v  in f.getheaders():
#          print('%s: %s' % (k, v))


with request.urlopen('http://www.baidu.com') as f:
    data = f.read()
    print('status:',f.status,f.reason)
    for k,v in f.getheaders():
        print(k,v)