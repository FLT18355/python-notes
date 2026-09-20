# 文件与 I/O

## 打开文件

```python
f = open("file.txt", "r", encoding="utf-8")
content = f.read()
f.close()
```

推荐使用 `with` 语句，自动关闭文件：

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
# 离开 with 块后文件自动关闭
```

## 文件模式

| 模式 | 说明 |
|------|------|
| r | 只读（默认） |
| w | 只写，清空原内容 |
| a | 追加 |
| x | 独占创建，文件已存在则报错 |
| b | 二进制模式 |
| + | 读写模式 |

组合示例：
- `rb`：二进制读取
- `wb`：二进制写入
- `r+`：读写（不截断）
- `w+`：读写（截断）
- `a+`：追加读写

## 读取方式

```python
with open("file.txt", "r", encoding="utf-8") as f:
    # 读取全部
    content = f.read()

    # 读取一行
    line = f.readline()

    # 读取所有行（返回列表）
    lines = f.readlines()

    # 逐行遍历（推荐，内存友好）
    for line in f:
        print(line.rstrip())
```

## 写入方式

```python
# 写入字符串
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.writelines(["第二行\n", "第三行\n"])

# 追加
with open("out.txt", "a", encoding="utf-8") as f:
    f.write("追加的行\n")
```

## 二进制文件

```python
# 读取图片
with open("photo.jpg", "rb") as f:
    data = f.read()

# 写入图片
with open("copy.jpg", "wb") as f:
    f.write(data)
```

## 文件指针

```python
with open("file.txt", "r") as f:
    print(f.read(5))   # 读取5个字符
    print(f.tell())    # 当前指针位置 → 5
    f.seek(0)          # 回到文件开头
    print(f.read())    # 读取全部
```

## 编码

```python
# UTF-8（推荐）
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# GBK（Windows 中文环境常见）
with open("file.txt", "r", encoding="gbk") as f:
    content = f.read()
```

## 上下文管理器

`with` 语句的本质是调用对象的 `__enter__` 和 `__exit__` 方法：

```python
class MyContext:
    def __enter__(self):
        print("进入上下文")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("离开上下文")


with MyContext():
    print("执行中")
# 输出：
# 进入上下文
# 执行中
# 离开上下文
```

## pathlib 文件操作

```python
from pathlib import Path

p = Path("data.txt")

# 读取
content = p.read_text(encoding="utf-8")

# 写入
p.write_text("hello", encoding="utf-8")

# 追加
with p.open("a", encoding="utf-8") as f:
    f.write("\nworld")
```
