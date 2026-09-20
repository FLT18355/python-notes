# pathlib — 路径处理

> 详细内容见 `stdlib/json/_pathlib_.md`，这里是补充与实战示例。

## 快速参考

```python
from pathlib import Path

p = Path(".")                          # 当前目录
p = Path("/home/user/data.txt")        # 绝对路径
p = Path("data") / "users" / "a.json"  # 路径拼接

# 判断
p.exists()      # 是否存在
p.is_file()     # 是否是文件
p.is_dir()      # 是否是目录

# 读写
content = p.read_text(encoding="utf-8")
p.write_text("hello", encoding="utf-8")

# 遍历
for f in Path(".").rglob("*.py"):  # 递归查找所有 .py 文件
    print(f.name)
```

## 实战示例

### 批量重命名

```python
from pathlib import Path

path = Path("photos")
for i, f in enumerate(sorted(path.glob("*.jpg")), 1):
    new_name = f"photo_{i:03d}.jpg"
    f.rename(path / new_name)
```

### 统计代码行数

```python
from pathlib import Path

total = 0
for f in Path(".").rglob("*.py"):
    total += len(f.read_text(encoding="utf-8").splitlines())
print(f"总行数：{total}")
```

### 查找大文件

```python
for f in Path(".").rglob("*"):
    if f.is_file() and f.stat().st_size > 100 * 1024 * 1024:  # 100MB
        print(f"{f}: {f.stat().st_size // 1024 // 1024} MB")
```
