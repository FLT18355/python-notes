# datetime — 日期与时间

`datetime` 模块提供日期和时间的处理功能，是最常用的时间处理库。

## 导入

```python
from datetime import datetime, date, time, timedelta
```

## 获取当前时间

```python
now = datetime.now()
print(now)        # → 2026-09-20 18:30:00.123456
print(now.year)   # → 2026
print(now.month)  # → 9
print(now.day)    # → 20
print(now.hour)   # → 18
print(now.minute) # → 30
print(now.second) # → 0
```

## 创建指定时间

```python
d = datetime(2025, 1, 1, 12, 0, 0)
# → 2025-01-01 12:00:00
```

## 格式化输出

```python
now = datetime.now()

now.strftime("%Y-%m-%d")        # → "2026-09-20"
now.strftime("%H:%M:%S")        # → "18:30:00"
now.strftime("%Y年%m月%d日")    # → "2026年09月20日"
now.strftime("%A")              # → "Saturday"（星期几）
now.strftime("%a")              # → "Sat"（星期缩写）
```

### 格式化符号

| 符号 | 说明 |
|------|------|
| `%Y` | 四位年份 |
| `%y` | 两位年份 |
| `%m` | 月份（01-12） |
| `%d` | 日期（01-31） |
| `%H` | 小时（00-23） |
| `%I` | 小时（01-12） |
| `%M` | 分钟（00-59） |
| `%S` | 秒（00-59） |
| `%A` | 星期全名 |
| `%a` | 星期缩写 |
| `%B` | 月份全名 |
| `b` | 月份缩写 |

## 解析字符串为时间

```python
s = "2026-09-20 18:30:00"
d = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(d)  # → 2026-09-20 18:30:00
```

## 时间戳

```python
now = datetime.now()
ts = now.timestamp()            # 时间戳（秒）
back = datetime.fromtimestamp(ts)  # 时间戳转 datetime
```

## 时间差（timedelta）

```python
from datetime import timedelta

# 创建时间差
delta = timedelta(days=7, hours=3, minutes=30)

# 时间运算
now = datetime.now()
future = now + timedelta(days=7)     # 7天后
past = now - timedelta(weeks=1)      # 1周前

# 计算时间差
d1 = datetime(2026, 1, 1)
d2 = datetime(2026, 9, 20)
diff = d2 - d1
print(diff.days)    # → 262（天数）
print(diff.total_seconds())  # → 总秒数
```

## date 与 time

```python
from datetime import date, time

# 仅日期
today = date.today()
print(today)  # → 2026-09-20

# 仅时间
t = time(18, 30, 0)
print(t)  # → 18:30:00
```

## 实战示例

```python
from datetime import datetime, timedelta

# 计算年龄
birthday = datetime(2008, 9, 20)
today = datetime.now()
age = today.year - birthday.year
if (today.month, today.day) < (birthday.month, birthday.day):
    age -= 1
print(f"今年 {age} 岁")

# 倒计时
target = datetime(2027, 1, 1)
remaining = target - datetime.now()
print(f"距离目标还有 {remaining.days} 天")
```
