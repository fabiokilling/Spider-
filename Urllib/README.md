# Python内置的HTTP请求库
        ## urllib.request           请求模块
        ## urllib.error             异常处理模块
        ## urllib.parse             url解析模块
        ## urllib.robotparser       robots.txt解析模块

# 相比Python2变化

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


# Request
request = request.Request(url = url,data = data,headers = headers, method = 'POST')


from urllib import request, parse


url = 'http://httpbin.org/post'

headers = {

        'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
        
        'Host':'httpbin.org'

}

dict = {
    
    'name':'Germey'

}

data = bytes(parse.urlencode(dict),encoding='utf8')

req = request.Request(url=url,data=data,headers=headers,method='POST')

response = request.urlopen(req)

print(response.read().decode('utf-8'))


### 运行结果

{
  
  "args": {}, 
  
  "data": "", 
  
  "files": {}, 
  
  "form": {
  
   "name": "Germey"
  
          }, 
  
  "headers": {
    
    "Accept-Encoding": "identity", 
    
    "Connection": "close", 
    
    "Content-Length": "11", 
    
    "Content-Type": "application/x-www-form-urlencoded", 
    
    "Host": "httpbin.org", 
    
    "User-Agent": "Mozilla/4.0(compatible;MSIE 5.5;Windows NT)"
  
            },
 
  "json": null, 
  
  "origin": "49.4.159.122", 
  
  "url": "http://httpbin.org/post"

}




## Request 还能使用.add_header('User-Agent','Mozilla/4.0(compatible;MSIE 5.5;Windows NT)')来添加headers
