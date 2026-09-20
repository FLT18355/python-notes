# stdlib_examples.py
# 标准库常用示例

import os
import sys
import json
import random
import datetime
import re
from pathlib import Path

print("=== os 模块 ===")
print(f"当前目录：{os.getcwd()}")
print(f"环境变量 HOME：{os.environ.get('HOME', '未知')}")

print("\n=== sys 模块 ===")
print(f"Python 版本：{sys.version}")
print(f"平台：{sys.platform}")
print(f"命令行参数：{sys.argv}")

print("\n=== json 模块 ===")
data = {"name": "张三", "age": 25, "city": "北京"}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(f"JSON 字符串：\n{json_str}")
loaded = json.loads(json_str)
print(f"加载后：{loaded['name']}")

print("\n=== datetime 模块 ===")
now = datetime.datetime.now()
print(f"当前时间：{now.strftime('%Y-%m-%d %H:%M:%S')}")
tomorrow = now + datetime.timedelta(days=1)
print(f"明天：{tomorrow.strftime('%Y-%m-%d')}")

print("\n=== random 模块 ===")
print(f"随机数：{random.randint(1, 100)}")
print(f"随机选择：{random.choice(['苹果', '香蕉', '橙子'])}")
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(f"打乱后：{items}")

print("\n=== re 模块 ===")
text = "邮箱：user@example.com，电话：138-1234-5678"
emails = re.findall(r"\w+@\w+\.\w+", text)
print(f"邮箱：{emails}")
phones = re.findall(r"\d{3}-\d{4}-\d{4}", text)
print(f"电话：{phones}")

print("\n=== pathlib 模块 ===")
p = Path(".") / "examples"
print(f"路径：{p}")
print(f"是否存在：{p.exists()}")
print(f"当前目录文件：")
for f in Path(".").iterdir():
    if f.is_file():
        print(f"  {f.name}")
