#-*-coding:utf-8-*- 
__author__ = 'Aaron2Study'
'''
python 学习
购物小程序练习
包含两级菜单，可以购买多件，
允许多用户登录，能够保存用户账户， 
能够查看购买记录，显示购物车列表
'''

import json
import getpass

product = [
    ("Electrical equiment", (("TV", 2000), ("Air-con", 2000), ("Washing-mechine", 3000), ("Refrigerator", 1500))),
    ("Clothes",(("UT", 200), ("HM", 150), ("ZARA",300), ("ANTA", 100))),
    ("Phone",(("Iphone", 5000), ("HUAWEI", 3000), ("SAMSUNG", 5000), ("XIAOMI", 2000))),
    ("Car",(("BMW", 500000), ("Audi", 500000), ("Pasate", 200000), ("Tesla", 800000)))
]

shopping_cart = {}

con_flag = True

user_dict = {}

def showcart():
    try:
        print("Your shopping cart is as below".center(50, '*'))
        print("id   p_name     num    total_price")
        for item in enumerate(shopping_cart):
            index = item[0]
            key = item[1]
            value = shopping_cart[key]
            count = value[1]
            p_sum = count * value[0]
            print(index, '. ', key, "     ", count, "      ", p_sum)
        print("END".center(50, '*'))
    except ValueError as e:
        print("shopping cart struct has error with %s." % e)

def write(dic):
    try:
        filew = open("user.json", 'w', encoding='utf-8')
        json.dump(dic, filew, ensure_ascii=False)
        filew.close()
    except ValueError as  e:
        print("ValueError:", e)

file = open("user.json", 'r', encoding = 'utf-8')
user_dict = json.load(file)
print(user_dict)

salary = 0
user_name = input("input your name:")
user_passwd = getpass.getpass("input your password:")   #pycharm不能使用这个模块
hasUser = False
# try:
#     for user_key in user_dict:
#         if user_name == user_key:
#             if user_passwd == user_dict[user_key][0]:
#                 salary = user_dict[user_key][1]
#                 hasUser = True
#                 break
# except ValueError as e:
#     print("Your name or pass word is error.")
try:
    if user_name in user_dict.keys():
        if user_passwd == user_dict[user_name][0]:
            salary = user_dict[user_name][1]
            hasUser = True
except ValueError as e:
    print("Your name or pass word is error.")

if not hasUser:
    user_sel = input("Will sign up?yes[y] or no [n]:")
    if user_sel == 'y' or user_sel == 'yes':
        sign_name = input("input your sign up name:")
        sign_passwd = ''
        for i in range(3):
            sign_passwd = getpass.getpass("First input your password:")
            sign_passwd1 = getpass.getpass("Second input your password:")
            if sign_passwd == sign_passwd1:
                break
            else:
                sign_passwd = ''
        for i in range(3):
            salary = input("input your salary:")
            if salary.isdigit():
                salary = int(salary)
                break
            else:
                salary = 0
                print("Your input invalid type....")
        if sign_passwd != '' and salary != 0:
            user_dict.setdefault(sign_name, [sign_passwd, salary])
            write(user_dict)
        else:
            con_flag = False



if con_flag:
    print("Welcome to my shopping mall with salary [%s]".center(50, '-') % salary)
    exit_flag = False
    exit_flag4detl = False
    while not exit_flag:
        print("Product menu list".center(50,'-'))
        for item in enumerate(product):
            index = item[0]
            p_class = item[1][0]
            print(index, p_class)
        user_class = input("Please select product classify[ or c for check q for quit]:")
        if user_class.isdigit():
            user_class = int(user_class)
            if user_class < len(product):
                exit_flag4detl = False
                print("Product detail list".center(50, '-'))
                while not exit_flag4detl:
                    for d_item in enumerate(product[user_class][1]):
                        d_index = d_item[0]
                        d_name = d_item[1][0]
                        d_price = d_item[1][1]
                        print("  ", d_index, ".", d_name, d_price)
                    user_choice = input("Please choose the product that you want to buy[c for check, q for go back]:")
                    if user_choice.isdigit():
                        user_choice = int(user_choice)
                        if user_choice < len(product[user_class][1]):
                            user_product = product[user_class][1][user_choice][0]
                            user_product_price = product[user_class][1][user_choice][1]
                            buy_num = input("How many do you want to buy:")
                            if not buy_num.isdigit():
                                print("Your have input invalid type...")
                            else:
                                buy_num = int(buy_num)
                                if buy_num*user_product_price > salary:
                                    print("Your balance \033[31;1m[%s]\033[0m is not enough need \033[31;1m[%s]\033[0m" %
                                          (salary, buy_num*user_product_price))
                                    exit_flag4detl = True
                                    exit_flag = True
                                else:
                                    salary -= user_product_price*buy_num
                                    if user_product in shopping_cart.keys():
                                        value = shopping_cart.get(user_product)
                                        value[1] += buy_num
                                    else:
                                        value = [user_product_price, buy_num]
                                        shopping_cart.setdefault(user_product, value)
                                        print("Your have buy [%s][%s] and balance is [%s]" % (buy_num, user_product, salary))
                        else:
                            print("Your input wrong number...")
                    elif user_choice == 'c' or user_choice == 'check':
                        showcart()
                        print("Your balance is \033[41;1m[%s]\033[0m" % salary)
                    elif user_choice == 'q' or user_choice == 'quit':
                        print("Go back to upper layer")
                        exit_flag4detl = True
        elif user_class == 'c' or user_class == 'check':
            showcart()
            print("Your balance is \033[41;1m[%s]\033[0m" % salary)
        elif user_class == 'q' or user_class == "quit":
            showcart()
            user_dict[user_name][1] = salary
            write(user_dict)
            print("Exit shopping".center(50, '-'))
            exit_flag = True

