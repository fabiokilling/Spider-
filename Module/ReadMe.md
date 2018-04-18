# python爬虫相关库安装

https://www.cnblogs.com/copywang/p/7832527.html

python爬虫涉及的库：

请求库，解析库，存储库，工具库

## 1. 请求库：urllib/re/requests

### A. urllib/re是python默认自带的库，可以通过以下命令进行验证：

import urllib, re

没有报错信息输出，说明环境正常
### B. requests安装

#### 2.1 打开CMD，输入

pip3 install requests

#### 2.2 等待安装后，验证

import requests

### C. selenium安装（驱动浏览器进行网站访问行为）

#### 3.1 打开CMD，输入

pip3 install selenium

#### 3.2 安装chromedriver

网址：https://npm.taobao.org/

把下载完成后的压缩包解压，把exe放到D:\Python3.6.0\Scripts\

这个路径只要在PATH变量中就可以

#### 3.3 等待安装完成后，验证

import selenium

from selenium import webdriver

回车后弹出chrome浏览器界面

#### 3.4 安装其他浏览器(已经没用了)

无界面浏览器phantomjs

下载网址：http://phantomjs.org/

下载完成后解压，把整个目录放到D:\Python3.6.0\Scripts\，把bin目录的路径添加到PATH变量

验证：

打开CMD

phantomjs

console.log('phantomjs')

CTRL+C

python

from selenium import webdriver

driver = webdriver.PhantomJS()

dirver.get('http://www.baidu.com')

driver.page_source

 

## 2. 解析库：

### A. lxml (XPATH)

打开CMD

pip3 install lxml

或者从https://pypi.python.org下载，例如，lxml-4.1.1-cp36-cp36m-win_amd64.whl (md5) ,先下载whl文件

pip3 install 文件名.whl
 
### B. beautifulsoup

打开CMD，需要先安装好lxml

pip3 install beautifulsoup4

验证

from bs4 import BeautifulSoup

soup = BeautifulSoup('<html></html>','lxml')
 

### C. pyquery（类似jquery语法）

打开CMD

pip3 install pyquery

验证安装结果

python

from pyquery import PyQuery as pq

doc = pq('<html>hi</html>')

result = doc('html').text()

result


 

## 3. 存储库

### A. pymysql（操作MySQL，关系型数据库）

安装：

pip3 install pymysql

安装后测试：

打开cmd

import pymysql

con = pymysql.connect(host = 'localhost',user = 'root',password = '123456',port = 3306,db='mysql')

cursor = conn.cursor()

cursor.execute('select * from db')


cursor.fetchone()


打开MySQL-Fronty里连接到localhost

查看mysql里的db，数据浏览器，发现一致

#### 3.2 pymongo（操作MongoDB，key-value）

安装

pip3 install pymongo

验证

import pymongo

client = pymongo.MongoClient('localhost')

db = client['testdb']

db['table'].insert({'name':'bob'})

db['table'].find_one({'name':'bob'})

 

### B. redis（分布式爬虫，维护爬取队列）

安装：

pip3 install redis

验证：

import redis

r = redis.Redis('localhost',6379)

r.set('name','Bob')


r.get('name')




 

## 4.工具库

### A. flask（WEB库）

pip3 install flask


 

### B. Django（分布式爬虫维护系统）

 

pip3 install django
 

### C. jupyter（运行在网页端的记事本，支持markdown，可以在网页上运行代码）

pip3 install jupyter
 
 验证：

打开CMD

jupyter notebook


之后就可以在网页直接创建记事本，代码块和Markdown块，支持打印

