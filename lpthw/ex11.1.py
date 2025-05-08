#print("How oldare you?",sep(": "),end= ' ')
#age = input()
#print("How tall are you?",sep(": "),end= ' ')
#height = input()
#print("How much do you weigh?",sep(": "),end= ' ')
#weight = input()

#print(f"So, you're {age} old,{height} tall and {weight} heavy.")

#print()
#sep 参数用于分隔多个输出对象，而你的代码中并没有多个对象需要分隔，因此不需要使用 sep。
#end 参数用于指定输出结束时的字符，这里正确地使用了 end=': ' 来替代默认的换行符。


#改正后应该是：
print("How oldare you?",end= ': ')
age = input()
print("How tall are you?",end= ': ')
height = input()
print("How much do you weigh?",end= ': ')
weight = input()

print(f"So, you're {age} old,{height} tall and {weight} heavy.")