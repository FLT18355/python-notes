# collections — 高级数据结构

`collections` 模块提供额外的数据结构，是对内置类型的扩展。

## 导入

```python
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple
```

## Counter — 计数器

统计可哈希对象的出现次数：

```python
from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(words)
print(count)           # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(count["apple"])  # 3
print(count.most_common(2))  # [('apple', 3), ('banana', 2)]

# 更新计数
count.update(["apple", "grape"])
print(count["apple"])  # 4
```

## defaultdict — 默认字典

访问不存在的键时返回默认值：

```python
from collections import defaultdict

# 列表默认值
d = defaultdict(list)
d["fruits"].append("apple")
d["fruits"].append("banana")
print(d["fruits"])  # ['apple', 'banana']

# 整数默认值（计数）
counts = defaultdict(int)
for word in ["a", "b", "a", "c"]:
    counts[word] += 1
print(counts)  # {'a': 2, 'b': 1, 'c': 1}
```

## deque — 双端队列

高效地在两端添加/删除元素：

```python
from collections import deque

d = deque([1, 2, 3])
d.append(4)         # → [1, 2, 3, 4]
d.appendleft(0)     # → [0, 1, 2, 3, 4]
d.pop()             # → [0, 1, 2, 3]
d.popleft()         # → [1, 2, 3]

# 固定长度，自动丢弃旧元素
d = deque(maxlen=3)
d.extend([1, 2, 3, 4])
print(d)  # deque([2, 3, 4], maxlen=3)
```

## namedtuple — 命名元组

创建带字段名的元组：

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x)    # 3
print(p.y)    # 4
print(p[0])   # 3

# 转换为字典
print(p._asdict())  # {'x': 3, 'y': 4}
```

## OrderedDict — 有序字典

保持插入顺序（Python 3.7+ 的 dict 默认也有序）：

```python
from collections import OrderedDict

d = OrderedDict()
d["a"] = 1
d["b"] = 2
d["c"] = 3

for key, value in d.items():
    print(f"{key}: {value}")
```

## ChainMap — 合并字典

将多个字典合并为一个视图：

```python
from collections import ChainMap

defaults = {"color": "red", "user": "guest"}
user_settings = {"color": "blue"}

combined = ChainMap(user_settings, defaults)
print(combined["color"])  # blue（优先使用 user_settings）
print(combined["user"])   # guest（fallback 到 defaults）
```
