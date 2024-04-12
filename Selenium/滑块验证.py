import re
from time import sleep
from urllib.request import urlretrieve
import requests
import time
import random

from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.options import Options
import cv2 as cv


# 初始化
def init():
    # 定义为全局变量，方便其他模块使用
    global url, browser, username, password, wait, options, headers
    # 登录界面的url
    url = ''

    agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 '
             'Safari/537.36 Edg/123.0.0.0')
    headers = {
        'User-Agent': agent
    }
    options = Options()
    options.add_argument('lang=zh_CN.UTF-8')
    # options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    # options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    options.add_argument('--start-maximized')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0')
    # options.add_experimental_option()

    # 实例化一个Edge浏览器
    browser = webdriver.Edge(options=options)
    # browser.add_cookie(cookie)
    # 用户名
    username = ''
    # 密码
    password = ''
    # 设置等待超时
    wait = WebDriverWait(browser, 20)


# 登录
def enterinfo():
    browser.get(url)
    print("打开登录页面,执行成功")
    browser.maximize_window()
    print("最大化窗口,执行成功")
    ActionChains(browser).send_keys(Keys.TAB * 2)
    ActionChains(browser).perform()
    print("切换输入,识别动态加载元素,执行成功")

    element1 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div['
                                                                    '1]/div/form/div[1]/div[2]/div/div/div/input')))
    print("获取用户名输入框,执行成功")
    element1.send_keys(username)
    print("自动输入用户名,执行成功")

    ActionChains(browser).send_keys(Keys.TAB)
    ActionChains(browser).perform()
    print("切换输入,识别动态加载元素,执行成功")

    element2 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div[1]/div/form/div['
                                                                    '2]/div[2]/div/div/div/input')))

    print("获取密码输入框,执行成功")
    element2.send_keys(password)
    print("自动输入密码,执行成功")

    print("等待5S")
    sleep(5)
    ActionChains(browser).send_keys(Keys.TAB)
    ActionChains(browser).perform()
    # print("开始执行登录尝试")

    print("滑块验证开始")
    element3 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="captcha"]/div[1]/div[2]/div[2]')))
    ActionChains(browser).move_to_element(element3).perform()
    ActionChains(browser).send_keys(Keys.ENTER)
    ActionChains(browser).perform()

    print("开始获取背景图")
    element4 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div["
                                                                    "1]/div/form/div[3]/div[2]/div/div/div/div["
                                                                    "1]/div/div[1]/img[1]"))).get_attribute("src")

    with open('verify1.jpg', 'wb') as f:
        f.write(requests.get(element4, headers=headers).content)

    print("开始获取滑块图")
    element5 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div["
                                                                    "1]/div/form/div[3]/div[2]/div/div/div/div["
                                                                    "1]/div/div[1]/img[2]"))).get_attribute("src")

    with open('verify2.jpg', 'wb') as f:
        f.write(requests.get(element5, headers=headers).content)

    # fullbg_image = Image.open('verify1.jpg')
    # bg_image = Image.open('verify2.jpg')

    # //*[@id="captcha"]/div[1]/div[1]/div[1]/div[1]
    # //*[@id="captcha"]/div[1]/div[1]/div[1]/div[1]/img[2]

    # sleep(10)

    # ActionChains(browser).send_keys(Keys.ENTER)
    # ActionChains(browser).send_keys(Keys.TAB)
    # ActionChains(browser).perform()
    # print("滑块验证")

    # print("开始执行登录尝试")
    # ActionChains(browser).send_keys(Keys.TAB * 2)
    # ActionChains(browser).send_keys(Keys.ENTER)
    # ActionChains(browser).perform()
    # print("滑块验证")

    # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_panel')))

    # sleep(200)

    # button_loginclick = browser.find_element(By.CLASS_NAME, 'rock-btn rock-btn-primary rock-btn-sm '
    #                                                         'apc3-external-login-index-left-form-button')
    # button_loginclick.click()
    # sleep(5)


# 获取图片信息
def get_image_info(img):
    '''
    :param img: (Str)想要获取的图片类型：带缺口、原始
    :return: 该图片(Image)、位置信息(List)
    '''

    # 将网页源码转化为能被解析的lxml格式
    soup = BeautifulSoup(browser.page_source, 'lxml')
    # 获取验证图片的所有组成片标签
    imgs = soup.find_all('div', {'class': 'gt_cut_' + img + '_slice'})
    # 用正则提取缺口的小图片的url，并替换后缀
    img_url = re.findall('url\(\"(.*)\"\);', imgs[0].get('style'))[0].replace('webp', 'jpg')
    # 使用urlretrieve()方法根据url下载缺口图片对象
    urlretrieve(url=img_url, filename=img + '.jpg')
    # 生成缺口图片对象
    image = Image.open(img + '.jpg')
    # 获取组成他们的小图片的位置信息
    position = get_position(imgs)
    # 返回图片对象及其位置信息
    return image, position


# 获取小图片位置
def get_position(img):
    '''
    :param img: (List)存放多个小图片的标签
    :return: (List)每个小图片的位置信息
    '''

    img_position = []
    for small_img in img:
        position = {}
        # 获取每个小图片的横坐标
        position['x'] = int(re.findall('background-position: (.*)px (.*)px;', small_img.get('style'))[0][0])
        # 获取每个小图片的纵坐标
        position['y'] = int(re.findall('background-position: (.*)px (.*)px;', small_img.get('style'))[0][1])
        img_position.append(position)
    return img_position


# 裁剪图片
def Corp(image, position):
    '''
    :param image:(Image)被裁剪的图片
    :param position: (List)该图片的位置信息
    :return: (List)存放裁剪后的每个图片信息
    '''

    # 第一行图片信息
    first_line_img = []
    # 第二行图片信息
    second_line_img = []
    for pos in position:
        if pos['y'] == -58:
            first_line_img.append(image.crop((abs(pos['x']), 58, abs(pos['x']) + 10, 116)))
        if pos['y'] == 0:
            second_line_img.append(image.crop((abs(pos['x']), 0, abs(pos['x']) + 10, 58)))
    return first_line_img, second_line_img


# 拼接大图
def put_imgs_together(first_line_img, second_line_img, img_name):
    '''
    :param first_line_img: (List)第一行图片位置信息
    :param second_line_img: (List)第二行图片信息
    :return: (Image)拼接后的正确顺序的图片
    '''

    # 新建一个图片，new()第一个参数是颜色模式，第二个是图片尺寸
    image = Image.new('RGB', (260, 116))
    # 初始化偏移量为0
    offset = 0
    # 拼接第一行
    for img in first_line_img:
        # past()方法进行粘贴，第一个参数是被粘对象，第二个是粘贴位置
        image.paste(img, (offset, 0))
        # 偏移量对应增加移动到下一个图片位置,size[0]表示图片宽度
        offset += img.size[0]
    # 偏移量重置为0
    x_offset = 0
    # 拼接第二行
    for img in second_line_img:
        # past()方法进行粘贴，第一个参数是被粘对象，第二个是粘贴位置
        image.paste(img, (x_offset, 58))
        # 偏移量对应增加移动到下一个图片位置，size[0]表示图片宽度
        x_offset += img.size[0]
    # 保存图片
    image.save(img_name)
    # 返回图片对象
    return image


# 判断像素是否相同
def is_pixel_equal(bg_image, fullbg_image, x, y):
    """
    :param bg_image: (Image)缺口图片
    :param fullbg_image: (Image)完整图片
    :param x: (Int)位置x
    :param y: (Int)位置y
    :return: (Boolean)像素是否相同
    """

    # 获取缺口图片的像素点(按照RGB格式)
    bg_pixel = bg_image.load()[x, y]
    # 获取完整图片的像素点(按照RGB格式)
    fullbg_pixel = fullbg_image.load()[x, y]
    # 设置一个判定值，像素值之差超过判定值则认为该像素不相同
    threshold = 60
    # 判断像素的各个颜色之差，abs()用于取绝对值
    if (abs(bg_pixel[0] - fullbg_pixel[0] < threshold) and abs(bg_pixel[1] - fullbg_pixel[1] < threshold) and abs(
            bg_pixel[2] - fullbg_pixel[2] < threshold)):
        # 如果差值在判断值之内，返回是相同像素
        return True

    else:
        # 如果差值在判断值之外，返回不是相同像素
        return False


# 计算滑块移动距离
def get_distance(bg_image, fullbg_image):
    '''
    :param bg_image: (Image)缺口图片
    :param fullbg_image: (Image)完整图片
    :return: (Int)缺口离滑块的距离
    '''

    # 遍历像素点横坐标
    for i in range(0, fullbg_image.size[0]):
        # 遍历像素点纵坐标
        for j in range(fullbg_image.size[1]):
            # 如果不是相同像素
            if not is_pixel_equal(fullbg_image, bg_image, i, j):
                # 返回此时横轴坐标就是滑块需要移动的距离
                return i


# 构造滑动轨迹
def get_tracks(distance):
    '''
    :param distance: (Int)缺口离滑块的距离
    :return: (List)移动轨迹
    '''

    # # 创建存放轨迹信息的列表
    # tracks = []
    # # 设置加速的距离
    # faster_distance = distance * (4 / 5)
    # # 设置初始位置、初始速度、时间间隔
    # start, v0, t = 0, 0, 0.2
    # # 当尚未移动到终点时
    # while start < distance:
    #     # 如果处于加速阶段
    #     if start < faster_distance:
    #         # 设置加速度为2
    #         a = 2
    #     # 如果处于减速阶段
    #     else:
    #         # 设置加速度为-3
    #         a = -3
    #     # 移动的距离公式
    #     move = v0 * t + 1 / 2 * a * t * t
    #     # 此刻速度
    #     v = v0 + a * t
    #     # 重置初速度
    #     v0 = v
    #     # 重置起点
    #     start += move
    #     # 将移动的距离加入轨迹列表
    #     tracks.append(round(move))
    # # 返回轨迹信息
    # return tracks

    v = random.randint(0, 1)
    t = 1
    tracks = []
    cur = 0
    mid = distance * 0.8
    while cur < distance:
        if cur < mid:
            a = random.randint(2, 3)
        else:
            a = -random.randint(2, 3)
        s = v * t + 0.5 * a * t ** 2
        cur += s
        v = v + a * t
        tracks.append(round(s))
    tracks.append(distance - sum(tracks))
    return tracks

    # tracks = []
    # current = 0
    # mid = distance * 3 / 4
    # t = 0.2
    # v = 0
    # while current < distance:
    #     if current < mid:
    #         a = 2
    #     else:
    #         a = -3
    #     v0 = v
    #     v = v0 + a * t
    #     move = v0 * t + 1 / 2 * a * t * t
    #     current += move
    #     tracks.append(round(move))
    # return tracks


# 模拟拖动
def move_to_gap(tracks):
    # 得到滑块标签
    slider = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="captcha"]/div[1]/div[2]/div[2]')))
    # 使用click_and_hold()方法悬停在滑块上，perform()方法用于执行
    ActionChains(browser).click_and_hold(slider).perform()
    for x in tracks:
        # 使用move_by_offset()方法拖动滑块，perform()方法用于执行
        ActionChains(browser).move_by_offset(xoffset=x, yoffset=1).perform()
        time.sleep(random.randint(10, 50) / 100)
    # 模拟人类对准时间
    # sleep(0.5)
    # 释放滑块
    ActionChains(browser).release().perform()


def match_picture():  # 读取背景图片和缺口图片
    full_image = cv.imread('verify1.jpg')
    slider_image = cv.imread('verify2.jpg')  # 识别图片边缘，获取灰度图
    full_image_edge = cv.Canny(full_image, 100, 200)
    slider_image_edge = cv.Canny(slider_image, 100, 200)
    cv.imwrite("full_image_edge.png", full_image_edge)
    cv.imwrite("slider_image_edge.png", slider_image_edge)
    # 转换图片格式,灰度图像转换为 RGB 彩色图像，以便于与其他彩色图像进行叠加或处理
    # !!!很关键！否则缺口匹配将不准确
    full_image_grey = cv.cvtColor(full_image_edge, cv.COLOR_GRAY2RGB)

    slider_image_grey = cv.cvtColor(slider_image_edge, cv.COLOR_GRAY2RGB)
    cv.imwrite("full_image_grey.png", full_image_grey)
    cv.imwrite("slider_image_grey.png", slider_image_grey)  # 缺口匹配

    res = cv.matchTemplate(full_image_grey, slider_image_grey, cv.TM_CCOEFF_NORMED)  # 寻找最优匹配
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # print("移动距离为", max_loc[0])
    return max_loc[0]  # 判断是否完成操作





# 主程序
def main():
    # 初始化
    init()
    # 登录
    enterinfo()
    # # 获取缺口图片及其位置信息
    # bg, bg_position = get_image_info('bg')
    # 获取完整图片及其位置信息
    # fullbg, fullbg_position = get_image_info('fullbg')
    # # 将混乱的缺口图片裁剪成小图，获取两行的位置信息
    # bg_first_line_img, bg_second_line_img = Corp(bg, bg_position)
    # # 将混乱的完整图片裁剪成小图，获取两行的位置信息
    # fullbg_first_line_img, fullbg_second_line_img = Corp(fullbg, fullbg_position)
    # 根据两行图片信息拼接出缺口图片正确排列的图片
    # bg_image = put_imgs_together(bg_first_line_img, bg_second_line_img, 'bg.jpg')
    # # 根据两行图片信息拼接出完整图片正确排列的图片
    # fullbg_image = put_imgs_together(fullbg_first_line_img, fullbg_second_line_img, 'fullbg.jpg')

    # fullbg_image = Image.open('verify1.jpg')
    # bg_image = Image.open('verify2.jpg')

    # 计算滑块移动距离
    # distance = get_distance(bg_image, fullbg_image)
    distance = int(match_picture() * 308 / 389)
    print("滑块移动距离为： ", distance)
    # 计算移动轨迹
    tracks = get_tracks(distance)
    print("滑块移动轨迹为： ", tracks)
    tracks.append(17)
    print("开始移动滑块")
    # 移动滑块
    move_to_gap(tracks)
    sleep(2)
    print("点击登录")
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[1]/div[1]/button[2]'))).click()
    sleep(200)


# 程序入口
if __name__ == '__main__':
    main()
