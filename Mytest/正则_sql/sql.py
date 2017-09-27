# -*- coding:utf-8 -*-

# 安装mysqldb
import MySQLdb


# 连接数据库
db = MySQLdb.Connect(host="localhost",db="test",port=3306,charset="utf8",user="root",passwd="123456")

# 使用cursor获取游标
cursor = db.cursor()

# 查询login数据库
sql = "select * from login"

# 执行查询语句
cursor.execute(sql)

# #获取一条数据
# result = cursor.fetchone()
# print result

# # for循环打印数据
# for index in result:
#     print index

# #获取指定的数据条数
# result = cursor.fetchmany(5)
# for index in result:
#     print index

# #获取所有的数据
# result = cursor.fetchall()
# for index in result:
#     print index


#元素与列表是一个概念.元祖与列表的不同在于列表的数据介意修改,而元素的数据不可以修改
#json 有两部分组成 最外边list,里面object,.其实就是字典

#声明list
p_list = []

# result = cursor.fetchall()
# for index in result:
#
#     #人的字典，实例化一个对象
#     person = {}
#
#     id = index[0]
#     name = index[1]
#     password = index[2]
#     #加入到字典里面
#     person["id"] = id
#     person["name"] = name
#     person["password"] = password
#     #将字典装入list里面
#     p_list.append(person)
# print p_list

#获取指定的条数

# #重置游标到第一条后面
# cursor.scroll(1,mode='absolute')
# result = cursor.fetchall()
# for index in result:
#     print index


# 数据库 增 insert  删 delete  改 update  查 select

# 向数据库里面添加一条数据
# 插入数据有两种方式 1: 模糊插入 2: 指定插入
# 使用模糊插入向数据库里面插入一条数据
# 注意如果id 自增插入的时候写 0

# #增
# insert = "insert into login values(10,'jjj',1010)"
# #执行插入语句
#
# try:
#     cursor.execute(insert)
#     db.commit()
# except:
#     db.rollback()
#     db.close()

# #删
# delete = "delete from login where id = 10"
# #执行删除语句
# try:
#     cursor.execute(delete)
#     db.commit()
# except:
#     db.rollback()
#     db.close()

# #改
# update = "update login set name = 'aaaaaaaa' where id = 1"
#
# #执行修改语句
# try:
#     cursor.execute(update)
#     db.commit()
# except:
#     db.rollback()
#     db.close()


#  多表关联 子查询
#  关联 : 内关联 左关联 右关联

# 内连接 inner join  等值连接 一把情况下与 ON 配合使用
# 左连接 left join 一把情况下与 ON 配合使用
# 右连接 right join 一把情况下与 ON 配合使用

# #两表关联，内链接
# inner = "select l.name,l.password,z.sex,z.YorN from login l inner join ziliao z ON l.id = z.id"
# #执行查询语句
# try:
#     cursor.execute(inner)
#     result = cursor.fetchall()
#     for index in result:
#         print index
#         pass
# except Exception:
#     db.rollback()
#     db.close()