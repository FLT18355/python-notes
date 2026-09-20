# loops.py
# 循环示例

# for 循环
print("=== for 循环 ===")
for i in range(5):
    print(f"数字：{i}")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"水果：{fruit}")

# while 循环
print("\n=== while 循环 ===")
count = 0
while count < 3:
    print(f"计数：{count}")
    count += 1

# break 和 continue
print("\n=== break 和 continue ===")
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(f"奇数：{i}")  # 1, 3

# 列表推导式
print("\n=== 列表推导式 ===")
squares = [x ** 2 for x in range(5)]
print(f"平方列表：{squares}")  # [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
print(f"偶数列表：{evens}")  # [0, 2, 4, 6, 8]

# 嵌套循环
print("\n=== 嵌套循环 ===")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
