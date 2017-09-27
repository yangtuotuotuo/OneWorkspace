# -*-coding:utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.maximize_window()

driver.get("http://www.jd.com")

# 查找控件输入袜子
time.sleep(2)
key = driver.find_element_by_id("key")
key.send_keys(u"袜子")

key.send_keys(Keys.ENTER)

#休眠5秒
time.sleep(5)

#查找列表展示控件
m_list = driver.find_element_by_class_name("m-list")

#通过js首先定位
driver.execute_script("arguments[0].scrollIntoView(true)",m_list)

#获取当前title
title = driver.title

print title

#切换窗口，首先需要获取当前窗口
jd_window = driver.current_window_handle

#开始查找控件点击详情
p_name = driver.find_elements_by_class_name("p-img")

#点击第五个
p_name[5].click()
time.sleep(2)

#获取所有窗口
windows = driver.window_handles

#切换到自己的窗口
for s_window in windows:
    if s_window != jd_window:
        #切换页面
        driver.switch_to_window(s_window)
        #获取title
        d_title = driver.title
        print d_title

        #查找控件，通过js进行定位
        crumb_wrap = driver.find_element_by_id("crumb-wrap")
        #进行定位
        driver.execute_script("arguments[0].scrollIntoView(true)",crumb_wrap)

        title = driver.title
        print title

        time.sleep(2)

        driver.quit()