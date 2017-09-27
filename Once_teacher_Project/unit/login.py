#-*- coding:utf-8 -*-
# 倒包
# 导入休眠包
import time
# 导入单元测试包
import unittest

from selenium import webdriver

# 倒包
from Once_teacher_Project.util import urlutil


# 定义类继承单元测试
class Login(unittest.TestCase):


    #测试用例执行的方法
    def setUp(self):

        # 打开浏览器 self 代表类本身,代表将driver赋值给这个类
        self.driver = webdriver.Firefox()
        # 设置窗口最大化
        self.driver.maximize_window()
        # 打开指定网页
        self.driver.get(urlutil.JD_LOGIN + urlutil.LOGIN)
        # 休眠五秒
        time.sleep(5)

        # 开始查找控件
        # 切换到用户登陆模块
        self.login_tab_r = self.driver.find_element_by_class_name("login-tab-r")
        # 点击一下
        self.login_tab_r.click()

        # 查找用户名和密码以及登陆按钮
        self.loginname = self.driver.find_element_by_id("loginname")
        self.nloginpwd = self.driver.find_element_by_id("nloginpwd")
        self.loginsubmit = self.driver.find_element_by_id("loginsubmit")
        pass


    #测试用例执行之后的方法
    def tearDown(self):

        # 关闭浏览器
        self.driver.quit()

        pass


    #测试用例登陆
    def test_us_pa_su(self):

        U"""用户名正确,密码正确,点击登陆,跳转到主页"""

        # 输入用户名和密码以及点击登陆
        self.loginname.send_keys("15210033534")
        self.nloginpwd.send_keys('ww970614')
        self.loginsubmit.click()

        # 休眠五秒
        time.sleep(5)

        # 获取标题
        title = self.driver.title

        # 进行断言
        self.assertEqual(title,u"京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！")

        # 使用验证


        pass

    #用户名为空,密码为空,请输入用户名
    def test_us_em_pw_em(self):

        U"""用户名为空,密码为空,点击登陆,应该提示请输入用户名和密码"""

        self.loginname.send_keys("")
        self.nloginpwd.send_keys("")
        self.loginsubmit.click()

        # 休眠五秒
        time.sleep(2)

        # 开始查找控件
        msg_error = self.driver.find_element_by_class_name("msg-error")

        # 获取内容
        message = msg_error.text

        # 进行断言
        self.assertEqual(message,u"请输入账户名和密码")

        pass

    # 软件测试方法 :
    # 1: 等价类 : 有效等价类 和无效等价类 比如要求输入邮箱/用户名/已验证手机 有效等价类是: 正确用户名 正确手机号 正确有限 无效等价类 : 用户名非法字符 邮箱是错误邮箱 手机号是错误手机号
    # 2: 边界值 : 一般情况输入框有规定输入的长度: 比如规定的长度 6 - 20 : 边界值就是 5 7 19 21 ,  其实从 7 - 19 也就是有效等价类 其余的都是无效等价类
    # 3: 错误推断法 :  根据经验去判断是不是符合要求
    # 4: 因故图: 比如输入规定内容,有固定提示 长用于场景测试
    # 5: 判定表驱动法 用于多个场景的组合
    # 6:

    #登陆页面关于我们
    def test_about_me(self):

        # 获取当前窗口
        login_window = self.driver.current_window_handle

        # 查找关于我们的控件
        about_me = self.driver.find_element_by_link_text("关于我们")
        # 点击一下
        about_me.click()
        # 休眠五秒
        time.sleep(5)

        # 获取所有的窗口
        all_window = self.driver.window_handles

        # 使用for循环做判断同时切换窗口
        for window in all_window:

            if window != login_window:

                #切换窗口
                self.driver.switch_to_window(window)
                # 获取标题
                about_title = self.driver.title
                #使用断言
                self.assertEqual(about_title,u'企业简介-京东商城')

        pass



