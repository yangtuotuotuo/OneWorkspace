# -*-coding:utf-8 -*-
from selenium import webdriver
import time

#打开浏览器
driver = webdriver.Firefox()

#窗口最大化
driver.maximize_window()

#打开指定网页
driver.get("http://www.jd.com")

#设置休眠时间，休眠有三种方式

# 1: 固定等待时间 需要倒包time 当网络加载完成,继续休眠设置的等待时间
# import time
# time.sleep(3)
# driver.quit()

# 2: 隐式等待 在打开浏览器的那一刻,和浏览器约定一个时间,当时间到达以后,无论网络加载或者没有加载出来都会往下执行代码
# driver.implicitly_wait(1)
# driver.quit()

# 3:显示等待 设置显示等待, 默认每隔0.5 秒检查一次元素是不是加载成功,如果加载成功,直接执行下面代码,加载不成功继续等待
# 需要导入的包 这个是最自能的等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#判断title是否被加载成功
title = (By.ID,"key")
title = (By.LINK_TEXT,"你好，请登录")#其余6种同左
title = (By.LINK_TEXT,"")

# 设置休眠 20 秒, 每隔 0.5 秒检查一次
WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located(title))

#定位一组元素
cate_menu_items = driver.find_elements_by_class_name("cate_menu_item")
print len(cate_menu_items),cate_menu_items

#点击第一个
cate_menu_items[0].click()

#获取每一个小项目
cate_menu_lks = driver.find_elements_by_class_name("cate_menu_lk")
print len(cate_menu_lks),cate_menu_lks

time.sleep(3)
driver.quit()