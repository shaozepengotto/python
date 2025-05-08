from sys import argv   # 

script, filename = argv

txt = open(filename)  # # 打开文件并赋值给变量txt

print(f"Here's your file {filename}:")  # 格式化字符串输出
print(txt.read())   # 读取txt文件内容并打印

print("Type the filename again:")  # 提示用户输入文件名
file_again = input("> ")  # 通过 >提示 接收用户输入的文件名

txt_again = open(file_again)

print(txt_again.read())