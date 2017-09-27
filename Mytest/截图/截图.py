#-*- coding:utf-8 -*-

# 截图方法的使用

from selenium import webdriver
# 导入系统包
import os
# 导入休眠包
import time

# 打开浏览器
driver = webdriver.Firefox()

# 最大化
driver.maximize_window()

# 打开网页
driver.get("http://www.jd.com")

#进行截图
#获取当前文件夹的名字
filename = os.getcwd()
print filename

#获取一张图片，保存到当前文件夹所在路径
driver.get_screenshot_as_file(filename+'/img.jpg')


# #截屏后保存图片到指定文件所在路径
driver.get_screenshot_as_file(u"D:\python_img\未解之谜.jpg")



driver.quit()