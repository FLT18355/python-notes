# pathlib 详解

`pathlib` 是 Python 3.4+ 内置的路径处理库，用面向对象的方式操作文件和目录，比 `os.path` 更简洁直观。

## 一、导入与创建

```python
from pathlib import Path

# 当前目录
p = Path(".")

# 指定路径
p = Path("/home/user/data.txt")

# 多段拼接（推荐）
p = Path("data") / "sub" / "file.txt"

# 从字符串创建
p = Path("data/file.txt")

# 用户主目录
home = Path.home()

# 当前工作目录
cwd = Path.cwd()
```

## 二、路径拼接

用 `/` 运算符拼接，比 `os.path.join()` 更直观：

```python
base = Path("/home/user")
p = base / "docs" / "readme.md"
print(p)  # /home/user/docs/readme.md
```

## 三、常用属性

```python
p = Path("/home/user/data/file.txt")

p.name        # 'file.txt'      文件名
p.stem        # 'file'          不带后缀的文件名
p.suffix      # '.txt'          后缀
p.suffixes    # ['.txt']        所有后缀
p.parent      # /home/user/data 父目录
p.parents     # 所有父目录（可迭代）
p.parts       # ('/', 'home', 'user', 'data', 'file.txt')
p.anchor      # '/'             根部分
```

## 四、判断方法

```python
p = Path("data.txt")

p.exists()       # 是否存在
p.is_file()      # 是否是文件
p.is_dir()       # 是否是目录
p.is_symlink()   # 是否是符号链接
p.is_absolute()  # 是否是绝对路径
```

## 五、读写文件（最常用）

```python
p = Path("data.txt")

# 读取文本
content = p.read_text(encoding="utf-8")

# 写入文本
p.write_text("hello", encoding="utf-8")

# 读取字节
data = p.read_bytes()

# 写入字节
p.write_bytes(b"hello")

# 逐行读取
with p.open("r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())
```

## 六、目录操作

```python
p = Path("new_dir")

# 创建目录
p.mkdir()                    # 创建单级
p.mkdir(parents=True)        # 递归创建
p.mkdir(exist_ok=True)       # 已存在不报错
p.mkdir(parents=True, exist_ok=True)  # 推荐组合

# 删除
p.rmdir()                    # 删除空目录

# 遍历目录
for item in Path(".").iterdir():
    print(item)

# 递归遍历（glob）
for f in Path(".").glob("*.py"):
    print(f)

for f in Path(".").rglob("*.py"):  # 递归
    print(f)
```

## 七、文件操作

```python
p = Path("data.txt")

# 重命名 / 移动
p.rename("new.txt")
p.replace("new.txt")   # 覆盖已存在文件

# 删除文件
p.unlink()

# 创建空文件
p.touch()

# 获取文件大小
p.stat().st_size

# 修改时间
p.stat().st_mtime
```

## 八、路径转换

```python
p = Path("data/file.txt")

str(p)          # 'data/file.txt'  转字符串
p.resolve()     # 绝对路径（解析符号链接）
p.absolute()    # 绝对路径
p.as_posix()    # 转 POSIX 风格字符串
```

## 九、配合 json 读写

```python
import json
from pathlib import Path

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def save_json(data: dict, path: Path) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

config = load_json(Path("config.json"))
save_json(config, Path("config.json"))
```

## 十、跨平台注意

```python
# 不要手写分隔符
p = Path("data\\file.txt")   # 错误：仅 Windows

# 用 / 运算符或 Path 自动处理
p = Path("data") / "file.txt"  # 正确，跨平台

# Windows 路径
Path("C:/Users/user")
Path(r"C:\Users\user")
```

## 十一、Path 与 os.path 对比

| 功能 | os.path | pathlib |
|------|---------|---------|
| 拼接 | `os.path.join("a", "b")` | `Path("a") / "b"` |
| 文件名 | `os.path.basename(p)` | `Path(p).name` |
| 目录名 | `os.path.dirname(p)` | `Path(p).parent` |
| 后缀 | `os.path.splitext(p)[1]` | `Path(p).suffix` |
| 存在判断 | `os.path.exists(p)` | `Path(p).exists()` |
| 读文件 | `open(p).read()` | `Path(p).read_text()` |

## 十二、最佳实践

```python
from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).resolve().parent

# 数据目录
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# 配置文件
CONFIG = BASE_DIR / "config.json"
if CONFIG.exists():
    content = CONFIG.read_text(encoding="utf-8")

# 遍历所有 Python 文件
for py_file in BASE_DIR.rglob("*.py"):
    print(py_file.name)
```

## 十三、要点

1. 路径拼接用 `/`，不要用字符串拼接
2. 读写文本用 `read_text()` / `write_text()`，记得指定 `encoding="utf-8"`
3. 递归创建目录用 `mkdir(parents=True, exist_ok=True)`
4. 递归查找文件用 `rglob()`
5. 获取脚本所在目录用 `Path(__file__).resolve().parent`