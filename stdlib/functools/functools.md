# functools — 函数工具

`functools` 模块提供高阶函数操作，用于函数增强和缓存。

## 导入

```python
from functools import partial, wraps, reduce, lru_cache, singledispatch, cache
```

## partial — 偏函数

固定函数的部分参数，生成新函数：

```python
from functools import partial

def power(base, exponent):
    return base ** exponent


square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125
```

## reduce — 累积

对序列进行累积操作：

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

# 求和
result = reduce(lambda a, b: a + b, nums)
print(result)  # 15

# 求最大值
result = reduce(lambda a, b: a if a > b else b, nums)
print(result)  # 5

# 阶乘
factorial = lambda n: reduce(lambda a, b: a * b, range(1, n + 1))
print(factorial(5))  # 120
```

## wraps — 保留元数据

装饰器中保留原函数信息：

```python
from functools import wraps


def timer(func):
    @wraps(func)  # 保留 __name__、__doc__ 等
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} 耗时：{end - start:.4f} 秒")
        return result
    return wrapper


@timer
def add(a, b):
    """计算两数之和"""
    return a + b


print(add.__name__)  # add（而不是 wrapper）
print(add.__doc__)   # 计算两数之和
```

## lru_cache — 缓存（记忆化）

缓存函数返回值，避免重复计算：

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))  # 354224848179261915075
# 缓存后速度极快
```

### 查看缓存统计

```python
print(fibonacci.cache_info())
# CacheInfo(hits=99, misses=101, maxsize=128, currsize=101)

# 清空缓存
fibonacci.cache_clear()
```

## cache — 无限缓存（Python 3.9+）

```python
from functools import cache


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(50))
```

## singledispatch — 单分派泛函数

根据第一个参数的类型分发到不同实现：

```python
from functools import singledispatch


@singledispatch
def process(arg):
    print(f"默认处理：{arg}")


@process.register(int)
def _(arg):
    print(f"整数处理：{arg * 2}")


@process.register(str)
def _(arg):
    print(f"字符串处理：{arg.upper()}")


@process.register(list)
def _(arg):
    print(f"列表处理：{len(arg)} 个元素")


process(10)        # 整数处理：20
process("hello")   # 字符串处理：HELLO
process([1, 2, 3]) # 列表处理：3 个元素
process(3.14)      # 默认处理：3.14
```

## cmp_to_key — 比较函数转键函数

```python
from functools import cmp_to_key


def compare(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0


nums = [3, 1, 4, 1, 5]
nums.sort(key=cmp_to_key(compare))
print(nums)  # [1, 1, 3, 4, 5]
```
