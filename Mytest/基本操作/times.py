#-*- coding:utf-8-*-
import time

#获取时间，时间戳
print time.time()

#获取本地时间
print time.localtime(time.time())

#格式化时间
print time.asctime(time.localtime(time.time()))

#自定义需要的格式
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())


#获取日历
import calendar
cal=calendar.month(2017,9)
print "以下输出2017年9月份的日历"
print cal
print type(cal)


#  在Java中方法 puclic void 方法名字(){} 在python 中方法叫函数, 关键字是 def

#  定义一个函数 无参数函数
def getName():
    return "hello world"
print getName()

#定义一个有参函数
def getName(name):
    return name
print getName("lisi")