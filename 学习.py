# num = 10
# print(num)
#
# result = 10 + 20
# print(result)
#
# # 多个变量同时指向同一个值
# a = b = c = 1
# print(a,b,c)
#
# # 值和变量的数量必须保持一致，否则会报错
# name,age,city = '张子俊',21,'武汉'
# print(name,age,city)
#
# num = 100
# print(num)
# import keyword
# print(keyword.kwlist)
# 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# 我问为什么
# 那女孩 传简讯给我
# 我该相信那女孩爱我
# 把爱都走曲折
# 谁忘了
# 可是为什么
# 自尊常常将人拖着
# num = 100000000000000000000000000000000000000000000000000000000000000000000000000
# print(num,type(num))
# print(0b1010)
# print(0o12)
# print(0xa,type(0xa))
# num = 15730.23453746457654675
# print(num,type(num))
# print(round(0.1+0.2,1))
# a = 5
# if a > 2:
#     a = a - 1
# print(a)
# """print('她说：\'python很有趣\’')
# haskjdhfbg
# asjygedfi9y"""
#
# year = 2026
# month = 6
# day = 6
# print('今年是',year,'年',month,'月',day,'日')
# print('今年是 %s 年 %s 月 %s 日'%(year,month,day))
# height = 1.85
# print('身高  %.2f米'%(height))
# print(f'今年是{year:6}年{month:3}月{day:3}日')
# pi = 3.141592653589793
# print(f'圆周率:{pi:.5f}')
# print(f'圆周率:{pi:010.2f}')
# print(f'圆周率:{123456789:,}')
# print(f'圆周率:{pi:%2}')

# name = input(('请输入你的名字：'))
# age = input('请输入你的年龄：')
# print(type(name),type(age))

# 精度等级:布尔型<整型<浮点型<复数型
# python会自动把低精度类型转换高精度
# 开发者主动调用内置函数完成转型：int(),float(),bool(),str()等
# 浮点数转换为整数，小数部位被截断
# age = int(input('请输入你的年龄:'))
# print(type(age))
# print(f"一年后，你的年纪是{age+1}岁")
# 非数字字符串转换会报错
# num = float(10)
# print(num,type(num))
# bool():将数据转换为本人下，任意数据都可以转换为布尔型，转换规则为：零/空为假，其余为真。
# 转换为False情况：
#               数值零：整数0，浮点0.0，复数0j
#               空对象：空字符串“”，列表[],元组（），字典{}，集合set(),特色值None
# 其余所有情况转换为布尔型都是为Ture

# str（）：将数据转为字符串型，所有数据都可以转换为字符串
# print(str(10),type(str(10)))
# print(str(9+10j),type(str(9+10j)))
# name = int(input("你的年龄："))
# print(f'我比你大5岁，所以我今年{name+5}岁')
# 运算符
# 一、算术运算符
# 算术运算符和数值一起来执行
# +，-，*，/:加减乘除     两个数相除，结果为浮点数
# //：整除     print(5//2)----2,向下取整
#  %：取模     print(10%4)----2,取余数
# **：幂       print(2**3)----8,底数在前，指数在后
# print(4**0.5)  开方    print（8**（1/3））  开立方
# 优先级 ： () > ** > * / % > + -
# result = (8 + 2 ** 3) * 3 - 15 // 4 % 2 + 6 / 2
# print(result)------------50.0
# 二、赋值运算符
#  = ；赋值运算符
#  ==：等于运算符，比较是否相等
#  +=：加法赋值运算符，先相加，再将计算结果重新赋给变量
# num = 100
# print(num)------100
# num += 100
# print(num)------200
#  -=: 减法赋值运算符
#  *=：乘法赋值运算符
#  /=，//=，%=,**=
# count = 10
# count -= 2 * 3
# count += 15 // 4
# count *= 4 ** (1 / 2)
# print(count)-------14.0
# 赋值运算符无优先级，均同级
# 注意：赋值运算符只针对已存在的变量，因为变量也需要参与计算，若变量未定义会报错
# 复合赋值运算符左侧必须是变量,不能是数字,否则会报错
# 三、转义字符
# \':表示一个普通单引号
# \\:表示一个普通的双引号
# print('she say:\"I\'m fine\"')
# #  /:斜杠   \:反斜杠
# # \\:表示一个反斜杠本身
# print('反斜杠\\')
# \n:换行符,将光标移至下一行
# print('第一行\n第二行\n第三行')
# \t:制表符,用于对齐文本
# 规则:4个英文字符相当于一个单元格
# print('\t*')
# print('1\t*')
# print('12\t*')
# print('123\t*')
# print('1234\t*')
# print('12345\t*')
# print('123456\t*')
# print('1234567\t*')
# \r:回车键,(覆盖前面的内容)
# 原始字符串    字符串前面加r    不会被转义
#
#  比较运算符，返回Ture表示真，False表示假
# print(1 == 2),print(1 == 1)
# 字母比较ASCII码值，多个字母比较，单个字母依次比较
# print('a' > 'b')-----false
#      97    98
# print('ab' > 'ac')-----false
# >=:大于或等于
# <=:小于或等于
# 比较大小必须是同类之间比较，否则会报错

# 逻辑运算符
# 根据布尔值判断真假，但是结果不一定是布尔值
# and :逻辑与，左右两笔是否都为真，真返回最后一个真
# or ：逻辑或，一个为真就是真，假，返回最后一个假
# print(2 - 2 or "3")------3
# print((0 or '' and 5) or 'test' and 0 or (10-7) > 2 and "end")-----end
# if分支结构
# 语法：
# '''
# if 条件表达式
#     条件为真时执行的代码块
# '''
# 条件表达式：最终需返回Ture或False，Ture执行， False直接跳过
# 缩进是语法要求：建议通过回车建自动生成缩进
# if 2 > 1:
#     print('666')
#     if 2 == 2:
#         print('222')
# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print('恭喜你，已经成年了')
# if age < 18:
#     print('抱歉，你没有成年')
# name = input("请输入你的用户名：")
# pwd = (input('请输入你的密码：'))
# if name == "zhangzijun" and pwd == "123456":
#     print('登陆成功')
# else:
#     print("登录失败")
#
#    else:条件为假运算
# # 三元表达式（三目运算符）    注意：三元表达式仅用于二选一场景
# age = int(input("请输入你的年龄："))
# print('成年' if age >= 18 else'未成年')
# name = input("请输入你的用户名：")
# pwd = (input('请输入你的密码：'))
# print('登陆成功' if name == "zhangzijun" and pwd == "123456" else '登陆失败')
# 根据年龄划分阶段，儿童0-12，青少年13-30，中年人31-60，老年人60以上
# age = int(input('请输入您的年龄：'))
# if 0 < age <= 12:
#     print('儿童')
# elif 12 < age <= 30:
#     print('青少年')
# elif 30 < age <= 60:
#     print('中年人')
# elif 60 < age <= 120:
#     print('老年人')
# else:
#     print('请输入正确年龄！')

# Debug调试
# 精准找到bug

# while 循环
# 语法：
# while 循环条件：
#       循环体代码块
#      (循环变量更新语句)   #避免导致死循环
# count = 0
# while count < 5:
#     print("hello world")
#     count += 1
# print('循环结束')
# num = 0
# while num < 101:
#     print(f'{num}%')
#     num += 1
#
# num = 1
# sum = 0
# while num <= 100:
#     sum += num
#     num += 1
# print(sum)---------1~100的和---5050
# 无限循环慎用，容易死机！！！

# for 循环
# 语法：
# for 临时变量 in可迭代变量：
#     循环体代码块
# 遍历字符串
# for i in ' 123456789':
#     print(i)
# for i in range(1,10):
#     print(i)
# for i in range(1,11):
#     print('hello world')
# for 循环的次数取决于可迭代变量
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)
# for i in range(1,10,2):
#     print(i)

# 循环嵌套
# # while循环嵌套
# row = 1
# while row <= 3:
#     col = 1
#     while col <= 4:--------------外循环一次，内循环完全执行完
#         print('*',end=' ')
#         col += 1
#     print()
#     row += 1

# row = 1
# while row <=9:
#     col = 1
#     while col <= row:------------------九九乘法表
#         sum = col * row
#         print(f'{row}x{col}={sum}', end='\t')
#         col += 1
#     print()
#     row += 1

# break和continue语句
# break，立即退出当前循环
# continue，跳过当前循环的剩余部分
# 通常与if搭配使用，满足特定条件退出整个循环（break）/退出当前循环（continue）
# for i in range (1,11):
#     if i == 5:
#         break
# #     print(i)
# for i in (1,2,3,4,5,6,7,9,10,11,12,13,14,15):
#     if i == 8:
#         print('找到了8')
#         break
# else:
#     print('没有找到8')

# 字符串编码
# 字符串(str):文本数据类型
# 字节串（bytes）：二进制数据
# 编码：ste.encode(encoding='UTF-8',),把字符串转为字节串
# name = '张子俊'
# byte_name = name.encode('utf-8')
# print(byte_name)     #     字节串展示采用十六进制（二进制太长），ASCII编码32~126为可打印字符，python打印字符串时显示该范围内字符串本身
# 实际开发中，必须保证编码和解码使用同一个编码格式，默认编码格式-------utf-8
# print(str.encode(name))
# 字符串基本操作
# 拼接与重复
#    字符串拼接必须和字符串   使用  +
#    字符串重复使用   *
# print('hello' + ' world')
# print('age' + str(18))
# print('python' * 10)
# print('hello' + '!' * 3)    先重复再拼接
# 字符串的成员运算： in /  not in
# in ： 判断“子串”是否包含在“目标字符串”中，若不存在则返回True，存在则返回False
# name = 'zhangzijun'
# print('zhang' in name)     True
# print('zj' in name)        False     整体判断

# 牵引和切片
# 索引(获取单个字符)
# 正向索引:从字符串左侧开始,第一个为0
# 负向索引:从字符串右侧开始,第一个为-1
# 语法:字符串[索引值]
# text = 'python'
# print(text[3])------h
# print(text[-4])-----t

# 切片(获取连续个字符)
# 语法:字符串[star:end:step]
# start: 切片开始
# end: 切片结束,包前不包后
# step: 步长,默认为 1
# text = 'python'
# # print(text[:5])-------pyhto
# # print(text[1:3])----yt
# print(text[::-2])-----nhy     步长为正,从左到右,步长为负,从右到左

# 字符串常见的内置函数    字符串 + . + 函数
# # 查找字符
# find('子串',[开始索引:结束索引)    寻找子串位置,返回首个牵引,找不到返回  -1
# index()                         找不到报错
# count()    子串出现次数

# # 修改字符
#   replace(旧子串,新子串,最大替换次数),返回替换后新字符串
#   split():按指定分隔符拆分字符串,返回列表,默认空白字符分割
#   strip 清除
#   lower   大转小
#   upper   小转大

# # 检查字符
# startswith:检查字符串是否以指定的前缀开头
# endswith:                    后缀
# islower:   是否全部小写
# isupper:   是否全部大写

# #  列表
# 语法：变量名 = [元素1，元素2，元素3，....]
# 内置函数list() 可以将其他可迭代对象转为列表
# 列表推导式是一种简洁的快速创建列表的方法
# 列表名 = [表达式 for 变量 in 可迭代对象]
# lst1 = []
# for i in range(1,6):
#     lst1.append(i)
# print(lst1)
#
# lst2 = [i for i in range(1,6)]
# print(lst2)
# 牵引和切片

# 字典
# 语法：变量名 = {键1：值1，键2：值2，----}
# 键具有唯一性，键重复时后面的值会覆盖前面的值
# 不可变性
# 键必须可哈希（不可变类型数据）键必须是不可变类型（字符串，数值，元组)
# hash（数据）：检验数据是否可哈希，可哈希会有值，不可哈希会报错
# 多样性

# 字典的常见操作
# 访问字典中的元素
# 使用in和not in 关键字检查字典中是否包含某个键，仅检查键
# 访问字典的值
# 方式一：字典[键名]，通过键获取字典中对应的值，键不存在时报错
# 方式二：get（键名，[默认值=None]）方法   更安全的访问方式，可设置默认值
# len（）：获取字典元素（键值对）的个数

# 添加和修改字典元素
# 有则修改，无则添加
# 字典[键] = 值

# 删除字典元素
# 1、pop（键，[默认值]）方法是删除指定的键值对，并返回默认值  默认值不指定会报错
# 2、clear()方法是删除字典中所有键值对，使字典变成空字典
# 3、del语句
# 使用del永远删除字典中的指定的键值对
# del 字典【键】 删除该字典对应的键值对
# 得了 字典      删除整个字典
# info = {'name':'zzj','age':20,'height':100,'weight':1000}
# print(info.pop('city',''))

# 遍历字典
# 使用for循环直接遍历字典时默认遍历字典中的键
# 1、字典.keys（）：逐个获取字典中的所有键
# 2、字典.values()：逐个获取字典中十一点值
# 3、字典.items（）：同时获取每一个键值对的键和值。返回的是（key，values）形式的元组

# 集合
# a = {}  空字典
# set（）  空集合
# set（可迭代对象）：把可迭代对象转换为集合，且会自动去重
# 可哈希性，无序性，不可修改

# 集合常见操作
# for遍历
# in 和 not in 判断是否在集合中
# add（）：向集合添加单个元素，若元素已经存在则不执行任何操作
# update（）：添加一个或多个元素

# 删除集合元素
# 1、remove（）：删除集合中指定元素，不存在报错
# 2、discard（）：元素不存在不报错，静默处理
#

# 集合的数值操作
# 交集   &   intersection
# # 并集   |   union
# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# set2 = {7, 8, 9, 10, 11, 12, 13}
# print(set1 & set2)
# print(set1 | set2)

# 深浅拷贝
# 可变类型与不可变类型
# 1、可变类型：   list,dict,set
# 2、不可变类型：  int,float,str,bool,tuple
# lst = [1, 2, 3, 4]
# print(f'列表：{lst},地址：{id(lst)}')
# lst[2] = 100
# print(f'列表：{lst},地址：{id(lst)}')
# s = {1,2,3,4,5,6,7,8,9}
# s.remove(5)
# print(s)
# year = 2026
# month = 10
# day = 8
# print('今年是%s年，%s月，%s日'%(year,month,day))
# money = int(input('输入你的金额：'))
# money = money + 10
# print(f'你的金额是：{money}')


# name = input("请输入你的姓名：")
# age = input("请输入你的年龄：")
# print(f"你的姓名是{name},年龄是{age}岁")
# print(type(age))















