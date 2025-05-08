#巩固练习：将 input和 argv一起使用，让脚本从用户那里得到更多的输入。不要想多了，只是
#用 argv得到一些东西，用 input从用户那里得到另外一些东西。
from sys import argv

# 从命令行获取参数
script, first_arg = argv

# 从用户输入获取其他信息
second_input = input("Please enter the second input: ")
third_input = input("Please enter the third input: ")

# 打印所有获取的信息
print(f"Script name: {script}")
print(f"First argument from argv: {first_arg}")
print(f"Second input from user: {second_input}")
print(f"Third input from user: {third_input}")
