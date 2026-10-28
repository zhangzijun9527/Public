# print('苹果|香蕉|橙子|葡萄')
# name = '张三'
# age = 25
# city = '北京'
# print(name,end='-')
# print(age,end='-')
# print(city,)
# name = '张子俊'
# age = 21
# height = '1.85'
# print(f'===========个人信息==========\n姓名：{name}\n年龄：{age}岁\n身高：{height}米\n============================')
# print('古人云：\"三人行，必有我师焉。\"')
# money = int(input('请输入你的金额：'))
# if money >= 500:
#     money -= 100
#     print(f'恭喜你优惠100元，现在您需要支付{money}元')
# elif 300 <= money <500:
#     money -= 50
#     print(f'恭喜你优惠50元，现在您需要支付{money}元')
# else:
#     print(f'抱歉没有优惠，现在您需要支付{money}元')
# money = 0
# sum = 0
# for i in range(1,8):
#     money = int(input(f'请输入你第{i}天的零花钱：'))
#     sum += money
# print(f'你现在零花钱总共有{sum}元'
# num = 333
# while num <= 666:
#     if num %2 == 0:
#         print(num)
#     num += 1
# sum = 0
# for i in range(1,10):
#     num = 1
#     while num <= i:
#         sum = i * num
#         print(f'{i}x{num}={sum}',end='\t')
#         num += 1
#     print()
# sum = 0
# for i in range(10):
#     for j in range(1,i+1):
#         sum = i * j
#         print(f'{i}x{j}={sum}',end='\t')
#     print()
# for i in range(1,50):
#     if i% 3 == 0 and i% 5 != 0:
#         print(i)
# target_num = 10
# while True:
#     num = int(input('请输入您的数字：'))
#     if num > target_num:
#         print('猜大了')
#     elif num < target_num:
#         print('猜小了')
#     else:
#         print('恭喜你猜对啦！')
#         break

# num = [1,2,3,4,5]
# num[:3] = ['a','b']
# print(num)

# 第二次作业
# money = float(input("请输入商品价格:"))
# if money >= 500:
#     payment = money - 100
# elif 300 <= money <= 500:
#     payment = money - 50
# else:
#     payment = money
# print(f'实付金额：{payment}')

# total_money = 0
# for i in range(1,8):
#     money = float(input(f'请输入星期{i}的零花钱：'))
#     total_money = total_money + money
# print(f'你的总零花钱是：{total_money}')
#
# num = 333
# while num <= 666:
#     if num % 2 == 0:
#         print(num)
#     num += 1
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}x{i}={i*j}',end='\t')
#     print()

# for i in range(1,51):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)
# target_num = 10
# while True:
#     guess_num = int(input('请输入您的数字：'))
#     if guess_num > target_num:
#         print('猜大了')
#     elif guess_num < target_num:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break

# info = "2026-08-30-Thursday"
# year = info[:4]
# print(year)
# month_day = info[5:10]
# print(month_day)
# weekday = info[11:19]
# print(weekday)
# print(info[9::-1])

# user_info = " 张三;17654323|zhangsan@1688.com-北京 "
# print(user_info.strip())
# print(type(11.3))

# money = int(input('请输入商品金额；'))
# if money >= 500:
#     money -= 100
#     print(f'您要支付的金额；{money}')
# elif 300 <= money < 500:
#     money -= 50
#     print(f'您要支付的金额：{money}')
# elif money < 300:
#     print(f'您要支付的金额：{money}')

# money = 0
# sum_money = 0
# for i in range(1,8):
#     money = int(input("请输入你今天的零花钱："))
#     sum_money += money
# print(f'你的零花钱总金额:{sum_money}')

# for i in range(0,10):
#     for j in range(1,i+1):
#         print(f'{j}x{i}={i*j}',end='\t')
#     print()

# for i in range(1,51):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i,end='\t')

# sum = 10
# while 1:
#     num = int(input("请输入你的数字："))
#     if num < sum:
#         print("猜小了")
#     elif num > sum:
#         print("猜大了")
#     elif num == sum:
#         print("猜对了！！！")
#         break

# info ="2026-08-30-Thursday"
# num1 = info[0:4]
# num2 = info[5:7]
# num3 = info[8:10]
# num4 = info[11:19]
# print(f'年份：{num1},月份：{num2},日期：{num3},星期：{num4}')
# print(info[9::-1])

# user_info = '  张三；816378317|zhangsan@168zhangsan,zhangsan'
# new = user_info.strip().replace('；',',').replace('|',',').replace('zhangsan','zhangsan'.upper())
# print(new)

# a = ['cat','dog','bird','fish']
# a.append('rabbit')
# a.append('turtle')
# # a.remove('dog')
# a.pop(1)
# print(a)

# a = [12,34,63,54,75,96,27,18]
# list = []
# for i in a:
#     if i % 3 == 0:
#         list.append(i)
# print(list)
# list = [i for i in a if i % 3 ==0 ]
# print(list)

# scores = [
#     ["张三",85,90,78],
#     ["李四",92,88,95],
#     ["王五",78,85,80],
# ]
# print(f'李四的数学成绩：{scores[1][2]}')
# scores[2][3] = 88
# scores.append(["赵六",85,90,78])
# print(scores)

# scores =  (78,92,85,92,76)
# print(len(scores))
# print(scores.index(92))
# print(scores.count(92))td
# print(100 in scores)
# print(sorted(scores,reverse=True))
#
# res1,res2 = [1,2]
# print(res1,res2)































