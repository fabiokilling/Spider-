# Python内置的HTTP请求库
## urllib.request           请求模块
## urllib.error             异常处理模块
## urllib.parse             url解析模块
## urllib.robotparser       robots.txt解析模块

相比Python2变化

### Python2

import urllib2

response = urllib2.urlopen('http://www.baidu.com')

### Python3

import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')

# urllib
## urlopen
urllib.request.urlopen(url,data=None,[timeout,]*,cafile=None,cadefault=False,context=None)


# 'http://httpbin.org'  用来做http测试用网址
