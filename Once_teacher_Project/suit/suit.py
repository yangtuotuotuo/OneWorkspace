#-*- coding:utf-8 -*-
# 导入自动化测试报告
import HTMLTestRunner
# 设置系统的编码格式
import sys
import unittest

# 导入单元测试
from unit import shopping

reload(sys)
sys.setdefaultencoding('utf-8')


# 实例化套件
suit = unittest.TestSuite()

# 将单元测试加入到测试套件里面
# suit.addTest(unittest.makeSuite(login.Login))
suit.addTest(unittest.makeSuite(shopping.Shopping))

# 指定自动化测试报告的生成路径
filename = "/Users/apple/Desktop/html_src/jd-21.html"
# 指定流的读写模式
output = open(filename,'wb')

# 运行自动化测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=output,title=u"京东登陆",description=u"登陆测试用例")

runner.run(suit)

