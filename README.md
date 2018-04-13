# Spider-
# 记录爬虫
https://blog.csdn.net/changjiale110/article/details/76145585 


爬虫获取headers作为代理 用浏览器打开需要url ，点击f12或右键检查（chrome） 点击 network –> Doc 点击f5 获取内容

拉到最后， 我们看到了我们看到 request headers内的信息 我门拉取其中2个使用 user-agent: 和 accept:

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
