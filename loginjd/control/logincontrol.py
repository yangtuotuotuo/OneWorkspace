#-*- coding:utf-8 -*-


# 定义一个类继承 object

# 注意在面试的时候问你写过case没有,意思就是写过测试用例

class LoginControl(object):

    # 类被实例化的时候执行
    def __init__(self,fiefox):

        # 实例化打开浏览器的方法
        self.fiefox = fiefox

        pass

    # 同时实现高内聚和低耦合
    # 高内聚的目的是为了调用的时候方便
    # 低耦合的目的是为了组合方便

    # 点击账号登陆的方法
    def LoginClick(self,username,password):


        # 点击
        self.fiefox.FindClass('loginjd-tab-r').click()

        loginname = self.fiefox.FindName("loginname")
        nloginpwd = self.fiefox.FindId("nloginpwd")

        loginname.send_keys(username)
        nloginpwd.send_keys(password)

        # 点击登陆,同时进行休眠
        self.fiefox.ClickClass("loginsubmit")

        pass

    #封装断言
    def LoginAssertToast(self,self1,excepts):

        #开始查找控件
        msg_error = self.fiefox.FindClass("msg-error")
        # 获取上边的内容
        message = msg_error.text
        # 进行断言
        self1.assertEqual(message,excepts)

        pass

