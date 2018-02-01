#-*-coding:utf-8-*- 
__author__ = 'Aaron2Study'
'''
python 学习
购物小程序练习
包含两级菜单，可以购买多件，
允许多用户登录，能够保存用户账户， 
能够查看购买记录，显示购物车列表
'''

product = [
    ("Electrical equiment", (("TV", 2000), ("Air-con", 2000), ("Washing-mechine", 3000), ("Refrigerator", 1500))),
    ("Clothes",(("UT", 200), ("HM", 150), ("ZARA",300), ("ANTA", 100))),
    ("Phone",(("Iphone", 5000), ("HUAWEI", 3000), ("SAMSUNG", 5000), ("XIAOMI", 2000))),
    ("Car",(("BMW", 500000), ("Audi", 500000), ("Pasate", 200000), ("Tesla", 800000)))
]

shopping_cart = {}

salary = input("input your salary:")
if salary.isdigit():
    salary = int(salary)
    print("Welcome to my shopping mall with salary [%s]".center(50,'-') % salary)
else:
    print("Your input invalid type....")

exit_flag = False
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
            print("Product detail list".center(50,'-'))
            for d_item in enumerate(product[user_class][1]):
                d_index = d_item[0]
                d_name = d_item[1][0]
                d_price = d_item[1][1]
                print("  ", d_index,".", d_name, d_price)
            user_choice = input("Please choose the product that you want to buy[c for check, q for quit]:")
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
                            print("Your balance is not enough [%s] need [%s]" %
                                  (salary, buy_num*user_product_price))
                        else:
                            salary -= user_product_price*buy_num
                            if user_product in shopping_cart.keys():
                                value = shopping_cart.get(user_product);
                                value[1] += buy_num
                            else:
                                value = [user_product_price, buy_num]
                                shopping_cart.setdefault(user_product, value)
                                print("Your have buy [%s] and balance is [%s]" % (user_product, salary))
                else:
                    print("Your input wrong number...")
            else:
                print("Your shopping cart is as below".center(50,'*'))
                print("id   p_name     num    total_price")
                for item in enumerate(shopping_cart):
                    index = item[0]
                    key = item[1]
                    value = shopping_cart[key]
                    count = value[1]
                    p_sum = count*value[0]
                    print(index,'. ',key,"  ",count, "  ", p_sum)
    elif user_class == 'c' or user_class == 'check':
        print("Your shopping cart is as below".center(50, '*'))
        print("id   p_name     num    total_price")
        for item in enumerate(shopping_cart):
            index = item[0]
            key = item[1]
            value = shopping_cart[key]
            count = value[1]
            p_sum = count * value[0]
            print(index, '. ', key, "  ", count, "  ", p_sum)
        print("Your balance is [%s]" % salary)
    elif user_class == 'q' or user_class == "quit":
        print("Your shopping cart is as below".center(50, '*'))
        print("id   p_name     num    total_price")
        for item in enumerate(shopping_cart):
            index = item[0]
            key = item[1]
            value = shopping_cart[key]
            count = value[1]
            p_sum = count * value[0]
            print(index, '. ', key, "  ", count, "  ", p_sum)
        exit_flag = True

