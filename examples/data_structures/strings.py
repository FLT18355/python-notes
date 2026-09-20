# strings.py
# 字符串操作示例

s = "  Hello, Python!  "

# 基本操作
print(f"原字符串：'{s}'")
print(f"去除空白：'{s.strip()}'")
print(f"大写：'{s.strip().upper()}'")
print(f"小写：'{s.strip().lower()}'")
print(f"标题：'{s.strip().title()}'")

# 查找与替换
print(f"查找 'Python'：{s.find('Python')}")  # 8
print(f"替换：'{s.strip().replace('Python', 'World')}'")

# 分割与连接
parts = "a,b,c".split(",")
print(f"分割：{parts}")
print(f"连接：{'-'.join(parts)}")

# 格式化
name = "蓝汐"
age = 18
print(f"f-string：{name} 今年 {age} 岁")
print("format：{} 今年 {} 岁".format(name, age))
print("% 格式化：%s 今年 %d 岁" % (name, age))

# 判断
print(f"以 H 开头：{s.strip().startswith('H')}")
print(f"以 ! 结尾：{s.strip().endswith('!')}")

# 统计
text = "hello world"
print(f"长度：{len(text)}")
print(f"l 出现次数：{text.count('l')}")

# 切片
print(f"前5个：{text[:5]}")
print(f"反转：{text[::-1]}")
