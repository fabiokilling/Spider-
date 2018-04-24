Requests 是用Python语言编写，基于urllib，采用Apache2 Licensed开源写的的HTTP库。

它比urllib更加方便，可以节约我们大量的工作，完全满足HTTP测试需求。

一句话--Python实现的简单易用的HTTP库



# cookies

模拟会话

做模拟登陆验证requests.Session()

使用Session()维持会话信息

import requests

s = requests.Session()

s.get('http://httpbin.rg/cookies/set/number/123456789')

response = s.get('http://httpbin.org/cookies')

print(response.text)

# 证书验证

import requests

from requests.packages import urllib3

urllib3.disable_warnings()           #这两行为了忽略warning

response = requests.get('http://www.12306.cn',verify=False)   #这里必须把verify设置为False，默认为Ture，可以跳过验证证书，如果网站证书是非官方授权，为非法证书，不修改此处会报错。

print(response.status_code)


## 指定本地CA证书,使用cert
import requests

response = requests.get('http://www.12306.cn',cert=('/path/server.crt','/path/key'))

print(response.status_code)


# 代理设置
声明一个字典类型的变量

import requests

proxies = {
    'http':'http://127.0.0.1:9743',
    
   'http':'http://127.0.0.1:9743',
}

response = requests.get('http://www.taobao.com',proxies=proxies)

print(response.status_code)
