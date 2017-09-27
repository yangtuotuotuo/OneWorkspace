#-*- coding:utf-8 -*-
from selenium import webdriver
#休眠包
import time

#当没有点击搜索按钮的时候，导入Keys包，模拟enter键
from selenium.webdriver.common.keys import Keys
# 鼠标事件要导入的包
from selenium.webdriver.common.action_chains import ActionChains

#打开浏览器
driver = webdriver.Firefox()

#######################################################基本操作######################################################################
#WebDriver类型
print type (webdriver)
#定义一个url
url = "http://www.baidu.com"
#打开指定网页
time.sleep(2)
driver.get(url)
# # 查找控件登陆方式有8 种  id name class xpath tag link  party_link css
# #通过id查找内容
# id = driver.find_element_by_id("kw")
# #向里面输入内容
# time.sleep(2)
# id.send_keys(u"未解之谜")
# #通过class查找元素
# time.sleep(3)
# #点击查找
# driver.find_element_by_id("su").click()
#
#
# #等待三秒后刷新页面
# time.sleep(3)
# driver.refresh()
# #返回上一个页面
# time.sleep(2)
# driver.back()
# #到下一个页面
# time.sleep(2)
# driver.forward()
# #设置窗口大小
# time.sleep(2)
# driver.set_window_size(540,960)
# #窗口最大化
# time.sleep(2)
# driver.maximize_window()

############################################################################################################################################

# #获取html的头部
# title = driver.title
# print title
#
# #获取当前页面的url，俗称域名
# util = driver.current_url
# print util
#
#
# #获取输入框（元素）的尺寸大小，返回的是字典{'width': 500, 'height': 22}，可以通过key取出值
# size = driver.find_element_by_id("kw").size
# print size
#
# #取字典里面所有的值
# print size.values()
#
# # 通过key取值
# print size['width'],size['height'],type(size['height'])
#
# #获取标签中间的汉字
# text = driver.find_element_by_class_name("mnav")
# print text.text#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# driver.quit()




#######################################################鼠标键盘的操作######################################################################
# driver.get("http://www.hordehome.com")
# 键盘事件

#设置等待超时
# driver.implicitly_wait(10)
# driver.find_element_by_xpath("//section/div/div[1]/header/div/div/div[2]/ul/li[1]/a/i").click()
# driver.find_element_by_id("search-term").clear()
# driver.find_element_by_id("search-term").send_keys("selenium")
# #当没有点击搜索按钮的时候，导入Keys包，模拟enter键
# element = driver.find_element_by_id("search-term").send_keys(Keys.ENTER)
#其他常见的键盘操作
# 键盘F1~F12
# send_keys(Keys.F1)~send_keys(Keys.F12)
# 复制send_keys(Keys.CONTROL,'c')
# 粘贴send_keys(Keys.CONTROL,'v')
# 全选send_keys(Keys.CONTROL,'a')
# 剪切send_keys(Keys.CONTROL,'x')
# send_keys(Keys.TAB)
#########################################################################################################################################



# 鼠标事件
# perform()执行所有的ActionChains中的行为

# 鼠标悬停
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# driver.implicitly_wait(10)
#鼠标悬停在搜索设置按钮上
# mouse = driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(mouse).perform()
# 双击鼠标左键
# ActionChains(driver).double_click(text).perform()

#点击鼠标右键
# ActionChains(driver).context_click().perform()

###############################################################################################################

#使用for循环进行页面下拉

driver.get("http://jd.com")
driver.maximize_window()

time.sleep(2)
number = 700

#获取浏览器的宽度和高度
height = driver.get_window_size()["height"]
width = driver.get_window_size()["width"]

print height,width

for index in range(0,5):

    js = "var q=document.documentElement.scrollTop="+str(height*index)
    driver.execute_script(js)

time.sleep(5)
###为什么下拉的时候卡顿，不流畅？？？？？？

###############################################################################################
#获取输入框的值，通过属性获取
# time.sleep(5)
# key = driver.find_element_by_id("kw")
# print key.get_attribute("autocomplete")
#
# #获取输入框的类型
# print key.get_attribute("type")
#
# #获取class的值
# print key.get_attribute("class")
#
# #判断元素设不是可见的
# print key.is_displayed()

driver.quit()