#-*- coding:utf-8 -*-
import time
import unittest

from selenium import webdriver

from Once_teacher_Project.util import urlutil


# 定义类
class Shopping(unittest.TestCase):


    def setUp(self):

        # 打开浏览器 self 代表类本身,代表将driver赋值给这个类
        self.driver = webdriver.Firefox()
        # 设置窗口最大化
        self.driver.maximize_window()
        # 打开指定网页
        self.driver.get(urlutil.JD_MAIN)
        # 休眠五秒
        time.sleep(5)

        pass


    def tearDown(self):

        # 关闭浏览器
        self.driver.quit()

        pass


    def test_shop(self):


        # 查找控件
        self.key = self.driver.find_element_by_id("key")
        self.button = self.driver.find_element_by_class_name("button")

        # 输入袜子
        self.key.send_keys(u"袜子")
        self.button.click()

        # 休眠五秒
        time.sleep(5)

        # 查找控件 进行定位
        self.ml_wrap = self.driver.find_element_by_class_name("ml-wrap")

        # 使用js 脚本进行定位
        self.driver.execute_script('arguments[0].scrollIntoView(true)',self.ml_wrap)

        # 休眠一秒
        time.sleep(1)

        # 获取当前的窗口
        detail_window = self.driver.current_window_handle

        # 查询一组商品
        p_name_type_2s = self.driver.find_elements_by_xpath("//div[@class = 'p-commit']/strong/a")

        # 进行点击第一个商品
        p_name_type_2s[0].click()

        # 休眠
        time.sleep(5)

        # 获取所以的窗口
        all_window = self.driver.window_handles

        # 使用 for循环 判断
        for window in  all_window:

            if window != detail_window:

                self.driver.switch_to_window(window)


        # 获取title
        detail_title = self.driver.title

        # 获取控件内容
        sku_name = self.driver.find_element_by_class_name("sku-name")

        # 使用断言
        self.assertEqual(detail_title,sku_name.text+"【图片 价格 品牌 报价】-京东")

        # 查找 控件
        sh_hd_wrap = self.driver.find_element_by_class_name("sh-hd-wrap")

        # 使用 js定位
        self.driver.execute_script('arguments[0].scrollIntoView(true)',sh_hd_wrap)

        # 休眠10秒
        time.sleep(10)

        # 选择商品
        # 通过 xpath 查找 div,点击第一个选择颜色

        # dds = self.driver.find_elements_by_class_name("item")
        #
        # # 点击第0 个
        # dds[0].click()

        # 查找添加按钮控件
        btn_add = self.driver.find_element_by_class_name("btn-add")

        # 点击一下变成两个
        btn_add.click()

        # 点击加入购物车按钮
        add_shop = self.driver.find_element_by_link_text("加入购物车")

        add_shop.click()

        # 休眠五秒
        time.sleep(5)

        # 去购物车结算
        go_shop = self.driver.find_element_by_link_text("去购物车结算")

        go_shop.click()

        # 休眠五秒
        time.sleep(5)

        #点击去结算
        go_commit = self.driver.find_element_by_link_text("去结算")

        go_commit.click()

        # 休眠五秒
        time.sleep(5)

        # 查找弹窗frame
        dialogIframe = self.driver.find_element_by_id("dialogIframe")

        # 切换进去
        self.driver.switch_to_frame(dialogIframe)

        # 查找
        login_tab_r = self.driver.find_element_by_class_name("login-tab-r")
        # 点击一下
        login_tab_r.click()

        # 开始查找控件
        # 查找用户名和密码以及登陆按钮
        self.loginname = self.driver.find_element_by_id("loginname")
        self.nloginpwd = self.driver.find_element_by_id("nloginpwd")
        self.loginsubmit = self.driver.find_element_by_id("loginsubmit")

        self.loginname.send_keys("15210033534")
        self.nloginpwd.send_keys('ww970614')
        self.loginsubmit.click()

        # 休眠五秒
        time.sleep(5)

        self.assertEqual(self.driver.title,u"订单结算页 -京东商城")


        pass