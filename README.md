# Spider-

## 记录爬虫

https://blog.csdn.net/changjiale110/article/details/76145585 

爬虫获取headers作为代理 用浏览器打开需要url ，点击f12或右键检查（chrome） 点击 network –> Doc 点击f5 获取内容

拉到最后， 我们看到了我们看到 request headers内的信息 我门拉取其中2个使用 user-agent: 和 accept:

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8

Accept-Encoding: gzip, deflate, br

Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8,it;q=0.7,en;q=0.6

Cache-Control: max-age=0

Connection: keep-alive

Host: www.zhihu.com

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36

## 储存一个list

使用pickle，将列表储存在文件中:

import pickle

my_list = ['Fred', 73, 'Hello there', 81.9876e-13]

pickle_file = open('my_pickled_list.pkl', 'wb')

pickle.dump(my_list, pickle_file)

pickle_file.close()

## 还原

使用load(),为这个函数提供一个文件对象(对应包含被pickle了的文件)，它会按照原来的格式返回数据：

import pickle

pickle_file = open('my_pickled_list.pkl', 'rb')

recovered_list = pickled.load(pickle_file)

pickle_file.close()

print(recovered_list)

(上面"w"和"r"后都加了b，因为pickle存储方式默认是二进制方式,不用二进制方式打开就会报错，所以后面加上"b")

(TypeError: write() argument must be str, not bytes)

(这是py2和py3的区别)

## 写一个简单的分布式知乎爬虫

https://www.jianshu.com/p/a2a07ed07161

## 记一次分布式B站爬虫任务系统的完整设计和实施

https://www.cnblogs.com/printhelloworld/p/6944343.html

## 出现报错

(AttributeError: 'module' object has no attribute 'urlopen')

### (Python2用法)

import urllib2  

response = urllib2.urlopen('http://www.baidu.com/')  

html = response.read()  

print html  

### (Python3用法)

import urllib.request

url = 'http://www.baidu.com/'

html = urllib.request.urlopen(url).read()

print(html)

'''

urllib库中属性不存在urlopen

AttributeError: 'module' object has no attribute 'urlopen'

官方3.0版本已经把urllib2,urlparse等五个模块都并入了urllib中，也就是整合了。

'''

import urllib.request 

url="http://www.baidu.com"

get=urllib.request.urlopen(url).read() 

print(get)

## selenium

(驱动浏览器，自动化测试，js渲染的网页无法用requests请求去正常去获取请求内容，selenium能驱动浏览器去执行js渲染，得到渲染后的页面，拿到js渲染后的内容)

import selenium

from selenium import webdriver

driver = webdriver.Chrome()

(如果这里提示找不到指定的文件，是因为Chromedriver没有安装)

UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead

使用Selenium要用PhantomJS来进行无界面模式的自动化测试，或者爬取某些动态页面

但是从某版本开始Selenium不支持PhantomJs，请使用headless模式

### Chrome

from selenium import webdriver

options=webdriver.ChromeOptions()

options.set_headless()

'''

options.add_argument(‘--headless‘)

'''

options.add_argument(‘--disable-gpu‘)    

'''

关闭GPU加速

'''

driver=webdriver.Chrome(options=options)

driver.get(‘http://httpbin.org/user-agent‘)

driver.get_screenshot_as_file(‘test.png‘)

driver.close()

不支持PhantomJs后处理方法的详情http://www.mamicode.com/info-detail-2193163.html

## 储存（Python os.mkdir() 方法）


# JSON在线解析

https://www.json.cn/


 pic_url = element_data.xpath('//*[@id="endText"]//img[not(@class="icon")]/@src')

#pic_url = [url for url in pic_url if url.find('css13/img') == -1]  #网易正文通用xpath取图片会取到最后一张会是网易的一个LOGO图片，此处为去最后一张图片

text = html.unescape(text)
去掉前端的类似amp;这种的东西
