# Spider-
# 记录爬虫
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


# 储存一个list

使用pickle，将列表储存在文件中:

import pickle

my_list = ['Fred', 73, 'Hello there', 81.9876e-13]

pickle_file = open('my_pickled_list.pkl', 'wb')

pickle.dump(my_list, pickle_file)

pickle_file.close()

# 还原

使用load(),为这个函数提供一个文件对象(对应包含被pickle了的文件)，它会按照原来的格式返回数据：

import pickle

pickle_file = open('my_pickled_list.pkl', 'rb')

recovered_list = pickled.load(pickle_file)

pickle_file.close()

print(recovered_list)

# (上面"w"和"r"后都加了b，因为pickle存储方式默认是二进制方式,不用二进制方式打开就会报错，所以后面加上"b")
# (TypeError: write() argument must be str, not bytes)
(这是py2和py3的区别)

# 写一个简单的分布式知乎爬虫
https://www.jianshu.com/p/a2a07ed07161


# 记一次分布式B站爬虫任务系统的完整设计和实施
https://www.cnblogs.com/printhelloworld/p/6944343.html


# AttributeError: 'module' object has no attribute 'urlopen'

import urllib.request

url = 'http://www.baidu.com/'

html = urllib.request.urlopen(url).read()

print(html)

urllib库中属性不存在urlopen

AttributeError: 'module' object has no attribute 'urlopen'

官方3.0版本已经把urllib2,urlparse等五个模块都并入了urllib中，也就是整合了。

import urllib.request 

url="http://www.baidu.com"

get=urllib.request.urlopen(url).read() 

print(get)
