#coding=utf-8

age = 20

#if语句
if age == 20:
    print "这是一个判断语句"

#eles语句
if age > 20:
    print "大于20"
else:
    print "等于20"

#else if语句
if age > 20:
    print "大于20"
elif age == 20:
    print "等于20"
elif age < 20:
    print "小于20"

#while循环语句
cout = 0
while (cout < 5): # 当条件成立的时候执行内部语句
    cout+=1
    print cout

#有 else 的 while
index = 0
while index < 5:
    print "index",index
    index += 1
else:
    print "当前下标是",index

#for循环str字符串
name = "jack"
for index in name:
    print index

#循环列表list
list = ["aaa","bbb","ccc","ddd","eee"]
for index in list:
    print index

for index in range(len(list)):
    print index,list[index]

for index in range(2,len(list)):
    print index,list[index]
else:
    print "输出所有内容"

#  实现冒泡排序
aaa = [1,9,4,7,6,3,2,77]

#  实现冒泡排序 思路是首先两个for循环嵌套
####################################################################################面试题 1#####################################################################################
for index in range(len(aaa)-1):
    for index1 in range(len(aaa)):
        if aaa[index] < aaa[index1]:
            aaa[index],aaa[index1] = aaa[index1],aaa[index]
print aaa

# 找出 100 以内的素数 1 既不是质素 也不是合数 ,,,,素数概念 只能被  1 和 本身整除的数 叫做 素数

susu = []
for index in range(2,100):
    for index1 in range(2,index):
        if index % index1 == 0:
            print "当前的不是素数",index
            # break 跳槽上一层 for循环
            break
    else:
            susu.append(index)
            pass
print susu

# break 跳出当前 for 循环, 直接 for 循环终止执行，continue 结束本次for循环,继续下一次for循环, 同时 continue 后面的代码是不会执行的

for index in  range(0,9):
    if index == 3:
        continue
    print index
#  pass 占位符
for index in  range(0,2):
    pass