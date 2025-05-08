formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "own text here",
    "Maybe a poem",
    "Or a song about fear"
))


# 这个代码的作用是定义一个格式化字符串formatter，然后使用format方法将不同类型的值填充到这个字符串中。最后输出结果。