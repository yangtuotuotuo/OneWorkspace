#-*- coding:utf_8 -*-

#定义一个类，继承object
class Person(object):

    "所有员工的基类"

    #实例化对象的时候执行的方法，在被实例化的时候执行，这里的self指整个类
    def __init__(self,name):
        self.name = name
        pass
    #定义获取名字的方法
    def getName(self):
        return self.name
    #类里面可以写N个方法

#实例化类同时调用方法
p = Person("lisi")
print p.getName()

#得到name这个属性
print getattr(p,"name")
#判断有没有这个属性
print hasattr(p,"name")
#修改李四为王五，如果没有返回值，反回None
print setattr(p,"name","王五")
print p.getName()

#删除属性
#print delattr(p,"name")
#print p.getName()

#获取类的属性，用来获取当前类的备注
print p.__doc__
#获取类名
print Person.__name__
#获取类的模块
print Person.__module__
#获取类的属性
print Person.__dict__

# java 的的权限有 4种  :
# 1: public  公共的,能够在整个项目里面访问,
# 2: private 私有的,只能够在类本身里面访问,如果外面想访问或者修改属性,需要根据类里面提供的方法去访问
# 3: protact protected 默认的, 在不同包的子类可以访问,但是不同包的非子类不能够访问
# 4: default 同一个类和同一个包的成员能够访问

# python 权限有:私有的,protected,公共的
# 1:私有的 private 以双下划线开头,只允许类本身访问这个变量
# 2:protected 以单下划线开头,允许其本身与子类进行访问,不能用于 from module import * 注意 型号代表导入所有快
# 3:默认的是公共的,都可以访问

class Student(object):
    #定义类变量
    #公共对外访问的
    name = "李四"
    #私有的只有类本身可以访问，使用双下划线
    __age = 18

    def getName(self):

        return name;

    #定义一个访问age的方法
    def getAge(self):

        return self.__age

#实例化学生对象
s = Student()
#输出名字
print s.name
#输出年龄
print s.getAge()
#正则表达式