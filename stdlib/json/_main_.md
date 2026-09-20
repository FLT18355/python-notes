Python JSON 库使用指南

Python 内置的 json 库用于处理 JSON 数据，主要包含编码（Python 对象 → JSON）和解码（JSON → Python 对象）两大功能。

一、基本导入

```python
import json
```

二、核心方法

1. json.dumps() - Python 对象转 JSON 字符串

```python
import json

data = {
    "name": "张三",
    "age": 25,
    "skills": ["Python", "Java"],
    "active": True,
    "score": None
}

# 基本用法
json_str = json.dumps(data)
print(json_str)
# {"name": "\u5f20\u4e09", "age": 25, "skills": ["Python", "Java"], "active": true, "score": null}

# 保留中文（不转义）
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
# {"name": "张三", "age": 25, ...}

# 格式化输出
json_str = json.dumps(data, ensure_ascii=False, indent=4)
print(json_str)

# 排序键
json_str = json.dumps(data, sort_keys=True)

# 自定义分隔符（紧凑输出）
json_str = json.dumps(data, separators=(',', ':'))
```

2. json.loads() - JSON 字符串转 Python 对象

```python
json_str = '{"name": "张三", "age": 25, "skills": ["Python", "Java"]}'

data = json.loads(json_str)
print(data["name"])       # 张三
print(data["skills"][0])  # Python
print(type(data))         # <class 'dict'>
```

3. json.dump() - Python 对象写入文件

```python
data = {"name": "张三", "age": 25}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```

4. json.load() - 从文件读取 JSON

```python
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
```

三、类型对应关系

Python 类型 JSON 类型
dict object
list / tuple array
str string
int / float number
True / False true / false
None null

⚠️ 注意：JSON 键必须是字符串，Python 中的 int 键会被自动转换。

四、常用参数详解

dumps / dump 常用参数

参数 说明 默认值
ensure_ascii 是否转义非 ASCII 字符 True
indent 缩进空格数 None
sort_keys 按键排序 False
separators 分隔符 (item_sep, key_sep) (', ', ': ')
default 处理无法序列化对象的函数 None

loads / load 常用参数

参数 说明
object_hook 将 dict 转换为自定义对象
parse_float 自定义 float 解析
parse_int 自定义 int 解析

五、进阶用法

1. 处理自定义对象

```python
import json
from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 使用 default 参数处理无法序列化的对象
def custom_encoder(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age}
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

user = User("张三", 25)
json_str = json.dumps(user, default=custom_encoder, ensure_ascii=False)
print(json_str)  # {"name": "张三", "age": 25}
```

2. 使用 object_hook 反序列化为对象

```python
def user_decoder(d):
    if "name" in d and "age" in d:
        return User(d["name"], d["age"])
    return d

json_str = '{"name": "张三", "age": 25}'
user = json.loads(json_str, object_hook=user_decoder)
print(user.name)  # 张三
print(type(user)) # <class '__main__.User'>
```

3. 异常处理

```python
try:
    data = json.loads('{"invalid": json}')
except json.JSONDecodeError as e:
    print(f"JSON 解析错误: {e}")
    print(f"位置: 行 {e.lineno}, 列 {e.colno}")
```

4. 处理大文件（流式解析）

对于超大 JSON 文件，json 库会把整个文件加载到内存，建议使用 ijson 库：

```python
# pip install ijson
import ijson

with open("large.json", "rb") as f:
    for record in ijson.items(f, "item"):
        print(record)
```

六、常见实战示例

读取 API 响应

```python
import json
import urllib.request

url = "https://api.example.com/data"
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))
    print(data)
```

配置文件读写

```python
# 读取配置
def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# 保存配置
def save_config(config, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

config = load_config("config.json")
config["debug"] = True
save_config(config, "config.json")
```

七、注意事项

1. 中文字符：默认 ensure_ascii=True 会把中文转义成 \uXXXX，建议设置 ensure_ascii=False
2. 文件编码：读写文件时始终指定 encoding="utf-8"
3. 类型限制：set、datetime、自定义对象等不能直接序列化，需用 default 处理
4. 性能：json 是纯 Python 实现，大量数据可考虑 orjson 或 ujson
5. 安全性：json.loads() 是安全的，不会执行任意代码（相比 eval）

八、替代库推荐

库 特点
orjson 速度极快，支持更多类型
ujson 性能优于标准库
simplejson 标准库超集，功能更多
ijson 流式解析大文件

```python
# orjson 示例
import orjson
data = orjson.loads(b'{"name": "张三"}')
json_bytes = orjson.dumps(data)
```