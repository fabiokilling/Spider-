from selenium import webdriver
options = webdriver.ChromeOptions()
options.set_headless()
driver = webdriver.Chrome(options=options)
#至此已完成
 driver.get('http://www.baidu.com')
 driver.page_source
