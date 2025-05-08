def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {box_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("Or, we can use variables from our script:")
amount_of_cheese = 10     # 定义变量，再给16行调用
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


#函数的调用方式有三种：
#  直接传递数字参数。 第9行
#  使用变量作为参数。 第13、14行再给16行调用
#  在参数中使用数学运算。  第20行