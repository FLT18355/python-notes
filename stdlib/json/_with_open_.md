# `with open()` 详解

`with open()` 是 Python 中推荐的文件操作方式，它利用上下文管理器自动管理文件资源。

## 一、为什么用 with open()？

不用 with（不推荐）：

```python
f = open("data.txt", "r", encoding="utf-8")
content = f.read()
f.close()
```

用 with（推荐）：

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

## 二、基本语法

```python
with open(文件路径, 模式, encoding=编码) as 变量名:
    # 操作文件
    ...
```

## 三、文件模式

| 模式 | 说明 |
|------|------|
| r | 只读（默认） |
| w | 只写，清空原内容 |
| a | 追加 |
| x | 独占创建 |
| b | 二进制 |
| + | 读写 |

## 四、读取

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())
```

## 五、写入

```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("内容\n")
```

## 六、二进制

```python
with open("image.png", "rb") as f:
    data = f.read()
```

## 七、配合 json

```python
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

## 八、pathlib

```python
from pathlib import Path

path = Path("config.json")
content = path.read_text(encoding="utf-8")
path.write_text("内容", encoding="utf-8")
```

## 九、要点

1. 始终用 with open()
2. 文本模式指定 encoding="utf-8"
3. 大文件逐行读
4. 路径拼接用 pathlib