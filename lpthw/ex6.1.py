types_of_people = 10  # 定义变量types_of_people，值为10
x = f"There are {types_of_people} types of people."  # 格式化字符串，将types_of_people的值插入到字符串中

binary = "binary"  # 定义变量binary，值为"binary"，这个值是一个字符串
do_not = "don't"   # 定义变量do_not，值为"don't"，这个值是一个字符串
y = f"Those who know {binary} and those who {do_not}."  # 格式化字符串，将binary和do_not的值插入到字符串中

print(x)  # 打印变量x的值。最后输出的是变量types_of_people的值插入后的字符串："There are 10 types of people."
print(y)  # 打印变量y的值。最后输出的是变量binary和do_not的值插入后的字符串："Those who know binary and those who don't."

print(f"I said: {x}") # 格式化字符串，将变量x的值插入到字符串中
print(f"I also said: '{y}'")

hilarious = False  # 定义变量hilarious，值为False，这个值是一个布尔值
joke_evaluation = f"Isn't that joke so funny?! {hilarious}"  # 格式化字符串，将变量hilarious的值插入到字符串中

print(joke_evaluation.format(hilarious)) # 打印变量joke_evaluation的值。最后输出的是变量hilarious的值插入后的字符串："Isn't that joke so funny?! False".相当于加长字符串

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)  #字符串拼接

# 加长字符串有三种方式
# 1. 使用加号（+）将两个字符串连接起来
# 2. 使用格式化字符串（f-string）将变量插入到字符串中
# 3. 使用字符串的format()方法将变量插入到字符串中——17行。在字符串后.format()方法，括号内可以传入变量，变量会按照顺序插入到字符串中

# 4.解释一下为什么w和e用+连起来就可以生成一个更长的字符串
# 在Python中，字符串可以通过加号（+）进行拼接，即将两个字符串连接起来生成一个新的字符串。在这个例子中，w和e都是字符串，通过加号（+）将它们连接起来，就可以生成一个更长的字符串。