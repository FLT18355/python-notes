# operators.py
# 运算符示例

a = 10
b = 3

# 算术运算符
print("=== 算术运算符 ===")
print(f"a + b = {a + b}")    # 13
print(f"a - b = {a - b}")    # 7
print(f"a * b = {a * b}")    # 30
print(f"a / b = {a / b}")    # 3.333...
print(f"a // b = {a // b}")  # 3（整除）
print(f"a % b = {a % b}")    # 1（取余）
print(f"a ** b = {a ** b}")  # 1000（幂运算）

# 比较运算符
print("\n=== 比较运算符 ===")
print(f"a == b: {a == b}")  # False
print(f"a != b: {a != b}")  # True
print(f"a > b: {a > b}")    # True
print(f"a < b: {a < b}")    # False

# 逻辑运算符
print("\n=== 逻辑运算符 ===")
x = True
y = False
print(f"x and y: {x and y}")  # False
print(f"x or y: {x or y}")    # True
print(f"not x: {not x}")      # False

# 成员运算符
print("\n=== 成员运算符 ===")
s = "python"
print(f"'py' in s: {'py' in s}")        # True
print(f"'xyz' not in s: {'xyz' not in s}")  # True
