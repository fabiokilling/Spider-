# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:17:42 2018

@author: bbtree
"""
import os
import requests  
os.makedirs('./png/', exist_ok=True)  
IMAGE_URL = "https://www.baidu.com/img/bd_logo1.png" 
def request_download():   
    res = requests.get(IMAGE_URL)
    with open('./png/1.png', 'wb')as f:
        f.write(res.content)
request_download()
