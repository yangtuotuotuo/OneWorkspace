#-*- coding:utf-8 -*-
# 导入单元测试框架
import unittest
# 导入单元测试包
from unit import main,login
# 导入自动化测试报告
import HTMLTestRunner
# 导入os 包的
import os

# 实例化suit

#啦啦啦啦啦
suit = unittest.TestSuite()

# 将单元测试添加到测试套件里面
# 低耦合的具体体现 优势在于想运行那个单元测试就可以运行那个单元测试,比较灵活,不会造成别的错误
# suit.addTest(unittest.makeSuite(main.Main))
suit.addTest(unittest.makeSuite(login.Login))

# 指定自动化测试报告位置/路径
filename = os.getcwd()+"/jd.html"
# 指定编码格式 只读 rb 二进制的 wb 只写 二进制 rb+ 可读可写二进制
files = file(filename,'wb')

# 运行单元测试
runner = HTMLTestRunner.HTMLTestRunner(stream=files,title=u"京东",description=u"京东测试报告")

# 运行套件
runner.run(suit)