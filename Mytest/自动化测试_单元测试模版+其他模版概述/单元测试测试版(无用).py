# -*-coding:utf-8 -*-

# 自动化测试模型有四中
# 1: 线性模型
# 2: 模块化与类库
# 3: 数据驱动
# 4: 关节字驱动

# 5: 单元测试 + 测试套件 (mvc 思想 )+ 自动化测试报告 + 断言

# 使用的思想 :
# 1: 高内聚 低耦合
# 2: 逻辑代码与测试用例的分离
# 3: mvc思想的使用 model层 view层 control层
#  model 层 对应的就是 数据层
#  view 层: 对应的就是单元测试层
#  control层 : 对应的就是逻辑代码层

# 4: 以面向对象的思想写代码

########################################################################################################################

# 在Java中单元测试框架有  jnit4 和 testning

# 在 python 中 单元测试框架有 unittest

# 单元测试里面有几个方法
# python 中 所有的测试用例执行之前执行的方法  setUpClass
#  所有的测试用例执行之后执行的方法 teardowClass
#  每一条测试用例执行之前执行的方法 setUp
#  每一条测试用例执行之后执行的方法 teardown
#  测试用例是以test开头的方法也叫函数
#  测试用例的执行顺序是按照 ASC-II 顺序执行是 0-9 A-Z a-z 执行的



#单元测试的步骤
#导入单元测试包
import unittest

#定义一个类继承unittest
class Person(unittest.TestCase):

    #所有的测试用例执行之前必须执行的方法
    @classmethod
    def setUpClass(cls):
        print "setUpClass"

        # 对象的初始化工作可以在这里完成

        pass

    # 所有测试用例执行之后执行的方法
    @classmethod
    def tearDownClass(cls):
        print "tearDownClass"

        # 销毁对象

        pass

    # 每一条测试用例执行之前执行的方法
    def setUp(self):
        print "setUp"

        # 在这里打开浏览器

        pass

    # 每一条测试用例执行之后执行的方法
    def tearDown(self):
        print "tearDown"

        # 关闭浏览器

        pass

    def test_a(self):
        print "a"

        pass

    def test_b(self):
        print "b"

        pass

    def test_c(self):
        print "c"

        pass

    def test_0(self):
        print "0"

        pass

    def test_A(self):
        print "A"

        pass


#运行单元测试
if __name__ == '__main__':

    unittest.main

# 如果有10个单元测试,如果一块运行,需要 用到测试套件 TestSuit

# 实例化 suit
# 这个叫测试套件, 可以装无数的单元测试
suit = unittest.TestSuite()

# 将单元测试加入到测试套件
suit.addTest(unittest.makeSuite(Person))


# 运行测试套件

# 方法一 不使用 htmltestrunner
if __name__ == '__main__':

    # # 这句话意思通过找suit 运行
    # unittest.main(defaultTest='suit')

    #方法二
    runner = unittest.TextTestRunner()
    #运行suit
    runner.run(suit)
