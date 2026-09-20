# variables.py
# 变量与数据类型示例

# 基本类型
name = "张三"
age = 25
height = 1.75
is_student = True
nothing = None

print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"身高：{height}")
print(f"是否学生：{is_student}")
print(f"空值：{nothing}")

# 类型查看
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student))  # <class 'bool'>
print(type(nothing))   # <class 'NoneType'>

# 类型转换
print(int("123"))     # 123
print(float("3.14"))  # 3.14
print(str(100))       # "100"
print(bool(0))        # False
print(bool(1))        # True
