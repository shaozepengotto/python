#file = open('文件名.txt', 'r')
#content = file.read()
#print(content)
#file.close()


file = open("ex15_sample.txt")
content = file.read()
prompt = input("看看内容> ")
print(content)
file.close()