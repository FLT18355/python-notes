# csv — CSV 文件处理

`csv` 模块用于读写 CSV（逗号分隔值）文件。

## 读取 CSV

```python
import csv

# 基本读取
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### 读取为字典

```python
import csv

with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["姓名"], row["分数"])
```

## 写入 CSV

```python
import csv

# 写入列表
with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "年龄", "城市"])
    writer.writerow(["张三", 25, "北京"])
    writer.writerow(["李四", 30, "上海"])

# 写入字典
with open("output.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = ["姓名", "年龄", "城市"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"姓名": "张三", "年龄": 25, "城市": "北京"})
```

## 自定义分隔符

```python
import csv

# TSV（制表符分隔）
with open("data.tsv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)

# 自定义分隔符
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        print(row)
```

## 处理中文和编码

```python
import csv

# 写入时指定编码
with open("data.csv", "w", encoding="utf-8-sig", newline="") as f:
    # utf-8-sig 添加 BOM，Excel 可正确识别中文
    writer = csv.writer(f)
    writer.writerow(["姓名", "城市"])
    writer.writerow(["张三", "北京"])
```

## 实战示例

```python
import csv
from pathlib import Path


def read_csv(path):
    """读取 CSV 文件，返回字典列表"""
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, data, fieldnames):
    """写入 CSV 文件"""
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# 读取
users = read_csv("users.csv")
print(f"共 {len(users)} 条记录")

# 过滤
active_users = [u for u in users if u["status"] == "active"]

# 写入
write_csv("active_users.csv", active_users, users[0].keys())
```

## 注意事项

1. 写入时使用 `newline=""` 避免空行
2. Excel 打开乱码时用 `utf-8-sig`
3. 字段包含逗号时自动加引号
4. 大数据用迭代器逐行读取，不要一次性加载
