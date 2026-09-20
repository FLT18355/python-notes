# error_handling.py
# 异常处理示例

# 基本 try-except
print("=== 基本异常处理 ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("错误：除数不能为零")

# 捕获多种异常
print("\n=== 多种异常 ===")
try:
    num = int("abc")
    result = 10 / num
except ValueError:
    print("错误：无法转换为整数")
except ZeroDivisionError:
    print("错误：除数不能为零")

# 获取异常信息
print("\n=== 异常信息 ===")
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"文件未找到：{e}")

# try-except-else-finally
print("\n=== finally ===")
try:
    f = open("temp.txt", "w")
    f.write("test")
except IOError:
    print("写入失败")
finally:
    f.close()
    print("文件已关闭")

# 自定义异常
print("\n=== 自定义异常 ===")
class AgeError(Exception):
    pass

def set_age(age):
    if age < 0 or age > 150:
        raise AgeError(f"年龄不合法：{age}")
    return age

try:
    set_age(200)
except AgeError as e:
    print(f"捕获异常：{e}")

# 断言
print("\n=== 断言 ===")
def divide(a, b):
    assert b != 0, "除数不能为零"
    return a / b

print(divide(10, 2))

# with 语句（上下文管理器）
print("\n=== 上下文管理器 ===")
with open("temp.txt", "w") as f:
    f.write("自动关闭")
print("文件已自动关闭")
