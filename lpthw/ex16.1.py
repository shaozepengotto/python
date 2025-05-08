# 我想在某个过文件中写几句话
from sys import argv

script, filename = argv
print(f"now I'm going to write to {filename}")
target = open(filename,'w')

line1 = input("line 1>")
line2 = input("line 2>")
line3 = input("line 3>")

target.write(line1)

target.write(line2)
target.write(line3)

target.close()
