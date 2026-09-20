# functions.py
# 函数示例

# 基本函数
def welcome():
    print("Hello, World!")

welcome()

# 带参数的函数
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}！")

greet("张三")
greet("李四", "早上好")

# 返回值
def add(a, b):
    return a + b

result = add(10, 20)
print(f"10 + 20 = {result}")

# 可变参数
def sum_all(*args):
    return sum(args)

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")

# 关键字参数
def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info(name="蓝汐", age=18, city="月光湖")

# 文档字符串
def multiply(a, b):
    """
    计算两个数的乘积
    :param a: 第一个数
    :param b: 第二个数
    :return: 乘积
    """
    return a * b

print(multiply(3, 4))  # 12
print(multiply.__doc__)  # 打印文档字符串
