#coding=utf-8

#输出语句，“你好世界”
print ("你好世界")

# ptyhon 有两个版本,一个是2.7 一个是 3.6 ,一般情况下我们使用2.7 版本的Python

# java 有8 种基本类型 ,python 有五种基本类型

# java 8种

# byte(字节)
# short(短整形)
# int(正行)
# long(长整形)
# double(双精度,Java默认是双精度)
# float(单精度)
# boolean(布尔类型)
#  char(字符类型)

# python 五种类型

# 1: 数字类型 Number (int long float complex(复数类型))
# 2: string 类型
# 3: List(列表类型) 类似于java中的集合
# 4: Tupe(元祖类型)
# 5: Dictionary(字典类型) 类似于Java中的对象

# 数字类型 Number


#年龄一般使用int
age = 18
print age,type(age)


#价格一般使用float
price = 19.99
print price,type(price)


#数字比较大的时候使用长整型，注意L是long类型标识符
count=10000L
print count,type(count)


#复数类型complex，结尾为j
aa=3.14j
print aa,type(aa)


#字符串类型
name1="zhangsan"
name2="张三"
print name1,type(name1)
print name2,type(name2)


#列表类型，在java中必须是同一个类型，而python中不需要是同一类型
list=["张三",'啊啊啊',19.88,'aaa',111111L]
#获取列表长度，在java中要用size,python中用len字段
print len(list)
#获取列表内容
print list[0],list[1],list[2],list[3],list[4]
#打印完整列表
print list
#输出第二到第三个元素，下标是1和3，包左不包右
print list[1:3]


#输出第二个到最后一个的元素
print list[1:]
#打印两次
print list*2


#元组与list的区别就在于list是中括号[]，而元组是小括号，list里面的内容是可以修改的，但是元组里面的内容是不可以修改的
tuple=('张三','lisi',18,20)
#修改list里面的内容
list[0]='李四'
print list[0]
#修改元组里面的内容
#tuple[0]='hh'------->错误的
##################元组获取到的内容与list是一样的######################


#字典类型对应的是java中的Object，字典的标识符是大括号{}
person = {
    'name':'wangwu',
    'sex':'男',
    'age':19,
    'address':'八维'
}
#通过key来获取对象里面内容
print person['name'],person['sex']
#获取所有的键
print person.keys()#获取所有的值
print person.values()
#向字典里面加内容
person['score']=99.0
print person
#修改年龄为99岁
person['age']=99
print person


#数据类型的转换
age='18'
print age,type(age)
#将str类型转换为int类型
print age,type(int(age))


#运算符
# 1: 算数运算符
# 2: 比较运算符
# 3: 逻辑运算符
# 4: 复制运算符
# 5: 位运算符
# 6: 成员运算符
# 7: 身份运算符
# 8: 运算符优先级

# 1: 算符运算符 +(加) -(减) *(乘) /(除) **(幂) //(取整)
a=3
b=2
#加法运算
print a+b
#减法运算
print b-a
#乘法运算
print a*b
#除法运算，和java一样取整
print a/b
#模
print a % b
#想获取的小数部分
print b*1.0/a
print float(b)/a
#幂运算
print a**b
#取整
print a//b

# 2: 比较运算符 ==  等于 != 不等于  <> 不等于  > 大于  < 小于   >=  大于等于 <=  小于等于
if a==b:
    print "相等"
else:
    print "不相等"
#########################
if a!=b:
    print "不相等"
else:
    print "相等"
#########################
if a <> b:
    print "不相等"
else:
    print "相等"
#########################
if a > b:
    print "大于"
if b < a:
    print "小于"
#########################大于等于小于等于同理

#  3: 复制运算符 = += -= *= /= %= **= //=

#给a赋值
a = 100
print a

a += b
print a

a -= b
print a

a *= b
print a

a /= b
print a

a **= b
print a

a //= b
print a

a %= b
print a

# 4: 逻辑运算符 and (在Java中使用 && ) or(在Java中使用 || ) not(在ava中 使用 !)

if a == 0 and b == 2:
    print "没毛病"
if a == 190 or b == 2:
    print "没毛病"
if not(a == 1000 and b == 20):
    print "没毛病"

#  5: 成员运算符 in(在的时候返回 true)  not in (不在的时候返回true)

aa=12
bb=13
list1=[12,13,14]
print aa in list1
print bb in list1

print aa not in list1
print bb not in list1

#  在字符串里面查找 ,
message = "我是中国人"
msg1 = "我"
msg2 = "爱"
print msg1 in message
print msg2 in message

# 6: 身份运算符 is  is not

a=20
b=20
print a is b

liming = "李明"
lisi = "李明"
print liming is not lisi

