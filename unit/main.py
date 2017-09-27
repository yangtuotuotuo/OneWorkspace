#-*- coding:utf-8 -*-
import unittest

from util import firefoxutil,urlutil

class Main(unittest.TestCase):


    # 所有测试用例执行之前的方法
    @classmethod
    def setUpClass(self):

        # 实例化对象
        self.firfox = firefoxutil.startFirfox2()
        # 实例化url
        self.url = urlutil.URL()

        pass




    # 每一条测试用例执行之前执行的方法
    def setUp(self):

        # 打开浏览器
        self.firfox.startFirFox1(self.url.JD_MAIN)

        pass

    # 关闭浏览器
    def tearDown(self):

        self.firfox.closeFirFox()

        pass


    # 测试用例
    def test_mian(self):

        pass


    # # 所有测试用例执行完的时候执行的方法
    # @classmethod
    # def tearDownClass(self):
    #
    #     # 销毁对象
    #     self.firfox = None
    #
    #     pass

if __name__ == '__main__':

    unittest.main()
