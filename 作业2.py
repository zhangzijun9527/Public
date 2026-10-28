# scores = {
#     '姓名':'zhangsan',
#     '年龄':'18',
#     '成绩':{'语文':'99','数学':'98','英语':'97'}
# }
# print(scores)
# scores['性别'] = '男'
# print(scores)
# scores['成绩']['数学'] = '95'
# print(scores)
# scores.pop('年龄')
# print(scores)
#
# class1 = {"class_name":"一班","interests":{'篮球','绘画','编程','围棋'}}
# class2 = {"class_name":"二班","interests":{'编程','围棋','羽毛球','音乐'}}
# a = class1["interests"]
# b = class2["interests"]
# print(a)
# print(b)
# c = (a | b)
# print(c)
# all = class1["interests"] | class2["interests"]
# print(all)
#
# def calculate(a,b):
#     return a*b
# while True:
#     try:
#         a = int(input("请输入长："))
#         b = int(input("请输入宽："))
#     except ValueError:
#         print("请输入有效数字")
#     else:
#         if a > 0 and b > 0:
#             print(f'面积：{calculate(a,b)}')
#             break
#         else:
#             print("请输入正数")
#
# import random
# def cai():
#     num = random.randint(1,100)
#     list = []
#     for i in range(10):
#         try:
#             num2 = int(input('请输入你的数字：'))
#             if num2 < num:
#                 list.append(num2)
#                 print(f'猜小了，你已经猜过{list}')
#             elif num2 > num:
#                 list.append(num2)
#                 print(f'猜大了,你已经踩过{list}')
#             elif num2 == num:
#                 print(f'猜对了')
#                 break
#             elif 0 <= num2 >= 100:
#                 print('请输入0-100nei')
#         except ValueError:
#             print('请输入有效数字')
# cai()
#
# while True:
#     try:
#         a = int(input('请输入0-100内的数字:'))
#     except ValueError:
#         print('请输入有效数字')
#     else:
#         if a < cai():
#             print('猜小了')
#         elif a > cai():
#             print('猜大了')
#         elif a == cai():
#             print('猜对了')
#             break

# menu = {}
# def add_menu():
#     add_menu = input('请输入菜品名称：')
#     if add_menu in menu:
#         print('该菜品已经添加')
#     else:
#         try:
#             add_money = float(input('请输入菜品价格：'))
#             if add_money < 0:
#                 print('价格不能太低了哦！')
#                 return
#             menu[add_menu] = add_money
#             print('添加成功')
#         except ValueError:
#             print('请输入正确价格')
#
# def search_menu():
#     search_menu = input('请输入你想搜索的菜品：')
#     if search_menu in menu:
#         print(f'菜名：{search_menu}价格：{menu[search_menu]}元')
#     elif search_menu  not in menu:
#         print('没有该菜品哦！')
#
# def show_menu():
#     if menu:
#         for name,price in menu.items():
#             print(f'菜品：{name}，价格{price}元')
#     else:
#         print('该菜品没添加')
#
# while True:
#     try:
#         print('''
#             1.添加菜品
#             2.搜索菜品
#             3.展示菜品
#             4.退出系统
#             ''')
#         a = int(input('请输入你选择的功能：'))
#
#         if a == 1:
#             add_menu()
#         elif a == 2:
#             search_menu()
#         elif a == 3:
#             show_menu()
#         elif a == 4:
#             print('欢迎下次光临!')
#             break
#         else:
#             print('请输入有效选项')
#     except ValueError:
#         print('请输入有效数字')

# class Book:
#     def __init__(self, title,author,price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def show_book(self):
#         return print(f'书名：{self.title}\t作者：{self.author}\t价格：{self.price}')
#
# p1 = Book('三体',"刘慈欣",30)
# p1.show_book()

# class Device:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def show_info(self):
#         print(f'设备：{self.name},价格：{self.price}')
#
# class Phone(Device):
#     def __init__(self,name,price,camera_pixels,battery_capacity):
#         super().__init__(name,price)
#         self.camera_pixels = camera_pixels
#         self.battery_capacity = battery_capacity
#     def show_info(self):
#         print(f'设备：{self.name}\t价格:{self.price}\t像素{self.camera_pixels}\t电池容量：{self.battery_capacity}')
#     def call(self):
#         print('可以打电话')
# p1 = Phone('苹果',999,1000000,6000)
# p1.show_info()
# p1.call()











