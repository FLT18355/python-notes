# itertools — 迭代器工具

`itertools` 模块提供高效的迭代器构建函数，用于处理循环和迭代。

## 导入

```python
import itertools
```

## 无限迭代器

```python
# count — 从起点开始的无限计数
for i in itertools.islice(itertools.count(1, 2), 5):
    print(i, end=" ")
# → 1 3 5 7 9

# cycle — 无限循环
for i, c in enumerate(itertools.islice(itertools.cycle("ABC"), 6)):
    print(c, end="")
# → ABCABC

# repeat — 重复值
for _ in itertools.repeat("hello", 3):
    print("hello", end=" ")
# → hello hello hello
```

## 有限迭代器

```python
# accumulate — 累积
nums = [1, 2, 3, 4, 5]
print(list(itertools.accumulate(nums)))
# → [1, 3, 6, 10, 15]

import operator
print(list(itertools.accumulate(nums, operator.mul)))
# → [1, 2, 6, 24, 120]（累积乘法）

# chain — 链接多个迭代器
for item in itertools.chain([1, 2], [3, 4], [5, 6]):
    print(item, end=" ")
# → 1 2 3 4 5 6

# compress — 根据选择器过滤
data = ["a", "b", "c", "d"]
selectors = [1, 0, 1, 0]
print(list(itertools.compress(data, selectors)))
# → ['a', 'c']

# dropwhile / takewhile
nums = [1, 4, 6, 4, 1]
print(list(itertools.takewhile(lambda x: x < 5, nums)))   # [1, 4]
print(list(itertools.dropwhile(lambda x: x < 5, nums)))   # [6, 4, 1]

# filterfalse — 保留为假的值
print(list(itertools.filterfalse(lambda x: x % 2 == 0, range(10))))
# → [1, 3, 5, 7, 9]
```

## 组合迭代器

```python
# permutations — 排列
print(list(itertools.permutations("AB", 2)))
# → [('A', 'B'), ('B', 'A')]

# combinations — 组合（不考虑顺序）
print(list(itertools.combinations("ABC", 2)))
# → [('A', 'B'), ('A', 'C'), ('B', 'C')]

# combinations_with_replacement — 可重复的组合
print(list(itertools.combinations_with_replacement("AB", 2)))
# → [('A', 'A'), ('A', 'B'), ('B', 'B')]

# product — 笛卡尔积
print(list(itertools.product("AB", "xy")))
# → [('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y')]
```

## 分组

```python
# groupby — 按键分组（要求输入已排序）
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
data.sort(key=lambda x: x[0])
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"{key}: {list(group)}")
# → a: [('a', 1), ('a', 2)]
# → b: [('b', 3), ('b', 4)]
```

## 实战示例

```python
import itertools

# 生成密码字典
lowercase = "abc"
digits = "123"
combinations = [a + b + c for a, b, c in itertools.product(lowercase, digits, lowercase)]
print(f"组合数：{len(combinations)}")

# 分批次处理大数据
data = range(100)
batch_size = 10
for batch in itertools.islice(itertools.chain(data), 0, None, batch_size):
    print(batch)

# 扁平化嵌套列表
nested = [[1, 2], [3, 4], [5, 6]]
flat = list(itertools.chain.from_iterable(nested))
print(flat)  # [1, 2, 3, 4, 5, 6]
```
