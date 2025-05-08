def add(a, b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

num1 =  float(input("请输入第一个数字："))   # input()函数返回的是字符串类型。不加float 或 int 返回值是2030（输入 20 30）
num2 =  float(input("请输入第二个数字："))
result = add(num1, num2)
print(f"结果是：{result}")