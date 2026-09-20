# dicts.py
# 字典操作示例

# 创建字典
user = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}
print(f"用户信息：{user}")

# 查询
print(f"姓名：{user['name']}")
print(f"年龄：{user.get('age')}")
print(f"城市：{user.get('city', '未知')}")

# 新增/修改
user["job"] = "工程师"
user["age"] = 26
print(f"更新后：{user}")

# 删除
user.pop("job")
del user["city"]
print(f"删除后：{user}")

# 遍历
print("\n=== 遍历字典 ===")
for key in user:
    print(f"{key}: {user[key]}")

for key, value in user.items():
    print(f"{key} = {value}")

# 字典推导式
squares = {x: x ** 2 for x in range(5)}
print(f"\n平方字典：{squares}")

# 合并字典
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(f"合并后：{d1}")  # {'a': 1, 'b': 3, 'c': 4}
