# time — 时间操作

`time` 模块提供时间相关的函数，主要用于时间戳、格式化、计时等。

## 导入

```python
import time
```

## 时间戳

```python
time.time()        # → 当前时间戳（从1970年1月1日至今的秒数）
```

## 暂停（休眠）

```python
time.sleep(1)      # 暂停1秒
time.sleep(0.5)    # 暂停0.5秒
```

## 格式化时间

```python
# 本地时间元组
lt = time.localtime()
print(lt)
# → time.struct_time(tm_year=2026, tm_mon=9, tm_mday=20, ...)

# 格式化输出
time.strftime("%Y-%m-%d %H:%M:%S")     # → "2026-09-20 18:30:00"
time.strftime("%A %B %d, %Y")          # → "Saturday September 20, 2026"

# 字符串转时间元组
t = time.strptime("2026-09-20", "%Y-%m-%d")
print(t.tm_year)  # → 2026
```

## 性能计时

```python
start = time.time()

# ... 要计时的代码 ...
total = sum(range(1000000))

end = time.time()
print(f"耗时：{end - start:.4f} 秒")
```

### 更精确的计时

```python
start = time.perf_counter()

# ... 代码 ...
time.sleep(0.1)

end = time.perf_counter()
print(f"耗时：{end - start:.6f} 秒")
```

> `perf_counter()` 精度更高，适合性能测试。

## 常用实战

### 进度条

```python
import sys

for i in range(101):
    bar = "█" * (i // 2) + "░" * (50 - i // 2)
    sys.stdout.write(f"\r[{bar}] {i}%")
    sys.stdout.flush()
    time.sleep(0.03)
print()
```

### 简单计时器

```python
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} 耗时：{end - start:.4f} 秒")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)
    return "完成"


slow_function()
```

## 格式化符号速查

| 符号 | 说明 |
|------|------|
| `%Y` | 四位年份 |
| `%m` | 月份（01-12） |
| `%d` | 日期（01-31） |
| `%H` | 小时（00-23） |
| `%M` | 分钟（00-59） |
| `%S` | 秒（00-59） |
| `%A` | 星期全名 |
| `%B` | 月份全名 |
