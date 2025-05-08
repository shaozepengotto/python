# 定义变量
name = "Alice"
age = 30
hobby = "编程"
quote = "坚持就是胜利"

# 使用多种转义字符和格式化字符串
message = (
    f"姓名：\t{name}\n"
    f"年龄：\t{age}\n"
    f"爱好：\t{hobby}\n"
    f"她说：\t\"{quote}\"\n"
    f"详细信息：\n"
    f"\t- 名字长度：{len(name)}个字符\n"
    f"\t- 年龄加倍：{age * 2}\n"
    f"\t- 爱好首字母：{hobby[0]}\n"
    f"路径示例：C:\\Users\\Alice\\Documents\\\n"
    f"换行符示例：第一行\n第二行\n第三行\n"
    f"制表符示例：\t项目1\t项目2\t项目3\n"
    f"反斜杠示例：\\这是一个反斜杠\n"
)

print(message)


# 巩固练习3
#定义变量