# re — 正则表达式

`re` 模块提供正则表达式匹配操作，用于复杂的字符串搜索和替换。

## 导入

```python
import re
```

## 匹配与搜索

```python
text = "邮箱：user@example.com，电话：138-0000-1234"

# re.search() — 搜索第一个匹配
m = re.search(r"\d{3}-\d{4}-\d{4}", text)
if m:
    print(m.group())  # → 138-0000-1234

# re.findall() — 找出所有匹配
phones = re.findall(r"\d{3}-\d{4}-\d{4}", text)
print(phones)  # → ['138-0000-1234']

emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)  # → ['user@example.com']

# re.match() — 从字符串开头匹配
m = re.match(r"邮箱", text)
print(m.group())  # → 邮箱
```

## 替换

```python
text = "价格：100元，折扣：50元"

# re.sub() — 替换匹配内容
result = re.sub(r"\d+", "***", text)
print(result)  # → 价格：***元，折扣：***元

# 带函数的替换
def double(m):
    return str(int(m.group()) * 2)

result = re.sub(r"\d+", double, text)
print(result)  # → 价格：200元，折扣：100元
```

## 分割

```python
text = "a,b;c|d"

# re.split() — 按正则分割
parts = re.split(r"[,;|]", text)
print(parts)  # → ['a', 'b', 'c', 'd']
```

## 常用元字符

| 元字符 | 说明 |
|--------|------|
| `.` | 匹配任意字符（除换行） |
| `^` | 字符串开头 |
| `$` | 字符串结尾 |
| `*` | 前一个字符 0 次或多次 |
| `+` | 前一个字符 1 次或多次 |
| `?` | 前一个字符 0 次或 1 次 |
| `{n}` | 恰好 n 次 |
| `{n,}` | 至少 n 次 |
| `{n,m}` | n 到 m 次 |
| `\|` | 或 |
| `\d` | 数字 [0-9] |
| `\D` | 非数字 |
| `\w` | 单词字符 [a-zA-Z0-9_] |
| `\W` | 非单词字符 |
| `\s` | 空白字符 |
| `\S` | 非空白字符 |

## 分组

```python
text = "姓名：张三，年龄：25"

# 分组提取
m = re.search(r"姓名：(\w+)，年龄：(\d+)", text)
if m:
    print(m.group(1))  # → 张三
    print(m.group(2))  # → 25
    print(m.groups())  # → ('张三', '25')

# 命名分组
m = re.search(r"姓名：(?P<name>\w+)，年龄：(?P<age>\d+)", text)
print(m.group("name"))  # → 张三
print(m.group("age"))   # → 25
```

## 常用标志

```python
re.IGNORECASE   # 忽略大小写，可简写 re.I
re.MULTILINE    # 多行模式，^$匹配每行开头结尾，可简写 re.M
re.DOTALL       # .匹配换行符，可简写 re.S
re.VERBOSE      # 忽略正则中的空白和注释
```

```python
text = "Hello World"
re.search(r"hello", text, re.IGNORECASE)  # 匹配成功
```

## compile 预编译

```python
# 多次使用同一正则时，预编译提高效率
pattern = re.compile(r"\d{3}-\d{4}-\d{4}")
pattern.search(text)
pattern.findall(text)
```

## 实战示例

```python
import re

# 验证手机号
def is_phone(num):
    return bool(re.fullmatch(r"1[3-9]\d{9}", num))

print(is_phone("13812345678"))  # → True
print(is_phone("12345678901"))  # → False

# 提取 Markdown 链接
md = "[蓝汐的笔记](https://example.com/note) 和 [GitHub](https://github.com/FLT18355)"
links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", md)
for text, url in links:
    print(f"{text} → {url}")
# → 蓝汐的笔记 → https://example.com/note
# → GitHub → https://github.com/FLT18355

# 去除 HTML 标签
html = "<p>Hello <b>World</b>!</p>"
text = re.sub(r"<[^>]+>", "", html)
print(text)  # → Hello World!
```

## 注意

- 正则默认**贪婪匹配**，加 `?` 变为非贪婪
- 特殊字符需转义：`\.` `\*` `\+` `\?` `\(` `\)` 等
- 复杂正则可用 `re.VERBOSE` 写成可读格式
