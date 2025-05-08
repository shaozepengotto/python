from sys import argv
script, input_file = argv   # input_file = 'ex20_test.txt'   这里直接指定了文件名，避免了命令行参数的复杂性

def print_all(f):
    print(f.read())    #  print_all函数是一个高阶函数，因为它接受一个函数作为参数。

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())     # readline()方法读取一行，返回值是字符串类型，包含换行符。

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)  #

print("Now let's rewind, kind of like a tape.")  #

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

