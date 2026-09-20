# random — 随机数

`random` 模块生成伪随机数，用于模拟、抽样、游戏等场景。

## 导入

```python
import random
```

## 生成随机数

```python
random.random()           # → [0.0, 1.0) 浮点数
random.uniform(1, 10)     # → [1.0, 10.0] 均匀分布浮点数
random.randint(1, 100)    # → [1, 100] 整数（含两端）
random.randrange(0, 100, 2)  # → 0到98的偶数
random.randrange(10)      # → [0, 10) 整数
```

## 序列操作

```python
items = ["苹果", "香蕉", "橙子", "葡萄"]

random.choice(items)       # → 随机选一个元素
random.choices(items, k=3) # → 随机选3个（可重复）
random.sample(items, 3)    # → 随机选3个（不重复）

random.shuffle(items)      # 原地打乱
print(items)  # → 随机排列
```

## 正态分布

```python
random.gauss(0, 1)         # 正态分布，均值0，标准差1
random.normalvariate(0, 1) # 同上
```

## 设定随机种子

```python
random.seed(42)
random.random()  # 每次运行结果相同
```

## 生成随机字符串

```python
import string

chars = string.ascii_letters + string.digits
random_str = ''.join(random.choices(chars, k=8))
print(random_str)  # → 8位随机字符串
```

## 实战示例

```python
import random

# 掷骰子
def roll_dice(n=1):
    return [random.randint(1, 6) for _ in range(n)]

print(roll_dice(2))  # → [3, 5]

# 抽奖
participants = ["小明", "小红", "小刚", "小丽", "小华"]
winner = random.sample(participants, 1)[0]
print(f"中奖者：{winner}")

# 生成随机密码
def generate_password(length=12):
    upper = random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2)
    lower = random.choices("abcdefghijklmnopqrstuvwxyz", k=4)
    digits = random.choices("0123456789", k=2)
    symbols = random.choices("!@#$%", k=2)
    pwd = upper + lower + digits + symbols
    random.shuffle(pwd)
    return ''.join(pwd)

print(generate_password())
```

## 范围速查

| 函数 | 说明 |
|------|------|
| `random()` | 0到1浮点数 |
| `uniform(a, b)` | a到b浮点数 |
| `randint(a, b)` | a到b整数（含两端） |
| `randrange(start, stop, step)` | 范围随机整数 |
| `choice(seq)` | 随机选一个 |
| `choices(seq, k=n)` | 随机选n个（可重复） |
| `sample(seq, k)` | 随机选k个（不重复） |
| `shuffle(seq)` | 原地打乱 |
| `gauss(mu, sigma)` | 正态分布 |
| `seed(n)` | 设置随机种子 |
