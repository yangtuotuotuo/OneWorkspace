#-*- coding:utf-8 -*-
import unittest
# 倒包
from util import firefoxutil,urlutil
# 导入逻辑控制层的包
from loginjd.control import logincontrol

# 定义类继承单元测试
class Login(unittest.TestCase):


    @classmethod
    def setUpClass(self):

        # 实例化浏览器的类
        self.firfox = firefoxutil.startFirfox2()

        # 实例化url
        self.URL = urlutil.URL()



        pass


    def setUp(self):

        # 打开浏览器
        self.firfox.startFirFox1(self.URL.JD_LOGIN)

        # 实例化控制类
        self.login = logincontrol.LoginControl(self.firfox)

        pass


    def tearDown(self):

        # 关闭浏览器
        self.firfox.closeFirFox()

        pass

    # @classmethod
    # def tearDownClass(self):
    #
    #     # 销毁对象
    #
    #     pass

    def test_us_em_pw_em(self):

        # 输入内容
        self.login.LoginClick('','')
        # 进行断言
        self.login.LoginAssertToast(self,"请输入账户名和密码")


        pass

    def test_us_pw(self):

        # mvc 思想搭建框架

        # 需要封装c层




        pass


