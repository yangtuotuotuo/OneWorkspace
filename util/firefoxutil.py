#-*- coding:utf-8 -*-
###


# 封装思想
# 1: 高内聚 低耦合
# 2: 测试用例与逻辑代码的分离
# 3: 以面向对象的思想写脚本
# 4: mvc 模型搭建框架  m model层 也就是数据层 v view 视图展示层,对应的是咱们这里的单元测试层  c control 控制层, 对应的是逻辑控制层

# 1: 高内聚的具体体现 : 把竟可能关联的代码放在一个类里面,封装成各种方法,


# 倒包
from selenium import webdriver
# 导入休眠包
import time
# 导入枚举包
from enum import Enum
# 导入三个包
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 定义一个类继承 object
class startFirfox2(object):

    # 类被实例化的时候执行的方法
    def __init__(self):

        # 将枚举实例化
        # 在 Java中实例化需要使用的关键字叫 new , 在python 中不需要使用关键字,直接类型()


        pass


    # 打开浏览器打开了方法
    # 1: 在Java中叫方法 在Python 中叫函数
    # 2: 在Java中关键字是public void 方法名字 在python 中关节字det
    # 3: 在Java中如果有返回类型,需要制定返回类型 在python 中是不需要指定返回类型

    # 注意 self 指定的类本身,如果把值复制给self,也就是整个类都可以使用
    def startFirFox1(self,url):

        # 打开浏览器
        self.driver = webdriver.Firefox()
        # 设置窗口最大化
        self.driver.maximize_window()
        # 打开指定网页
        self.driver.get(url)
        # 设置等待时间
        # self.WebWait(self.driver.title)
        self.ImplaySleep(ENUM.FIVE_TIME)
        pass

    # 关闭浏览器的方法
    def closeFirFox(self):

        self.driver.quit()

    # 休眠方法 三种 1: 静止休眠 2 : 隐士休眠  3: 显示休眠

    def TimeSleep(self,number):

        time.sleep(number)


    #隐士休眠
    def ImplaySleep(self,number):

        self.driver.implicitly_wait(number)

    # 显示休眠
    def WebWait(self,message):

        # 查找内容
        text = (By.LINK_TEXT,message)
        # 设置休眠时间
        WebDriverWait(self.driver,ENUM.TWENTY_TIME,ENUM.ZONE_TIME).until(EC.presence_of_element_located(text))


        pass

    # 查找控件的方式
    def FindId(self,ID):

        try:

            # 查找内容
            ids = (By.ID, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))

            return self.driver.find_element_by_id(ID)

        except Exception:

            return Exception



    # 查找控件的方式

    def FindName(self, ID):

        try:

            # 查找内容
            ids = (By.NAME, ID)
            # 设置休眠时间
            WebDriverWait(self.driver,ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_element_by_name(ID)

        except Exception:

            return Exception

    # 查找控件的方式

    def FindClass(self, ID):

        try:

            # 查找内容
            ids = (By.CLASS_NAME, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_element_by_class_name(ID)

        except Exception:

            pass

    # 查找控件的方式

    def FindLink(self, ID):

        try:

            # 查找内容
            ids = (By.LINK_TEXT, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_element_by_link_text(ID)

        except Exception:

            pass# 查找控件的方式

    def FindPartty(self, ID):

        try:

            # 查找内容
            ids = (By.PARTIAL_LINK_TEXT, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_element_by_partial_link_text(ID)

        except Exception:

            pass# 查找控件的方式

    def FindXpath(self, ID):

        try:

            # 查找内容
            ids = (By.XPATH, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_element_by_xpath(ID)

        except Exception:

            pass

    # 查找控件的方式

    def FindCss(self, ID):

        try:

            # 查找内容
            ids = (By.CSS_SELECTOR, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_element_by_css_selector(ID)

        except Exception:

            pass

    # 查找控件的方式
    def FindIds(self, ID):

        try:

            # 查找内容
            ids = (By.ID, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_elements_by_id(ID)

        except Exception:

            pass

    # 查找控件的方式

    def FindNames(self, ID):

        try:

            # 查找内容
            ids = (By.NAME, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_elements_by_name(ID)

        except Exception:

            pass

    # 查找控件的方式

    def FindClasses(self, ID):

        try:

            # 查找内容
            ids = (By.CLASS_NAME, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_elements_by_class_name(ID)

        except Exception:

            pass

    # 查找控件的方式

    def FindLinks(self, ID):

        try:

            # 查找内容
            ids = (By.LINK_TEXT, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_elements_by_link_text(ID)

        except Exception:

            pass  # 查找控件的方式

    def FindParttys(self, ID):

        try:

            # 查找内容
            ids = (By.PARTIAL_LINK_TEXT, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_elements_by_partial_link_text(ID)

        except Exception:

            pass  # 查找控件的方式

    def FindXpaths(self, ID):

        try:

            # 查找内容
            ids = (By.XPATH, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_elements_by_xpath(ID)

        except Exception:

            pass

    # 查找控件的方式

    def FindCsses(self, ID):

        try:

            # 查找内容
            ids = (By.CSS_SELECTOR, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(
                EC.presence_of_element_located(ids))

            return self.driver.find_elements_by_css_selector(ID)

        except Exception:

            pass

    # 点击方法的封装
    def ClickId(self,ID):

        self.FindId(ID).click()

        self.TimeSleep(ENUM.TWO_TIME)

        pass

    # 点击方法的封装
    def ClickClass(self, Cls):

        self.FindClass(Cls).click()

        self.TimeSleep(ENUM.TWO_TIME)

        pass




# 定义一个枚举类
class ENUM(Enum):

    #一分钟
    OND_TIME = 1
    # 二分钟
    TWO_TIME = 2
    # 五分钟
    FIVE_TIME = 5
    # 十分钟
    TEN_TIME = 10
    # 二十分钟
    TWENTY_TIME = 20
    # 0.5 秒
    ZONE_TIME = 0.5

