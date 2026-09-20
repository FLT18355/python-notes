# file_io.py
# 文件读写示例

import json
from pathlib import Path

# 写入文本文件
print("=== 写入文件 ===")
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")

# 读取文本文件
print("=== 读取文件 ===")
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 逐行读取
print("=== 逐行读取 ===")
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"行：{line.strip()}")

# 追加写入
print("=== 追加写入 ===")
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("追加的行\n")

# JSON 读写
print("=== JSON 操作 ===")
data = {
    "name": "张三",
    "age": 25,
    "skills": ["Python", "Java"]
}

# 写入 JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取 JSON
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(f"加载的数据：{loaded}")

# pathlib 方式
print("\n=== pathlib 方式 ===")
path = Path("example.txt")
content = path.read_text(encoding="utf-8")
print(f"pathlib 读取：{content.strip()}")
path.write_text("用 pathlib 写入", encoding="utf-8")
print(f"pathlib 写入后：{path.read_text(encoding='utf-8')}")

# 清理临时文件
Path("example.txt").unlink()
Path("data.json").unlink()
print("\n临时文件已清理")
