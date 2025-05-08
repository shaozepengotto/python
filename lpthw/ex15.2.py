from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

txt.close()   # 关闭文件。缺少这行运行不了